# Test Phase | Module Six and Module Seven

**Project progress:** [Start Here](../README.md) → [1 Analyze](../analysis/README.md) → [2 Design | M5](../design/README.md) → [3 Prototype | M6](../prototype/README.md) → [4 Construct | M7](../src/README.md) → **5 Test**

## Purpose

Testing checks whether the program behaves the way the current requirements and your design say it should.

The project allows students to create different themes, maps, room names, item names, and output wording. Because of that variation, the most useful project testing is **requirement-based manual testing** using your own game map and known paths.

The file [`game_test_plan.md`](game_test_plan.md) is a recommended place to record tests. It is not a graded deliverable unless your instructor tells you otherwise.

## Module Six Prototype Tests

Run:

```bash
python3 prototype/move_between_rooms.py
```

Check at least:

- A valid move from each room where possible
- An invalid direction from a room
- An invalid non-movement command
- The `exit` command
- The loop ending at the required exit condition

When a test fails:

1. Repeat the exact command that failed.
2. Identify the current room before the command.
3. Compare the expected behavior with the milestone requirements.
4. Find the first branch or update where the program differs.
5. Make one small correction.
6. Run the same test again.

## Project Two Manual Test Strategy

Use your Project One map to plan tests before randomly exploring the game.

### 1. Movement

Test:

- [ ] At least one valid move in each supported direction that exists on your map.
- [ ] An invalid direction from a room where that direction is not connected.
- [ ] Room updates after valid movement.
- [ ] No unintended room update after invalid movement.

### 2. Items and Inventory

Test:

- [ ] A valid get-item command in a room containing an item.
- [ ] The collected item appears in inventory.
- [ ] An invalid item name.
- [ ] A get-item command in a room without an available item, if your command design permits that input.
- [ ] The same room does not incorrectly provide the same item again after it has been collected.

### 3. Game Endings

Test both complete outcomes:

- [ ] **Winning path:** collect all required items before entering the villain room.
- [ ] **Losing path:** enter the villain room before collecting all required items.

Do not treat one successful playthrough as enough evidence that every branch works.

### 4. Readability and Maintenance

Before final submission, also review the code without running it:

- [ ] Function and variable names are understandable.
- [ ] Indentation is consistent.
- [ ] Comments explain useful intent rather than restating every line.
- [ ] Extra unused code has been removed.
- [ ] The final file does not still contain unfinished `TODO:` placeholders.

## Debug One Problem at a Time

When a test fails, avoid changing several unrelated sections at once.

A good debugging cycle is:

> **Reproduce → Locate → Change one thing → Test again**

If coding reveals that your Project One design was inconsistent, update your design notes so your repository still tells one coherent story from design to implementation.

## Final Project Two Check

When all required tests pass, return to the top-level [Module Seven | Project Two](../README.md#module-seven--project-two) submission section.
