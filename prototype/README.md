# Prototype Phase | Module Six Milestone

**Project progress:** [Start Here](../README.md) → [1 Analyze](../analysis/README.md) → [2 Design | M5](../design/README.md) → **3 Prototype | M6** → [4 Construct | M7](../src/README.md) → [5 Test](../tests/README.md)

## Purpose

The Module Six Milestone is a **working prototype** of one part of the final text-based game: moving between rooms.

You are not building the complete Project Two game yet. The milestone deliberately uses a smaller provided dragon-game dictionary so you can practice translating movement logic into Python in small steps.

The graded milestone deliverable is:

- [`move_between_rooms.py`](move_between_rooms.py)

## Before You Code

1. Read the complete Module Six Milestone Guidelines and Rubric.
2. Review the milestone video, flowchart, and other supporting materials listed in D2L Brightspace.
3. Review your Project One [`../design/move.pseudo`](../design/move.pseudo) to reconnect the movement design ideas with Python code.
4. Open the course-provided [SRS](../analysis/text_based_game_srs.md) and review the Module Six section.

> [!IMPORTANT]
> The milestone's required behavior comes from the Module Six Milestone Guidelines and Rubric. Your Project One pseudocode is a design aid, but the milestone uses the specified simplified prototype scenario.

## What the Prototype Must Do

Your milestone program should include the required behavior for:

- Showing the current room
- Prompting for a command
- Moving to a linked room after a valid movement command
- Handling the `exit` command
- Rejecting invalid commands with an appropriate message
- Repeating through a gameplay loop until the exit condition is reached
- Using decision branching to control the command paths
- Using readable comments, whitespace, and naming

The provided starter file already contains the dictionary supplied by the milestone directions. Complete the `TODO:` sections without replacing the required dictionary with the full Project Two game yet.

## Work Incrementally

A useful order is:

1. Run the starter file before making large changes.
2. Establish the current-room value.
3. Add the gameplay loop.
4. Display the current room.
5. Read one command.
6. Handle one command path at a time.
7. Test after each small change.
8. Add or revise input validation.
9. Test all required cases again.

## Run the Prototype

From the repository root:

```bash
python3 prototype/move_between_rooms.py
```

On Windows, if needed:

```powershell
python prototype/move_between_rooms.py
```

## Milestone Test Checklist

Before submitting:

- [ ] A valid movement command moves to the correct linked room.
- [ ] Another valid direction can move from a different room.
- [ ] An invalid movement command does not move the player.
- [ ] An invalid command produces the expected type of error output.
- [ ] The player can enter `exit`.
- [ ] The gameplay loop ends when the required exit condition is reached.
- [ ] The code runs without syntax errors.
- [ ] Names, comments, and whitespace make the code readable.

Use [`../tests/game_test_plan.md`](../tests/game_test_plan.md) if you want a place to record test results.

## Milestone Submission Checkpoint

Return to the [Module Six | Milestone](../README.md#module-six--milestone) section in the top-level README and follow the current D2L **What to Submit** instructions.

## Next Step

Keep this prototype after submitting it. In Module Seven, continue to the [Construct Phase](../src/README.md) for Project Two.
