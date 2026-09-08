# Prototype | Module Six Milestone

**Project sequence:** [Start Here](../README.md) →
[M5 Analyze](../analysis/README.md) → [M5 Design](../design/README.md) →
**M6 Construct/Test Prototype** → [M7 Construct](../src/README.md) →
[M7 Test](../tests/README.md)

## Purpose

The Module Six Milestone is a **reduced Construct + Test iteration** of the
project SDLC. You will build one working portion of the larger text game before
integrating the complete system in Module Seven.

The graded milestone deliverable is:

- [`move_between_rooms.py`](move_between_rooms.py)

## Prototype Scope: What Is and Is Not Included

| Included in M6 | Intentionally deferred to M7 |
| --- | --- |
| Provided three-room dragon dictionary | Your Project One room map |
| Current-room output | Items in rooms |
| Movement commands | Inventory |
| `exit` command | Villain behavior |
| Gameplay loop | Winning by collecting all items |
| Decision branching | Losing by entering villain room too early |
| Input validation | Get-item command |
| Debugging/readability | Full-game functions and integration |

This boundary is important. A successful milestone is **not** supposed to look
like the complete Project Two game.

## Before You Code

Review:

1. Module Six Milestone Guidelines and Rubric in D2L Brightspace
2. Milestone Simplified Dragon Text Game supporting resources
3. Your Project One [`../design/move.pseudo`](../design/move.pseudo)
4. Project One instructor feedback related to movement
5. [SRS Section 2](../analysis/text_based_game_srs.md#2-module-six-milestone--construct-and-test-a-reduced-prototype)

Your Project One movement pseudocode can help you think about input, validation,
branching, and room updates. The milestone's **actual required scenario** still
comes from the current milestone Guidelines and Rubric.

## Provided Dictionary

The starter already includes the exact simplified dictionary supplied by the
milestone:

```python
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}
```

Read it carefully before coding. Do not replace it with your Project One rooms
for this checkpoint.

## Build the Prototype Incrementally

Open [`move_between_rooms.py`](move_between_rooms.py).

A useful development sequence is:

1. Establish the starting room.
2. Create the gameplay loop.
3. Display the current room.
4. Prompt for one command.
5. Handle a valid movement command.
6. Handle `exit`.
7. Handle invalid input.
8. Repeat until the required exit condition is reached.
9. Test each branch and fix one defect at a time.

The optional [`move_between_rooms_sdw.md`](move_between_rooms_sdw.md) gives you
working space for this reduced problem.

## Run the Prototype

Run the prototype from the repository root. **Windows users must use Git Bash**
for this `bash` command block.

<!-- ci:command-test id=run-module-six-prototype fixture=existing-repo expect=repo -->
```bash
cd ~/Repos/it140-projects
python3 prototype/move_between_rooms.py
```

## Review Against the Milestone Rubric

| Rubric criterion | Weight | Evidence to review |
| --- | ---: | --- |
| Functionality | 30% | Required movement and exit behavior works |
| Gameplay Loop | 10% | Repetition controls continued play |
| Decision Branching | 20% | Valid move, exit, and invalid paths are handled |
| Input Validation | 20% | Invalid commands are rejected appropriately |
| Debugging | 10% | Required cases were run and corrected |
| Industry Standard Best Practices | 10% | Comments, whitespace, and names support readability |

## Test the Milestone

Use the Module Six section of [`../tests/README.md`](../tests/README.md).

At minimum, check:

- [ ] A valid move from the Great Hall.
- [ ] A valid move from the Bedroom.
- [ ] An invalid direction.
- [ ] An invalid command.
- [ ] The `exit` command.
- [ ] The loop ends at the required exit condition.
- [ ] The program runs without syntax errors.
- [ ] Names, comments, and whitespace are readable.

## Milestone Submission Checkpoint

Submit `move_between_rooms.py` in D2L Brightspace according to the current
Module Six What to Submit instructions.

Keep the file and review instructor feedback after grading.

## Handoff to Project Two

In Module Seven:

**Reuse or adapt:**

- Movement/dictionary techniques that worked
- Loop and branching experience
- Input-validation lessons
- Debugging lessons and instructor feedback

**Replace or expand:**

- Replace the three-room sample data with your Project One world.
- Add item and inventory behavior.
- Add required functions and function calls.
- Replace the milestone `exit` ending with the Project Two win/loss conditions.

Continue to the [Project Two Construct instructions](../src/README.md).
