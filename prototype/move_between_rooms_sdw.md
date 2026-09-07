# Module Six Milestone Software Development Worksheet

* **Course**: IT 140 - Introduction to Scripting
- **Activity**: Module Six Milestone
- **Program**: Simplified Movement Prototype
- **Purpose**: Optional working notes for the M6 Construct + Test checkpoint

> [!NOTE]
> This worksheet is not a graded deliverable unless your instructor specifically
> asks for it. The graded milestone work belongs in `move_between_rooms.py`.

## How to Use This Worksheet

Keep answers brief. Use it to translate the current milestone requirements and
your Project One movement design into a small implementation plan.

## 1. Scope Check

### Where to Look

- Module Six Milestone Guidelines and Rubric
- Milestone Simplified Text Game Flowchart/supporting materials
- `../design/move.pseudo`
- `../analysis/text_based_game_srs.md`, Section 2

### Prompt

In your own words, what does the simplified milestone need to accomplish?

**Your notes:**

TODO: Summarize the milestone purpose without describing the full Project Two
game.

### Reduced-Scope Checkpoint

- [ ] I understand that the milestone uses the provided three-room dictionary.
- [ ] I understand that the milestone includes movement and `exit`.
- [ ] I understand that items, inventory, villain, and final win/loss behavior
  are deferred to Project Two.

## 2. Understand the Provided Dictionary

### Prompt

Trace the room connections before coding.

| Current room | Valid direction | Destination |
| --- | --- | --- |
| Great Hall | TODO | TODO |
| Bedroom | TODO | TODO |
| Bedroom | TODO | TODO |
| Cellar | TODO | TODO |

What should happen if a requested direction is not listed for the current room?

**Your notes:**

TODO: Describe the required validation behavior in your own words.

## 3. Input, Process, Output

### Input

TODO: What command does the player provide, and what values/categories must the
program recognize?

### Process

TODO: What decisions and state updates occur after the command is entered?

### Output

TODO: What information must the player see during normal and invalid input?

## 4. Gameplay Loop Plan

### Prompt

Describe one iteration of the loop.

1. TODO
2. TODO
3. TODO
4. TODO

What condition causes the loop to stop?

**Your notes:**

TODO

## 5. Branch Plan

Complete the behavior table without writing the full Python solution here.

| Command category | Expected behavior |
| --- | --- |
| Valid movement | TODO |
| `exit` | TODO |
| Invalid input | TODO |

## 6. Incremental Construction Check

- [ ] I can display the current room.
- [ ] I can obtain one command.
- [ ] I can recognize a valid movement command.
- [ ] I can update the current room after a valid move.
- [ ] I can recognize `exit`.
- [ ] I can reject invalid input.
- [ ] I can repeat until the exit condition is reached.

## 7. Test and Debug Notes

| Case | Expected result | Actual result | Pass? |
| --- | --- | --- | :---: |
| Valid move | TODO | TODO | TODO |
| Different valid move | TODO | TODO | TODO |
| Invalid direction | TODO | TODO | TODO |
| Invalid command | TODO | TODO | TODO |
| Exit | TODO | TODO | TODO |

**Debugging note:**

TODO: Record one defect and correction, or write `No changes needed`.

## 8. Project Two Handoff

What did you learn from this prototype that should carry into Project Two?

**Your notes:**

TODO: Record one or two useful implementation/debugging lessons.

What milestone-only behavior must **not** become the final design?

**Your notes:**

TODO: Identify the sample-world and ending differences you must revisit in M7.
