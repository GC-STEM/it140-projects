# Test | Module Six and Module Seven

**Project sequence:** [Start Here](../README.md) →
[M5 Analyze](../analysis/README.md) → [M5 Design](../design/README.md) →
[M6 Construct/Test Prototype](../prototype/README.md) →
[M7 Construct](../src/README.md) → **M7 Test**

## Purpose

Testing occurs twice in this three-module SDLC:

- **Module Six:** test the reduced movement prototype.
- **Module Seven:** test the complete game against the student's Project One
  design and Project Two requirements.

Student game worlds differ, so the most useful final-game testing is
**requirement-based manual testing** using the student's own map and known
playthrough paths.

[`game_test_plan.md`](game_test_plan.md) is optional working space. It is not a
graded deliverable unless your instructor specifically asks for it.

# Module Six | Test the Movement Prototype

Run the milestone from the repository root. **Windows users must use Git Bash**
for this `bash` command block.

<!-- ci:command-test id=test-run-module-six fixture=existing-repo expect=repo -->
```bash
cd ~/Repos/it140-projects
python3 prototype/move_between_rooms.py
```

Test the milestone's reduced scope:

- [ ] Valid movement from the Great Hall
- [ ] Valid movement from the Bedroom
- [ ] Valid movement from the Cellar when applicable
- [ ] Invalid direction from a room
- [ ] Invalid non-movement command
- [ ] `exit`
- [ ] Loop ends at the required exit condition

## Debugging Cycle

When a case fails:

1. Reproduce the exact command sequence.
2. Record the current room before the failing command.
3. Compare actual behavior with the milestone requirement.
4. Locate the first incorrect decision or state update.
5. Change one thing.
6. Rerun the same case.

# Module Seven | Test the Complete Game

Use your Project One map to plan tests. A map gives you known routes for
specific movement, item, winning, and losing cases.

## 1. Movement and Input Validation

Test:

- [ ] Valid movement in each direction represented by your map
- [ ] Invalid direction from a room
- [ ] Invalid command format/value required by your command design
- [ ] Current room changes only after a valid move

## 2. Items and Inventory

Test:

- [ ] Valid get-item command in a room containing an item
- [ ] Collected item appears in inventory
- [ ] Invalid item name/request
- [ ] Get-item behavior in a room without an available item
- [ ] A collected room does not incorrectly provide the same item again

## 3. Function and Status Behavior

Test that required function calls produce the needed player information:

- [ ] Available commands are communicated
- [ ] Current room is shown
- [ ] Inventory is shown
- [ ] Current-room item is shown when applicable

## 4. Complete Endings

Run both full outcomes:

- [ ] **Winning path:** collect all required items before entering the villain
  room.
- [ ] **Losing path:** enter the villain room before all required items have
  been collected.

A single successful playthrough is not enough evidence that all branches work.

## 5. Static Readability Review

Before final submission, review the file without running it:

- [ ] Function and variable names are understandable.
- [ ] Indentation is consistent.
- [ ] Comments add useful context.
- [ ] Whitespace supports readability.
- [ ] Unused/dead starter code is removed.
- [ ] No unfinished `TODO:` or `pass` placeholders remain.

## Final Project Two Check

When the required cases pass, return to
[Module Seven | Project Two](../README.md#module-seven--project-two) in the
root README and follow the current D2L submission instructions.
