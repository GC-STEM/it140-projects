# Software Development Worksheet (SDW)

- **Course**: IT 140 - Introduction to Scripting
- **Activities**: Project One, Module Six Milestone, and Project Two
- **Program**: Text-Based Adventure Game
- **Purpose**: Optional working notes across the three-module project sequence

> [!NOTE]
> This worksheet is a learning aid. It is **not a graded deliverable** unless your instructor specifically asks for it. Keep notes brief. The graded work belongs in the Project One design files, the Module Six prototype file, and the Project Two source file.

## Project Progress

> **Analyze → Design → Prototype → Construct → Test**

---

## 1. Analyze | Module Five

Use the Project One Guidelines and Rubric and [`../analysis/text_based_game_srs.md`](../analysis/text_based_game_srs.md).

### 1.1 Game Goal in Your Own Words

TODO: In one or two sentences, explain what the player must do to win and what causes the player to lose.

### 1.2 Required World Elements

| Element | Your notes |
| --- | --- |
| Theme | TODO |
| Storyline | TODO |
| Start room | TODO |
| Villain | TODO |
| Minimum room count | TODO |
| Minimum item count | TODO |

### 1.3 Command Types

TODO: Describe the two command types required by the project without writing Python code.

### Analyze Checkpoint

- [ ] I understand the minimum room and item requirements.
- [ ] I know which rooms cannot contain items.
- [ ] I understand what makes the map winnable.
- [ ] I understand the movement action.
- [ ] I understand the get-item action.

---

## 2. Design | Project One

### 2.1 Map Planning Notes

TODO: List room names and rough directional relationships before or while editing the Draw.io map.

### 2.2 Item Placement Notes

TODO: Record which item belongs in which room. Do not put an item in the start room or villain room.

### 2.3 Pseudocode Consistency Notes

- [ ] Move pseudocode matches the map's directional connections.
- [ ] Get-item pseudocode matches the item behavior required by the project.
- [ ] Names are consistent across the storyboard and map.

### Project One Submission Check

- [ ] `game_storyboard.md` complete
- [ ] `game_map.drawio` complete
- [ ] `move.pseudo` complete
- [ ] `get_item.pseudo` complete
- [ ] Submitted through D2L Brightspace as directed

---

## 3. Prototype | Module Six Milestone

### 3.1 Design-to-Code Notes

What Python concepts did you use to implement the simplified movement prototype?

| Need | Python concept you used |
| --- | --- |
| Store room connections | TODO |
| Repeat gameplay | TODO |
| Choose command behavior | TODO |
| Validate input | TODO |
| Update current room | TODO |

### 3.2 Milestone Debugging Notes

TODO: Record one problem you found while testing and how you fixed it, or write `No changes needed`.

### Milestone Submission Check

- [ ] `prototype/move_between_rooms.py` meets the current milestone requirements.
- [ ] I tested valid movement, invalid input, and exit.
- [ ] I reviewed readability and naming.
- [ ] I submitted the required `.py` file through D2L Brightspace.

---

## 4. Construct | Project Two

### 4.1 Design Handoff

Before coding the full game:

- [ ] I reviewed instructor feedback from Project One.
- [ ] I reviewed instructor feedback from the Module Six milestone.
- [ ] My storyboard and map still agree.
- [ ] My pseudocode reflects the behavior I intend to code.

### 4.2 Full Game Data Notes

TODO: Record anything you need to check while turning your map into the final room/item dictionary.

### 4.3 Function Plan

TODO: Identify the function or functions you plan to use for instructions/status. Keep the plan simple and within Project Two requirements.

### 4.4 Gameplay Loop Plan

TODO: In words, list the major jobs one turn of the final gameplay loop must perform.

---

## 5. Test | Project Two

Use [`../tests/game_test_plan.md`](../tests/game_test_plan.md) for detailed test records.

### Final SDLC Check

- [ ] Analyze: I understand the project requirements.
- [ ] Design: My Project One artifacts form a consistent game design.
- [ ] Prototype: I completed and tested the Module Six movement prototype.
- [ ] Construct: My Project Two code follows my own design.
- [ ] Test: I tested movement, item behavior, winning, and losing.
- [ ] Submit: I followed the current D2L What to Submit instructions for all three graded checkpoints.
