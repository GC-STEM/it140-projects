# Construct Phase | Module Seven Project Two

**Project progress:** [Start Here](../README.md) → [1 Analyze](../analysis/README.md) → [2 Design | M5](../design/README.md) → [3 Prototype | M6](../prototype/README.md) → **4 Construct | M7** → [5 Test](../tests/README.md)

## Purpose

Project Two turns your Project One design into the complete working text-based game.

The graded Project Two deliverable is:

- [`text_based_game.py`](text_based_game.py)

Unlike the Module Six prototype, the final program uses **your own rooms, items, villain, and game design**.

## Before You Code

Review these materials together:

1. Project Two Guidelines and Rubric in D2L Brightspace
2. Your [`../design/game_storyboard.md`](../design/game_storyboard.md)
3. Your [`../design/game_map.drawio`](../design/game_map.drawio)
4. Your [`../design/move.pseudo`](../design/move.pseudo)
5. Your [`../design/get_item.pseudo`](../design/get_item.pseudo)
6. Your [`../prototype/move_between_rooms.py`](../prototype/move_between_rooms.py) and any milestone feedback
7. The Project Two section of the [SRS](../analysis/text_based_game_srs.md)

If your Project One artifacts disagree, resolve the design inconsistency before building the final dictionary or command logic.

## Build the Final Game Incrementally

Use the `TODO:` prompts in `text_based_game.py` as checkpoints. A simple development order is:

1. Add the required identifying comment and review the starter structure.
2. Complete the function or functions that show instructions and player status.
3. Define `main()` and the room/item dictionary based on your Project One map.
4. Establish the player's starting room and inventory.
5. Build the gameplay loop.
6. Add movement-command handling.
7. Add get-item handling.
8. Add input validation.
9. Add the win and loss conditions.
10. Run a complete winning path and a complete losing path.

Run the program after small changes. Do not wait until every TODO is complete before testing.

## Required Functions and Organization

Project Two requires one or more functions that organize the required behavior for showing commands and showing player status. The directions allow you to organize these as separate functions or combine them.

The starter file shows one reasonable structure, but you may revise it as long as your final code meets the current Project Two requirements.

## Room and Item Dictionary

Create the final dictionary from **your Project One design**.

Before coding the whole dictionary, compare each room on your map with its:

- Valid neighboring directions
- Item, if any
- Start-room role, if applicable
- Villain-room role, if applicable

Do not copy the small Module Six dictionary as though it were your final game world.

## The Gameplay Loop

The final loop should continue while gameplay is active and allow the player to:

- See current status
- Enter a movement or get-item command
- Receive a result from that command
- Continue to another turn when the game has not ended

Project Two ends because the player **wins or loses**. Remove or redesign the milestone's simplified exit ending if you copied milestone code into the final file.

## Industry-Standard Best Practices

Use the practices required by the rubric:

- Clear variable and function names
- Consistent indentation
- Helpful comments where they improve understanding
- Readable whitespace
- Small, understandable sections of logic

Do not add complexity only to make the program look advanced. The simplest correct program is usually easier to test and maintain.

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

Before moving to Test:

- [ ] The program starts and shows required instructions/status information.
- [ ] The game data matches my Project One design.
- [ ] Movement commands are handled.
- [ ] Get-item commands are handled.
- [ ] Input validation is present.
- [ ] Inventory changes when a valid item is collected.
- [ ] The game can reach a winning outcome.
- [ ] The game can reach a losing outcome.
- [ ] The milestone-only exit condition is not being used as the final win/loss condition.

## Next Step

Continue to the [Test Phase](../tests/README.md) before submitting Project Two.
