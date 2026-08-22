"""Validate the IT 140 Projects repository and project checkpoints."""

from __future__ import annotations

import argparse
import ast
import json
import re
import struct
import subprocess
import sys
import tomllib
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


REPO_ROOT = Path(__file__).resolve().parents[2]

M5_GRADED_PATHS = {
    "design/game_storyboard.md",
    "design/game_map.drawio",
    "design/move.pseudo",
    "design/get_item.pseudo",
}

M6_GRADED_PATHS = {
    "prototype/move_between_rooms.py",
}

M7_GRADED_PATHS = {
    "src/text_based_game.py",
}

EDITABLE_PATHS = (
    M5_GRADED_PATHS
    | M6_GRADED_PATHS
    | M7_GRADED_PATHS
    | {
        "prototype/move_between_rooms_sdw.md",
        "src/text_based_game_sdw.md",
        "tests/game_test_plan.md",
    }
)

REQUIRED_FILES = (
    ".gitattributes",
    ".gitignore",
    "README.md",
    "pyproject.toml",
    ".github/RЕADME.md",
    ".github/ISSUE_TEMPLATE/report-a-problem.yml",
    ".github/ISSUE_TEMPLATE/request-an-improvement.yml",
    ".github/ci/check_repository.py",
    ".github/ci/check_starter.py",
    ".github/social-preview.png",
    ".github/workflows/external-links.yml",
    ".github/workflows/tests.yml",
    ".github/workflows/tests.yml.disabled",
    ".vscode/settings.json",
    "analysis/README.md",
    "analysis/text_based_game_srs.md",
    "design/README.md",
    "design/game_storyboard.md",
    "design/game_map.drawio",
    "design/get_item.drawio.png",
    "design/get_item.pseudo",
    "design/move.drawio.png",
    "design/move.pseudo",
    "design/tbg_flowchart.drawio.png",
    "design/text_based_game_sdd.md",
    "prototype/README.md",
    "prototype/move_between_rooms.py",
    "prototype/move_between_rooms_sdw.md",
    "src/README.md",
    "src/text_based_game.py",
    "src/text_based_game_sdw.md",
    "tests/README.md",
    "tests/game_test_plan.md",
    "tests/test_move_between_rooms.py",
    "tests/test_text_based_game.py",
)

REQUIRED_TEXT_MARKERS = {
    "README.md": (
        "# IT 140 Projects | Modules Five–Seven",
        "## Module Five | Project One",
        "## Module Six | Milestone",
        "## Module Seven | Project Two",
        "## Review the Automated Repository Checks",
        "## Help and Support",
    ),
    ".github/RЕADME.md": (
        "# About the `.github` Folder",
        "## Automated Repository Checks",
        "## Issue or Project Question?",
    ),
    "analysis/README.md": (
        "# Analyze Phase | Understand the Text-Game Requirements",
        "## Purpose",
        "## Analyze Checkpoint",
    ),
    "analysis/text_based_game_srs.md": (
        "# Software Requirements Specification (SRS)",
        "## 1. Project One | Game Design Requirements",
        "## 2. Module Six Milestone | Simplified Prototype Requirements",
        "## 3. Project Two | Full Game Requirements",
    ),
    "design/README.md": (
        "# Design Phase | Module Five Project One",
        "## Graded Deliverables",
        "## Project One Submission Checkpoint",
    ),
    "design/text_based_game_sdd.md": (
        "# Software Design Document",
        "## 2. High-Level Game Model",
    ),
    "prototype/README.md": (
        "# Prototype Phase | Module Six Milestone",
        "## What the Prototype Must Do",
        "## Milestone Submission Checkpoint",
    ),
    "src/README.md": (
        "# Construct Phase | Module Seven Project Two",
        "## Required Functions and Organization",
        "## Construction Checkpoint",
    ),
    "tests/README.md": (
        "# Test Phase | Module Six and Module Seven",
        "## Module Six Prototype Tests",
        "## Final Project Two Check",
    ),
}

REFERENCE_PNGS = (
    "design/get_item.drawio.png",
    "design/move.drawio.png",
    "design/tbg_flowchart.drawio.png",
)

