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
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit


REPO_ROOT = Path(__file__).resolve().parents[2]

M5_GRADED_PATHS = {
    "design/game_storyboard.md",
    "design/game_map.drawio",
    "design/move.pseudo",
    "design/get_item.pseudo",
}
M6_GRADED_PATHS = {"prototype/move_between_rooms.py"}
M7_GRADED_PATHS = {"src/text_based_game.py"}
ALL_GRADED_PATHS = M5_GRADED_PATHS | M6_GRADED_PATHS | M7_GRADED_PATHS

EDITABLE_PATHS = (
    ALL_GRADED_PATHS
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
    ".github/ci/README.md",
    ".github/ci/check_readme_commands.py",
    ".github/ci/check_repository.py",
    ".github/ci/check_starter.py",
    ".github/social-preview.png",
    ".github/workflows/external-links.yml",
    ".github/workflows/readme-commands.yml",
    ".github/workflows/tests.yml",
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
        "## Three Graded Checkpoints",
        "## Set Up or Open Your Personal Projects Repository",
        "# Module Five | Project One",
        "# Module Six | Milestone",
        "# Module Seven | Project Two",
        "# Review the Automated Repository Checks",
        "# Return to Existing Work",
        "# Help and Support",
    ),
    ".github/RЕADME.md": (
        "# About the `.github` Folder",
        "## What Is Here?",
        "## Automated Repository Checks",
        "## Issue or Project Question?",
    ),
    ".github/ci/README.md": (
        "# IT 140 Projects | GitHub Continuous Integration Guide",
        "## Student CI",
        "## Course Repository CI",
        "## Maintainer Guidance",
        "## Summary",
    ),
    "analysis/README.md": (
        "# Analyze Phase | Requirements Across Modules Five–Seven",
        "## Module Five | Initial Analysis",
        "## Module Six | Reanalyze the Reduced Scope",
        "## Module Seven | Reanalyze Before Integration",
        "## Analyze Checkpoint",
    ),
    "analysis/text_based_game_srs.md": (
        "# Software Requirements Specification (SRS)",
        "## 1. Project One | Analyze and Design Requirements",
        "## 2. Module Six Milestone | Construct and Test a Reduced Prototype",
        "## 3. Project Two | Construct and Test the Complete Game",
        "## 4. Cross-Module Handoff Requirements",
    ),
    "design/README.md": (
        "# Design Phase | Module Five Project One",
        "## Graded Deliverables",
        "## 5. Review Against the Project One Rubric",
        "## Project One Submission Checkpoint",
    ),
    "design/text_based_game_sdd.md": (
        "# Software Design Document",
        "## 2. High-Level Game Model",
        "## 7. Module Six Prototype Handoff",
        "## 8. Project Two Integration Handoff",
        "## 9. Requirements Traceability",
    ),
    "prototype/README.md": (
        "# Prototype | Module Six Milestone",
        "## Prototype Scope: What Is and Is Not Included",
        "## Review Against the Milestone Rubric",
        "## Handoff to Project Two",
    ),
    "prototype/move_between_rooms_sdw.md": (
        "# Module Six Milestone Software Development Worksheet",
        "## 1. Scope Check",
        "## 7. Test and Debug Notes",
        "## 8. Project Two Handoff",
    ),
    "src/README.md": (
        "# Construct | Module Seven Project Two",
        "## Inputs From Earlier Modules",
        "## The Final Game Is Different From the Milestone",
        "## Review Against the Project Two Rubric",
        "## Construction Checkpoint",
    ),
    "src/text_based_game_sdw.md": (
        "# Project Two Software Development Worksheet",
        "## 1. Handoff Review",
        "## 7. Win and Loss Plan",
        "## 10. Final Submission Check",
    ),
    "tests/README.md": (
        "# Test | Module Six and Module Seven",
        "# Module Six | Test the Movement Prototype",
        "# Module Seven | Test the Complete Game",
        "## Final Project Two Check",
    ),
    "tests/game_test_plan.md": (
        "# Text-Based Game Test Plan",
        "# Module Six | Prototype Tests",
        "# Module Seven | Full Playthroughs",
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
    missing_or_empty = 0
    for relative_path in REQUIRED_FILES:
        path = REPO_ROOT / relative_path
        if not path.is_file():
            checks.error(f"Required file is missing: {relative_path}")
            missing_or_empty += 1
            continue
        if path.stat().st_size == 0:
            checks.error(f"Required file is empty: {relative_path}")
            missing_or_empty += 1
    if missing_or_empty == 0:
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
            checks.error("pyproject.toml must keep Ruff E and F enabled.")
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
        checks.note("Major documentation keeps its expected structure.")


def check_game_map(checks: Checks) -> None:
    """Verify the Project One game map remains parseable Draw.io XML."""
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
    """Verify course-provided flowchart references remain PNG files."""
    invalid = [
        path for path in REFERENCE_PNGS if check_png_signature(path) is None
    ]
    for path in invalid:
        checks.error(f"Provided flowchart reference is not a PNG: {path}")
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
    """Return a local Markdown path or None for external/anchor links."""
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
    """Check the repository social-preview PNG."""
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
            f"Social preview dimensions are too small: {width}x{height}."
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
        roots = git_output("rev-list", "--max-parents=0", "HEAD").splitlines()
    except RuntimeError as exc:
        checks.error(f"Could not inspect repository history: {exc}")
        return None
    if len(roots) != 1:
        checks.error("Could not identify one initial template commit.")
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
            "Course-managed repository file was added, removed, renamed, "
            f"or changed: {path}"
        )
    if not unexpected:
        checks.note("Committed changes are limited to student project files.")


