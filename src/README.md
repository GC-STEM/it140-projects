# Construct | Module Seven Project Two

**Project sequence:** [Start Here](../README.md) →
[M5 Analyze](../analysis/README.md) → [M5 Design](../design/README.md) →
[M6 Construct/Test Prototype](../prototype/README.md) →
**M7 Construct** → [M7 Test](../tests/README.md)

## Purpose

Project Two is the final **Construct + Test** iteration of the three-module
SDLC. You will integrate your own Project One design into one working Python
program and verify that the required game paths behave correctly.

The graded Project Two deliverable is:

- [`text_based_game.py`](text_based_game.py)

## Inputs From Earlier Modules

Project Two should not begin from a blank design.

| Earlier artifact/evidence | How it informs Project Two |
| --- | --- |
| `design/game_storyboard.md` | Final theme, room/item names, villain, storyline |
| `design/game_map.drawio` | Final room connections and item placement |
| `design/move.pseudo` | Movement-command behavior |
| `design/get_item.pseudo` | Get-item/inventory behavior |
| Project One feedback | Corrections to make before implementation |
| `prototype/move_between_rooms.py` | Movement/dictionary/loop practice |
| Milestone feedback | Construction/debugging corrections to apply |

Review the current Project Two Guidelines and Rubric and supporting flowchart
and sample output in D2L Brightspace as well.

## The Final Game Is Different From the Milestone

| Module Six prototype | Module Seven final game |
| --- | --- |
| Provided three-room dragon dictionary | Your Project One rooms/items/villain |
| Movement only | Movement + get-item commands |
| No inventory | Inventory required |
| No villain behavior | Villain loss condition required |
| `exit` ends the loop | Win or loss ends the loop |
| Reduced practice program | Complete graded game |

If you copy useful code from the milestone, revise it to satisfy the final
requirements rather than preserving milestone-only assumptions.

## Build the Final Game Incrementally

Open [`text_based_game.py`](text_based_game.py). Use the TODO prompts as
checkpoints rather than trying to write the entire game at once.

### 1. Identify the Source

Add the full-name comment required by the current Project Two directions.

### 2. Complete the Required Function or Functions

Project Two requires function(s) that organize required behavior, including:

- Showing available commands
- Showing current room
- Showing inventory
- Showing the item in the current room when applicable

The starter separates instructions and status into two helper functions. You may
organize the functions differently if your completed program still meets the
current Project Two requirements.

### 3. Build the Final Room/Item Dictionary

Use **your Project One map**.

For every room, verify:

- Valid neighboring directions
- Destination room for each direction
- Item for that room, when applicable
- Start-room role
- Villain-room role

Do not substitute the milestone's three-room dictionary for this step.

### 4. Establish Player State

The gameplay needs at least:

- Current room
- Inventory

Choose values that match your Project One design.

### 5. Build the Gameplay Loop

One loop iteration should coordinate the player's status, command input,
command handling, state updates, and game-ending checks.

Build and run small sections incrementally.

### 6. Add Function Calls

Call the required helper function(s) from the appropriate part of gameplay so
the player sees commands and current status as required.

### 7. Add Decision Branching and Input Validation

The final game must distinguish and validate at least:

- Movement commands
- Get-item commands
- Invalid commands

Use your Project One pseudocode as the design reference for the detailed
movement and item behaviors.

### 8. Add Win and Loss Behavior

The gameplay loop continues until:

- The player **wins** by collecting all required items before encountering the
  villain, or
- The player **loses** by entering the villain room before collecting all
  required items.

Do not use the milestone's `exit` room as the final ending condition.

## Review Against the Project Two Rubric

| Rubric criterion | Weight |
| --- | ---: |
| Functions | 10% |
| Main Function: Dictionary | 10% |
| Main Function: Gameplay Loop | 15% |
| Main Function: Function Calls | 5% |
| Main Function: Decision Branching | 20% |
| Input Validation | 20% |
| Debugging | 10% |
| Industry Standard Best Practices | 10% |

The optional [`text_based_game_sdw.md`](text_based_game_sdw.md) gives you a
rubric-aligned planning and debugging checklist.

## Run the Final Game

From the repository root:

```bash
python3 src/text_based_game.py
```

On Windows, if needed:

```powershell
python src/text_based_game.py
```

## Construction Checkpoint

Before final testing:

- [ ] Required function(s) are implemented and called.
- [ ] The dictionary matches my Project One design.
- [ ] Current room and inventory are tracked.
- [ ] Movement commands work.
- [ ] Get-item commands work.
- [ ] Invalid input is handled.
- [ ] A winning outcome is reachable.
- [ ] A losing outcome is reachable.
- [ ] Milestone-only sample data and ending assumptions are gone.
- [ ] No unfinished `TODO:` or `pass` placeholders remain.

## Next Step

Continue to [Test](../tests/README.md) before submitting Project Two.