EXPECTED_PROTOTYPE_ROOMS = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class Checks:
    """Collect validation results and emit one useful report."""

    def __init__(self) -> None:
        self.errors: list[str] = []
        self.notes: list[str] = []

    def error(self, message: str) -> None:
        """Record a failing check."""
        self.errors.append(message)

    def note(self, message: str) -> None:
        """Record a successful or informational check."""
        self.notes.append(message)

    def finish(self) -> None:
        """Print results and exit nonzero if any checks failed."""
        for note in self.notes:
            print(f"PASS: {note}")

        if not self.errors:
            print("PASS: Repository and project checks completed.")
            return

        print("\nRepository checks failed:", file=sys.stderr)
        for error in self.errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)


def read_text(relative_path: str) -> str:
    """Read one repository text file as UTF-8."""
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def check_required_files(checks: Checks) -> None:
    """Verify required repository files exist and are nonempty."""
    for relative_path in REQUIRED_FILES:
        path = REPO_ROOT / relative_path
        if not path.is_file():
            checks.error(f"Required file is missing: {relative_path}")
            continue
        if path.stat().st_size == 0:
            checks.error(f"Required file is empty: {relative_path}")

    if not checks.errors:
        checks.note("Required repository files are present and nonempty.")


def check_json_and_toml(checks: Checks) -> None:
    """Parse repository JSON and TOML configuration files."""
    settings_path = REPO_ROOT / ".vscode/settings.json"
    pyproject_path = REPO_ROOT / "pyproject.toml"

    try:
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
        if not isinstance(settings, dict):
            checks.error(".vscode/settings.json must contain a JSON object.")
    except (OSError, json.JSONDecodeError) as exc:
        checks.error(f"Invalid .vscode/settings.json: {exc}")

    try:
        with pyproject_path.open("rb") as handle:
            pyproject = tomllib.load(handle)
        lint = pyproject.get("tool", {}).get("ruff", {}).get("lint", {})
        selected = set(lint.get("select", []))
        if not {"E", "F"}.issubset(selected):
            checks.error(
                "pyproject.toml must keep Ruff E and F checks enabled."
            )
    except (OSError, tomllib.TOMLDecodeError) as exc:
        checks.error(f"Invalid pyproject.toml: {exc}")


def check_required_text_markers(checks: Checks) -> None:
    """Verify major course-managed documents keep expected sections."""
    missing = 0
    for relative_path, markers in REQUIRED_TEXT_MARKERS.items():
        text = read_text(relative_path)
        for marker in markers:
            if marker not in text:
                checks.error(
                    f"Required section is missing from {relative_path}: "
                    f"{marker}"
                )
                missing += 1

    if missing == 0:
        checks.note("Major Markdown artifacts keep their expected sections.")


def check_game_map(checks: Checks) -> None:
    """Verify the Project One game-map file remains parseable Draw.io XML."""
    path = REPO_ROOT / "design/game_map.drawio"
    try:
        root = ET.parse(path).getroot()
    except (OSError, ET.ParseError) as exc:
        checks.error(f"Invalid Draw.io XML in design/game_map.drawio: {exc}")
        return

    tag = root.tag.rsplit("}", maxsplit=1)[-1]
    if tag != "mxfile":
        checks.error("design/game_map.drawio must have an mxfile root.")
        return

    diagrams = [
        node
        for node in root.iter()
        if node.tag.rsplit("}", maxsplit=1)[-1] == "diagram"
    ]
    if not diagrams:
        checks.error("design/game_map.drawio contains no diagram page.")
        return

    checks.note("The Project One game map is parseable Draw.io XML.")


def check_png_signature(relative_path: str) -> tuple[int, int] | None:
    """Return PNG width and height when the file has a valid PNG header."""
    data = (REPO_ROOT / relative_path).read_bytes()
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", data[16:24])


def check_reference_pngs(checks: Checks) -> None:
    """Verify course-provided flowchart reference images remain PNG files."""
    invalid = [
        path for path in REFERENCE_PNGS if check_png_signature(path) is None
    ]
    for path in invalid:
        checks.error(f"Provided flowchart reference is not a valid PNG: {path}")

    if not invalid:
        checks.note("Provided flowchart reference PNG files are valid.")