def determine_checkpoint(changed: set[str]) -> int:
    """Infer the active checkpoint from later-stage graded-file changes."""
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
    """Check basic completion state of the Project One artifacts."""
    storyboard = read_text("design/game_storyboard.md")
    if "TODO:" in storyboard:
        checks.error("Project One storyboard still contains TODO prompts.")
    map_text = read_text("design/game_map.drawio")
    if "TODO" in map_text or "replace room labels" in map_text:
        checks.error("Project One game map still has starter placeholders.")
    for path in ("design/move.pseudo", "design/get_item.pseudo"):
        text = read_text(path)
        if "TODO" in text:
            checks.error(f"{path} still contains starter TODO prompts.")
        if pseudocode_statement_count(text) < 4:
            checks.error(
                f"{path} needs more pseudocode statements for a completed "
                "design."
            )
    prefixes = ("Project One", "design/")
    if not any(
        any(error.startswith(prefix) for prefix in prefixes)
        for error in checks.errors
    ):
        checks.note("Project One design artifacts replaced starter prompts.")


def parse_python(relative_path: str, checks: Checks) -> ast.Module | None:
    """Parse one project Python file and report syntax errors."""
    try:
        return ast.parse(read_text(relative_path), filename=relative_path)
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
        checks.error("Module Six prototype still contains TODO prompts.")
    tree = parse_python(path, checks)
    if tree is None:
        return
    if find_assignment_value(tree, "rooms") != EXPECTED_PROTOTYPE_ROOMS:
        checks.error(
            "Module Six prototype must keep the provided three-room "
            "movement dictionary."
        )
    if not any(
        isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree)
    ):
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
        checks.error("Module Six prototype must recognize 'exit'.")
    prefixes = ("Module Six prototype", f"{path} is not valid Python")
    if not any(
        any(error.startswith(prefix) for prefix in prefixes)
        for error in checks.errors
    ):
        checks.note("Module Six prototype has the expected basic structure.")


def check_project_two_completion(checks: Checks) -> None:
    """Check basic Project Two structure without grading game content."""
    path = "src/text_based_game.py"
    text = read_text(path)
    if "TODO:" in text:
        checks.error("Project Two source still contains TODO prompts.")
    tree = parse_python(path, checks)
    if tree is None:
        return
    if any(isinstance(node, ast.Pass) for node in ast.walk(tree)):
        checks.error("Project Two source still contains pass placeholders.")
    functions = [
        node for node in tree.body if isinstance(node, ast.FunctionDef)
    ]
    if not any(node.name == "main" for node in functions):
        checks.error("Project Two source must contain main().")
    if len(functions) < 2:
        checks.error(
            "Project Two source must use at least one helper function in "
            "addition to main()."
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
    if not any(
        isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree)
    ):
        checks.error("Project Two source must contain a gameplay loop.")
    if not any(isinstance(node, ast.If) for node in ast.walk(tree)):
        checks.error("Project Two source must use decision branching.")
    if not calls_named(tree, "input"):
        checks.error("Project Two source must obtain player commands.")
    if not calls_named(tree, "print"):
        checks.error("Project Two source must display game information.")
    prefixes = ("Project Two source", f"{path} is not valid Python")
    if not any(
        any(error.startswith(prefix) for prefix in prefixes)
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

    graded_changes = changed & ALL_GRADED_PATHS
    if not graded_changes:
        checks.note(
            "No graded project checkpoint has started; untouched starter "
            "deliverables are a neutral state."
        )
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
        help="Validate the course starter or a personal project repository.",
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
    else:
        checks.note("Starter mode skips student checkpoint completion checks.")

    checks.finish()


if __name__ == "__main__":
    main()
