# Project Two Software Development Worksheet

* **Course**: IT 140 - Introduction to Scripting
- **Activity**: Project Two
- **Program**: Complete Text-Based Adventure Game
- **Purpose**: Optional working notes for the M7 Construct + Test checkpoint

> [!NOTE]
> This worksheet is not a graded deliverable unless your instructor specifically
> asks for it. The graded Project Two work belongs in `text_based_game.py`.

## 1. Handoff Review

### Where to Look

Review:

- Current Project Two Guidelines and Rubric
- `../design/game_storyboard.md`
- `../design/game_map.drawio`
- `../design/move.pseudo`
- `../design/get_item.pseudo`
- Project One instructor feedback
- `../prototype/move_between_rooms.py`
- Module Six instructor feedback

### Handoff Checkpoint

- [ ] My storyboard and map agree.
- [ ] I reviewed Project One feedback.
- [ ] I reviewed milestone feedback.
- [ ] I know which milestone ideas can be reused.
- [ ] I know which milestone sample behaviors must be replaced.

## 2. Prototype-to-Final Differences

Complete this before copying or adapting milestone code.

| Concern | Module Six | Project Two |
| --- | --- | --- |
| Game world | Provided sample | TODO: My own design |
| Items/inventory | Not included | TODO |
| Villain | Not included | TODO |
| Ending | `exit` | TODO |
| Commands | Movement + exit | TODO |

## 3. Final Dictionary Plan

Use the Project One map as the source. Record only what helps you verify the
translation.

| Room | Neighbor directions to verify | Item, if any |
| --- | --- | --- |
| TODO | TODO | TODO |
| TODO | TODO | TODO |
| TODO | TODO | TODO |

Add rows as needed.

### Dictionary Checkpoint

- [ ] Every Project One room is represented.
- [ ] Direction names and destination rooms match the map.
- [ ] Item placement matches the map/storyboard.
- [ ] The start room has no item.
- [ ] The villain room has no item.

## 4. Function Plan

Project Two requires function(s) for commands/status behavior.

| Function | Responsibility | Called from |
| --- | --- | --- |
| TODO | TODO | TODO |
| TODO | TODO | TODO |

Use only as many functions as you need to meet the requirements clearly.

## 5. Gameplay Loop Plan

List the major jobs that happen during one turn of the final game.

1. TODO
2. TODO
3. TODO
4. TODO
5. TODO

What conditions stop the loop?

**Your notes:**

TODO: Identify both required final outcomes.

## 6. Command and Validation Plan

| Command category | Validation question | State change/output |
| --- | --- | --- |
| Movement | TODO | TODO |
| Get item | TODO | TODO |
| Invalid input | TODO | TODO |

Compare these notes with your Project One pseudocode before coding the branches.

## 7. Win and Loss Plan

### Winning

TODO: What state proves the player has collected all required items?

### Losing

TODO: What state proves the player reached the villain too early?

### Ending Checkpoint

- [ ] The milestone `exit` condition is not being used as the final game ending.
- [ ] The final loop can reach both required outcomes.

## 8. Incremental Construction Check

- [ ] Required function(s) run.
- [ ] Dictionary loads without a syntax error.
- [ ] One valid move works.
- [ ] One invalid move is rejected.
- [ ] One valid item can be collected.
- [ ] One invalid item command is handled.
- [ ] Inventory updates correctly.
- [ ] Winning behavior works.
- [ ] Losing behavior works.

## 9. Debugging Notes

| Failing case | Cause found | Change made | Retest result |
| --- | --- | --- | --- |
| TODO | TODO | TODO | TODO |

## 10. Final Submission Check

- [ ] I tested a complete winning path.
- [ ] I tested a complete losing path.
- [ ] I tested invalid movement and item input.
- [ ] I reviewed function/variable names, comments, whitespace, and indentation.
- [ ] I removed unfinished `TODO:` and `pass` placeholders.
- [ ] I saved `text_based_game.py` before submitting it in D2L Brightspace.