def without_code_fences(text: str) -> str:
    """Remove fenced code blocks before scanning Markdown links."""
    output: list[str] = []
    in_fence = False
    fence_marker = ""

    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            continue
        if not in_fence:
            output.append(line)

    return "\n".join(output)


def local_link_target(raw_target: str) -> str | None:
    """Return a local Markdown link path or None for external/anchor links."""
    target = raw_target.strip()
    if not target:
        return None

    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(maxsplit=1)[0]

    if target.startswith("#"):
        return None

    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None

    path = unquote(parsed.path)
    if not path or path.startswith("/"):
        return None
    return path


def check_markdown_links(checks: Checks) -> None:
    """Verify local links in repository Markdown files resolve."""
    broken = 0
    repo_root = REPO_ROOT.resolve()

    for file_path in sorted(REPO_ROOT.rglob("*.md")):
        if ".git" in file_path.parts:
            continue

        relative_path = file_path.relative_to(REPO_ROOT)
        text = without_code_fences(file_path.read_text(encoding="utf-8"))

        for match in MARKDOWN_LINK.finditer(text):
            target = local_link_target(match.group(1))
            if target is None:
                continue

            resolved = (file_path.parent / target).resolve()
            try:
                resolved.relative_to(repo_root)
            except ValueError:
                checks.error(
                    f"Local link leaves the repository in {relative_path}: "
                    f"{target}"
                )
                broken += 1
                continue

            if not resolved.exists():
                checks.error(
                    f"Broken local link in {relative_path}: {target}"
                )
                broken += 1

    if broken == 0:
        checks.note("Local links in Markdown files resolve.")


def check_social_preview(checks: Checks) -> None:
    """Check the repository social-preview PNG signature, size, and ratio."""
    path = REPO_ROOT / ".github/social-preview.png"
    data = path.read_bytes()

    if len(data) > 1_048_576:
        checks.error(".github/social-preview.png must remain under 1 MiB.")
        return

    dimensions = check_png_signature(".github/social-preview.png")
    if dimensions is None:
        checks.error(".github/social-preview.png is not a valid PNG file.")
        return

    width, height = dimensions
    if width < 640 or height < 320:
        checks.error(
            "Social preview dimensions are unexpectedly small: "
            f"{width}x{height}."
        )
        return

    ratio = width / height
    if not 1.9 <= ratio <= 2.1:
        checks.error(
            "Social preview should remain approximately 2:1; "
            f"found {width}x{height}."
        )
        return

    checks.note(
        f"Social preview is valid ({width}x{height}, {len(data)} bytes)."
    )


def git_output(*args: str) -> str:
    """Run Git and return stripped standard output."""
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(message or "Git command failed.")
    return result.stdout.strip()


def student_changed_paths(checks: Checks) -> set[str] | None:
    """Return committed paths changed since the template root commit."""
    try:
        roots = git_output(
            "rev-list",
            "--max-parents=0",
            "HEAD",
        ).splitlines()
    except RuntimeError as exc:
        checks.error(f"Could not inspect repository history: {exc}")
        return None

    if len(roots) != 1:
        checks.error(
            "Could not identify one initial template commit for this "
            "personal repository."
        )
        return None

    try:
        changed_text = git_output(
            "diff",
            "--name-only",
            "--diff-filter=ACDMRTUXB",
            roots[0],
            "HEAD",
        )
    except RuntimeError as exc:
        checks.error(f"Could not compare with the template commit: {exc}")
        return None

    return {line for line in changed_text.splitlines() if line}


def check_student_change_scope(
    checks: Checks,
    changed: set[str] | None,
) -> None:
    """Ensure committed changes are limited to student-editable files."""
    if changed is None:
        return

    unexpected = sorted(changed - EDITABLE_PATHS)
    for path in unexpected:
        checks.error(
            "Course-managed repository file was added, removed, renamed, or "
            f"changed: {path}"
        )

    if not unexpected:
        checks.note(
            "Committed changes are limited to student project/working files."
        )


