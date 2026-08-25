"""Validate the intentional starter state of the IT 140 Projects repo."""

from __future__ import annotations

import ast
import sys
from pathlib import Path
import xml.etree.ElementTree as ET


REPO_ROOT = Path(__file__).resolve().parents[2]

EXPECTED_PROTOTYPE_ROOMS = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

STORYBOARD_MARKERS = (
    "TODO: Name and briefly describe your game's theme.",
    "TODO: In one short paragraph",
    "TODO: Start room",
    "TODO: Villain room",
    "TODO: Identify and briefly describe the villain.",
)
MOVE_MARKERS = tuple(f"TODO {number}:" for number in range(1, 7))
GET_ITEM_MARKERS = tuple(f"TODO {number}:" for number in range(1, 7))
PROTOTYPE_MARKERS = (
    "TODO: Set the player's starting room",
    "TODO: Create the gameplay loop",
    "TODO: Run and debug all milestone cases",
)
FINAL_SOURCE_MARKERS = (
    "TODO: Add the full-name comment",
    "TODO: Print instructions",
    "TODO: Show the current room.",
    "TODO: Show the current inventory.",
    "TODO: Create the full room/item dictionary",
    "TODO: Set the player's starting room.",
    "TODO: Create the player's inventory.",
    "TODO: Create the gameplay loop.",
)


class StarterChecks:
    """Collect starter validation failures."""

    def __init__(self) -> None:
        self.errors: list[str] = []

    def error(self, message: str) -> None:
        """Record a failing starter check."""
        self.errors.append(message)

    def finish(self) -> None:
        """Print results and exit nonzero when starter checks fail."""
        if not self.errors:
            print("PASS: Course starter state is intentionally incomplete.")
            print("PASS: Project One design templates are intact.")
            print("PASS: Module Six prototype starter is intact.")
            print("PASS: Project Two source starter is intact.")
            return
        print("Course starter checks failed:", file=sys.stderr)
        for error in self.errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)


def parse_python(
    relative_path: str,
    checks: StarterChecks,
) -> ast.Module | None:
    """Parse one starter Python file."""
    path = REPO_ROOT / relative_path
    try:
        return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as exc:
        checks.error(f"Starter Python is not valid in {relative_path}: {exc}")
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


def check_storyboard(checks: StarterChecks) -> None:
    """Verify the Project One storyboard starter markers."""
    text = (REPO_ROOT / "design/game_storyboard.md").read_text(
        encoding="utf-8"
    )
    for marker in STORYBOARD_MARKERS:
        if marker not in text:
            checks.error(f"Storyboard starter is missing marker: {marker!r}")


def check_game_map(checks: StarterChecks) -> None:
    """Verify the Project One map starter placeholders."""
    path = REPO_ROOT / "design/game_map.drawio"
    try:
        root = ET.parse(path).getroot()
    except (OSError, ET.ParseError) as exc:
        checks.error(f"Game-map starter is not valid Draw.io XML: {exc}")
        return
    text = path.read_text(encoding="utf-8")
    required = (
        'name="Game Map"',
        "replace room labels",
        "Room 1",
        "Room 8",
        "Item: TODO",
        "TODO: Rename rooms",
    )
    for marker in required:
        if marker not in text:
            checks.error(f"Game-map starter is missing marker: {marker!r}")
    tag = root.tag.rsplit("}", maxsplit=1)[-1]
    if tag != "mxfile":
        checks.error("Game-map starter must keep an mxfile root.")


def check_pseudocode(checks: StarterChecks) -> None:
    """Verify both Project One pseudocode starter templates."""
    cases = (
        ("design/move.pseudo", MOVE_MARKERS),
        ("design/get_item.pseudo", GET_ITEM_MARKERS),
    )
    for relative_path, markers in cases:
        text = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                checks.error(
                    f"{relative_path} starter is missing marker: {marker!r}"
                )


def check_prototype(checks: StarterChecks) -> None:
    """Verify the Module Six simplified prototype starter."""
    relative_path = "prototype/move_between_rooms.py"
    path = REPO_ROOT / relative_path
    text = path.read_text(encoding="utf-8")
    for marker in PROTOTYPE_MARKERS:
        if marker not in text:
            checks.error(f"Prototype starter is missing marker: {marker!r}")
    tree = parse_python(relative_path, checks)
    if tree is None:
        return
    if find_assignment_value(tree, "rooms") != EXPECTED_PROTOTYPE_ROOMS:
        checks.error(
            "Prototype starter must keep the provided three-room dictionary."
        )
    executable = [
        node
        for node in tree.body
        if not (
            isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Constant)
            and isinstance(node.value.value, str)
        )
    ]
    assignments = [node for node in executable if isinstance(node, ast.Assign)]
    if len(executable) != 1 or len(assignments) != 1:
        checks.error(
            "Prototype starter must remain incomplete after the rooms "
            "dictionary."
        )


def check_final_source(checks: StarterChecks) -> None:
    """Verify Project Two source remains a valid incomplete starter."""
    relative_path = "src/text_based_game.py"
    path = REPO_ROOT / relative_path
    text = path.read_text(encoding="utf-8")
    for marker in FINAL_SOURCE_MARKERS:
        if marker not in text:
            checks.error(
                f"Project Two starter is missing marker: {marker!r}"
            )
    tree = parse_python(relative_path, checks)
    if tree is None:
        return
    functions = {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }
    expected = {"show_instructions", "show_status", "main"}
    if set(functions) != expected:
        checks.error(
            "Project Two starter must keep show_instructions(), "
            "show_status(), and main()."
        )
    for name in expected:
        function = functions.get(name)
        if function is None:
            continue
        if not any(isinstance(node, ast.Pass) for node in function.body):
            checks.error(
                f"Project Two starter function {name}() must remain "
                "intentionally incomplete."
            )
    guards = [
        node
        for node in tree.body
        if isinstance(node, ast.If)
        and "__name__" in ast.unparse(node.test)
        and "__main__" in ast.unparse(node.test)
    ]
    if len(guards) != 1:
        checks.error("Project Two starter must contain one main guard.")
    elif not any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "main"
        for node in ast.walk(guards[0])
    ):
        checks.error("The Project Two main guard must call main().")


def main() -> None:
    """Run all course-starter checks."""
    checks = StarterChecks()
    check_storyboard(checks)
    check_game_map(checks)
    check_pseudocode(checks)
    check_prototype(checks)
    check_final_source(checks)
    checks.finish()


if __name__ == "__main__":
    main()
