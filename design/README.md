# Design Phase | Module Five Project One

**Project sequence:** [Start Here](../README.md) →
[M5 Analyze](../analysis/README.md) → **M5 Design** →
[M6 Construct/Test Prototype](../prototype/README.md) →
[M7 Construct](../src/README.md) → [M7 Test](../tests/README.md)

## Purpose

Project One completes the **Design checkpoint** for the three-module project.
You are planning the complete game before writing its final Python code.

The design you submit in Module Five becomes an input to Project Two in Module
Seven. Treat these artifacts as the design record for your own game, not as
one-time files to discard after grading.

## Graded Deliverables

Complete all four Project One files:

| File | What it defines | Used again later |
| --- | --- | --- |
| [`game_storyboard.md`](game_storyboard.md) | Theme, storyline, rooms, items, villain | M7 final game data and output context |
| [`game_map.drawio`](game_map.drawio) | Room layout, directional relationships, item placement | M7 room/item dictionary and test paths |
| [`move.pseudo`](move.pseudo) | Movement input, validation, room update, output, flow | M6 prototype and M7 movement logic |
| [`get_item.pseudo`](get_item.pseudo) | Get-item input, validation, inventory update, output, flow | M7 item/inventory logic |

The [Software Design Document (SDD)](text_based_game_sdd.md) is a
course-provided reference. It explains design relationships without supplying a
completed game solution.

## Course-Provided Flowchart References

The Project One directions ask you to create pseudocode based on provided
flowcharts. This repository includes reference images for those processes:

- [`move.drawio.png`](move.drawio.png) — move-between-rooms reference
- [`get_item.drawio.png`](get_item.drawio.png) — get-item reference

Use the flowcharts to understand required process structure. Do not copy a
sample game world in place of your own theme, rooms, items, or villain.

## 1. Complete the Storyboard

Open [`game_storyboard.md`](game_storyboard.md).

Describe:

- Your theme
- The basic storyline
- At least eight rooms
- At least six items for the minimum eight-room design
- Your villain

Use names you can keep consistent across the map and final game.

## 2. Create the Game Map

Open [`game_map.drawio`](game_map.drawio) in VS Code using the Draw.io
integration.

The current Project One requirements include:

- At least eight rooms
- At least six items for the minimum eight-room design
- No item in the start room
- No item in the villain room
- One item in every room except the start room and villain room
- A layout that lets the player collect all required items before entering the
  villain room
- Directional relationships that support north, south, east, and west movement

Before continuing, trace at least one complete **winning route** through your
map. If the villain blocks access to a required item, revise the design.

## 3. Write Move Pseudocode

Open [`move.pseudo`](move.pseudo) beside the provided movement flowchart.

Your pseudocode needs to make clear:

- What movement input is requested
- How that input is validated for the current room
- What happens after a valid direction
- What happens after an invalid direction
- What output is produced
- How decision branching and repetition control the process

This pseudocode is later useful twice: first as conceptual support for the M6
movement prototype, and then as part of the final M7 game design.

## 4. Write Get-Item Pseudocode

Open [`get_item.pseudo`](get_item.pseudo) beside the provided get-item
flowchart.

Your pseudocode needs to make clear:

- What item input is requested
- How the request is validated for the current room
- How a valid item is added to inventory
- What happens after an invalid item request
- What output is produced
- How branching or repetition controls the process

The milestone does **not** implement this process. It carries forward directly
to Project Two.

## 5. Review Against the Project One Rubric

| Rubric criterion | Weight | Design evidence |
| --- | ---: | --- |
| Storyboard: Theme and Map | 20% | Storyboard + game map |
| Pseudocode: Logical Steps and Functionality | 30% | Move + get-item pseudocode |
| Pseudocode: Input / Output | 20% | Inputs, prompts, results, feedback |
| Pseudocode: Program Flow | 25% | Branching, loops, and all required paths |
| Clear Communication | 5% | Organized, understandable design artifacts |

The rubric evaluates the submitted design, not whether you already wrote the
final Python game.

## 6. Design Consistency and Handoff Check

Before submitting Project One:

- [ ] Storyboard and map use the same room names.
- [ ] Storyboard and map use the same item names.
- [ ] The villain is placed consistently.
- [ ] The start room and villain room contain no items.
- [ ] The map is winnable.
- [ ] Move pseudocode can work with the map's directional relationships.
- [ ] Get-item pseudocode matches the required item/inventory behavior.
- [ ] I can explain how these artifacts will become inputs to Project Two.

## Project One Submission Checkpoint

Submit these four files in D2L Brightspace according to the current What to
Submit instructions:

- `game_storyboard.md`
- `game_map.drawio`
- `move.pseudo`
- `get_item.pseudo`

## Next Step

After Project One is graded, keep the same repository and review instructor
feedback. In Module Six, continue to the
[Prototype instructions](../prototype/README.md).

Do not replace your Project One design with the milestone's small sample world.
