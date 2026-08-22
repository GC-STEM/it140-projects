# Design Phase | Module Five Project One

**Project progress:** [Start Here](../README.md) → [1 Analyze](../analysis/README.md) → **2 Design | M5** → [3 Prototype | M6](../prototype/README.md) → [4 Construct | M7](../src/README.md) → [5 Test](../tests/README.md)

## Purpose

The Design phase is the focus of **Project One**. You will plan the complete text-based adventure game before writing the final game code.

Project One has four graded deliverables:

1. A storyboard
2. A world map
3. Move-between-rooms pseudocode
4. Get-item pseudocode

These artifacts become the design you use again in Module Six and Project Two.

## Graded Deliverables

Complete all four files in this folder:

- [`game_storyboard.md`](game_storyboard.md)
- [`game_map.drawio`](game_map.drawio)
- [`move.pseudo`](move.pseudo)
- [`get_item.pseudo`](get_item.pseudo)

The [Software Design Document (SDD)](text_based_game_sdd.md) is a course-provided design reference. The [SDW](../src/text_based_game_sdw.md) is optional working space.

> [!NOTE]
> The current Project One directions tell you to create the move and get-item **pseudocode based on course-provided flowcharts**. Those flowcharts are design references rather than student-created Project One submission files. If your course or repository provides the flowchart files, use them as directed and leave the provided originals unchanged.

## Before You Design

Make sure you have:

1. Read the Project One Guidelines and Rubric.
2. Completed the [Analyze Phase](../analysis/README.md).
3. Reviewed the [SRS](../analysis/text_based_game_srs.md).
4. Identified the required rooms, items, start room, villain, and gameplay goal.

## 1. Complete the Storyboard

Open [`game_storyboard.md`](game_storyboard.md) and complete the `TODO:` prompts in your own words.

Your storyboard must identify:

- The theme
- The basic storyline
- The rooms
- The items
- The villain

Keep the storyboard consistent with your map. Names used in one artifact should match the names you use in the others.

## 2. Create the Game Map

Open [`game_map.drawio`](game_map.drawio) in VS Code using the Draw.io integration.

Your map must follow the current Project One requirements, including:

- At least eight rooms
- At least six items
- No item in the start room
- No item in the villain room
- A layout that allows the player to collect all required items before entering the villain room
- Connections that make movement using north, south, east, and west understandable

Use the map as a design tool. The final player does not need to see this map while playing the text game.

> [!TIP]
> Before moving on, trace at least one complete winning route through your map. If the villain blocks access to a required item, revise the map.

## 3. Write Move Pseudocode

Open [`move.pseudo`](move.pseudo).

Use the provided prompts to describe, step by step:

- How the player enters a movement command
- How the program decides whether the move is valid
- How the current room changes after a valid move
- What the player sees after a valid or invalid move
- Where decision branching and repetition are needed

Do not write the final Python code here. Pseudocode should describe the logic in clear steps.

## 4. Write Get-Item Pseudocode

Open [`get_item.pseudo`](get_item.pseudo).

Describe:

- How the player enters a get-item command
- How the program checks whether the requested item is in the current room
- How a valid item is added to inventory
- What happens after an invalid item request
- What output the player receives

## 5. Compare the Design Artifacts

Before submitting Project One, compare all four files.

Check that:

- [ ] Room names match between the storyboard and map.
- [ ] Item names match between the storyboard and map.
- [ ] The villain is placed in the same room everywhere.
- [ ] The start room contains no item.
- [ ] The villain room contains no item.
- [ ] The map is winnable.
- [ ] Move pseudocode matches how rooms connect on the map.
- [ ] Get-item pseudocode matches the item behavior described by the project.

## Project One Submission Checkpoint

When all four design files meet the current Project One Guidelines and Rubric, return to [Module Five | Project One](../README.md#module-five--project-one) in the top-level README and submit the required files in D2L Brightspace.

## Next Step

After Project One is complete, keep this same repository. In Module Six, continue to the [Prototype Phase](../prototype/README.md).