def determine_checkpoint(changed: set[str]) -> int:
    """Infer the active graded checkpoint from later-stage file changes."""
    if changed & M7_GRADED_PATHS:
        return 7
    if changed & M6_GRADED_PATHS:
        return 6
    return 5


def require_changed_paths(
    checks: Checks,
    changed: set[str],
    required: set[str],
    checkpoint_name: str,
) -> None:
    """Require checkpoint deliverables to differ from the starter commit."""
    missing = sorted(required - changed)
    for path in missing:
        checks.error(
            f"{checkpoint_name} deliverable has not changed from the "
            f"starter template: {path}"
        )


def pseudocode_statement_count(text: str) -> int:
    """Count nonempty pseudocode lines that are not comments."""
    return sum(
        1
        for line in text.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    )


def check_project_one_completion(checks: Checks) -> None:
    """Check basic completion state of the four Project One artifacts."""
    storyboard = read_text("design/game_storyboard.md")
    if "TODO:" in storyboard:
        checks.error(
            "Project One storyboard still contains starter TODO prompts."
        )

    map_text = read_text("design/game_map.drawio")
    if "TODO" in map_text or "replace room labels" in map_text:
        checks.error(
            "Project One game map still contains starter placeholder text."
        )

    for path in ("design/move.pseudo", "design/get_item.pseudo"):
        text = read_text(path)
        if "TODO" in text:
            checks.error(f"{path} still contains starter TODO prompts.")
        if pseudocode_statement_count(text) < 4:
            checks.error(
                f"{path} does not contain enough pseudocode statements "
                "to represent a completed design."
            )

    if not any(
        error.startswith("Project One")
        or error.startswith("design/")
        for error in checks.errors
    ):
        checks.note(
            "Project One design artifacts have replaced starter prompts."
        )


def parse_python(relative_path: str, checks: Checks) -> ast.Module | None:
    """Parse one project Python file and report syntax errors."""
    text = read_text(relative_path)
    try:
        return ast.parse(text, filename=relative_path)
    except SyntaxError as exc:
        checks.error(f"{relative_path} is not valid Python: {exc}")
        return None


def find_assignment_value(tree: ast.Module, name: str) -> object | None:
    """Return a literal value assigned to one top-level variable."""
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            continue
        try:
            return ast.literal_eval(node.value)
        except (ValueError, TypeError):
            return None
    return None


def calls_named(tree: ast.AST, name: str) -> bool:
    """Return True when an AST contains a call to a simple function name."""
    return any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == name
        for node in ast.walk(tree)
    )


def has_main_guard(tree: ast.Module) -> bool:
    """Return True when one module guard calls main()."""
    for node in tree.body:
        if not isinstance(node, ast.If):
            continue
        test_text = ast.unparse(node.test)
        if "__name__" not in test_text or "__main__" not in test_text:
            continue
        if any(
            isinstance(child, ast.Call)
            and isinstance(child.func, ast.Name)
            and child.func.id == "main"
            for child in ast.walk(node)
        ):
            return True
    return False


def check_milestone_completion(checks: Checks) -> None:
    """Check basic Module Six milestone structure."""
    path = "prototype/move_between_rooms.py"
    text = read_text(path)
    if "TODO:" in text:
        checks.error(
            "Module Six prototype still contains starter TODO prompts."
        )

    tree = parse_python(path, checks)
    if tree is None:
        return

    if find_assignment_value(tree, "rooms") != EXPECTED_PROTOTYPE_ROOMS:
        checks.error(
            "Module Six prototype must keep the provided three-room "
            "movement dictionary."
        )

    has_loop = any(
        isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree)
    )
    if not has_loop:
        checks.error("Module Six prototype must contain a gameplay loop.")
    if not any(isinstance(node, ast.If) for node in ast.walk(tree)):
        checks.error("Module Six prototype must use decision branching.")
    if not calls_named(tree, "input"):
        checks.error("Module Six prototype must obtain a player command.")
    if not calls_named(tree, "print"):
        checks.error("Module Six prototype must display player information.")
    if not any(
        isinstance(node, ast.Constant) and node.value == "exit"
        for node in ast.walk(tree)
    ):
        checks.error("Module Six prototype must recognize the 'exit' command.")

    milestone_errors = (
        "Module Six prototype",
        f"{path} is not valid Python",
    )
    if not any(
        any(error.startswith(prefix) for prefix in milestone_errors)
        for error in checks.errors
    ):
        checks.note("Module Six prototype has the expected basic structure.")


def check_project_two_completion(checks: Checks) -> None:
    """Check basic Project Two source structure without grading game content."""
    path = "src/text_based_game.py"
    text = read_text(path)
    if "TODO:" in text:
        checks.error("Project Two source still contains starter TODO prompts.")

    tree = parse_python(path, checks)
    if tree is None:
        return

    if any(isinstance(node, ast.Pass) for node in ast.walk(tree)):
        checks.error("Project Two source still contains pass placeholders.")

    functions = [
        node for node in tree.body if isinstance(node, ast.FunctionDef)
    ]
    if not any(node.name == "main" for node in functions):
        checks.error("Project Two source must contain a main() function.")
    if len(functions) < 2:
        checks.error(
            "Project Two source must use at least one helper function "
            "in addition to main()."
        )
    if not has_main_guard(tree):
        checks.error("Project Two source must run main() from a main guard.")

    has_dictionary = any(isinstance(node, ast.Dict) for node in ast.walk(tree))
    has_dictionary |= calls_named(tree, "dict")
    if not has_dictionary:
        checks.error("Project Two source must create a room/item dictionary.")

    has_inventory = any(isinstance(node, ast.List) for node in ast.walk(tree))
    has_inventory |= calls_named(tree, "list")
    if not has_inventory:
        checks.error("Project Two source must create an inventory list.")

    has_loop = any(
        isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree)
    )
    if not has_loop:
        checks.error("Project Two source must contain a gameplay loop.")
    if not any(isinstance(node, ast.If) for node in ast.walk(tree)):
        checks.error("Project Two source must use decision branching.")
    if not calls_named(tree, "input"):
        checks.error("Project Two source must obtain player commands.")
    if not calls_named(tree, "print"):
        checks.error("Project Two source must display game information.")

    project_two_prefixes = (
        "Project Two source",
        f"{path} is not valid Python",
    )
    if not any(
        any(error.startswith(prefix) for prefix in project_two_prefixes)
        for error in checks.errors
    ):
        checks.note("Project Two source has the expected basic structure.")


def check_student_checkpoint(
    checks: Checks,
    changed: set[str] | None,
) -> None:
    """Validate the appropriate progressive project checkpoint."""
    if changed is None:
        return

    checkpoint = determine_checkpoint(changed)

    require_changed_paths(
        checks,
        changed,
        M5_GRADED_PATHS,
        "Project One",
    )
    check_project_one_completion(checks)

    if checkpoint >= 6:
        require_changed_paths(
            checks,
            changed,
            M6_GRADED_PATHS,
            "Module Six Milestone",
        )
        check_milestone_completion(checks)

    if checkpoint >= 7:
        require_changed_paths(
            checks,
            changed,
            M7_GRADED_PATHS,
            "Project Two",
        )
        check_project_two_completion(checks)

    checks.note(
        f"Personal repository checkpoint detected: Module {checkpoint}."
    )


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        required=True,
        choices=("starter", "student"),
        help="Validate the course starter or a personal student repository.",
    )
    return parser.parse_args()


def main() -> None:
    """Run repository and project checks."""
    args = parse_args()
    checks = Checks()

    check_required_files(checks)
    if checks.errors:
        checks.finish()

    check_json_and_toml(checks)
    check_required_text_markers(checks)
    check_game_map(checks)
    check_reference_pngs(checks)
    check_markdown_links(checks)
    check_social_preview(checks)

    if args.mode == "student":
        changed = student_changed_paths(checks)
        check_student_change_scope(checks, changed)
        check_student_checkpoint(checks, changed)

    checks.finish()


if __name__ == "__main__":
    main()
