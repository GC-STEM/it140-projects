# Software Design Document

- **Course**: IT 140 - Introduction to Scripting
- **Activities**: Project One, Module Six Milestone, and Project Two
- **Program**: Text-Based Adventure Game
- **Status**: Course-provided design reference; do not edit

## 0. Purpose

This SDD explains how the Project One design artifacts relate to later
construction without supplying a completed solution.

The project does not complete every SDLC activity in one week. The design is
created in Module Five, a reduced portion is prototyped and tested in Module
Six, and the complete design is implemented and tested in Module Seven.

## 1. Student Design Artifacts

The student's Project One design consists of:

- `game_storyboard.md`
- `game_map.drawio`
- `move.pseudo`
- `get_item.pseudo`

These four files should describe one coherent game.

## 2. High-Level Game Model

The final system coordinates:

- **World state** — room connections and item placement
- **Player location** — current room
- **Inventory** — collected items
- **Input** — movement and get-item commands
- **Validation** — whether a command is valid in the current state
- **Decision branching** — what happens for each command/result
- **Repetition** — turns continue until the game ends
- **Output** — instructions, status, command results, and final outcomes

Project One designs the important parts of this model. Project Two later
combines them into one Python program.

## 3. Storyboard-to-Map Relationship

The storyboard defines names and narrative intent. The map gives those choices
spatial relationships.

Before submission, verify that:

- Room names match.
- Item names match.
- The villain location matches.
- The start room and villain room contain no items.
- The map permits a winning route.

## 4. Map-to-Dictionary Handoff

In Project Two, the map becomes the main source for the final room/item
dictionary.

For each room, the programmer will need to determine:

- Which directions lead to neighboring rooms
- The destination room for each valid direction
- The item associated with the room, when applicable

Project One does not require writing the final dictionary yet.

## 5. Move Process Design

The movement design needs to account for:

- Current room
- Movement command
- Whether the requested direction is valid from that room
- Current-room update after a valid move
- Feedback after valid or invalid input
- Repetition as gameplay continues

The Module Six milestone implements a reduced version of this idea using a
provided three-room dictionary. The final implementation returns to the
student's own map.

## 6. Get-Item Process Design

The get-item design needs to account for:

- Current room
- Item in that room, when present
- Player's item request
- Validation of the requested item
- Inventory update after a valid request
- Feedback after valid or invalid input

The Module Six milestone intentionally does not implement this process. It is
carried from Project One directly into Project Two.

## 7. Module Six Prototype Handoff

The milestone is a reduced construction/testing iteration. It practices:

- Translating movement design into Python
- Reading a room dictionary
- Writing a gameplay loop
- Using decision branching
- Validating commands
- Debugging one behavior at a time

The milestone uses sample dragon-game data and an `exit` ending. Those are
prototype constraints, not changes to the final design.

## 8. Project Two Integration Handoff

Before coding Project Two, reconcile:

1. Project One design artifacts
2. Project One instructor feedback
3. Module Six prototype code
4. Module Six instructor feedback
5. Current Project Two requirements

Reuse useful programming patterns from the milestone, but build the final room
and item data from the student's own Project One design.

## 9. Requirements Traceability

| Requirement/design concern | M5 design evidence | M6 evidence | M7 evidence |
| --- | --- | --- | --- |
| Theme, rooms, items, villain | Storyboard + map | Not in reduced prototype | Final dictionary/output |
| Room movement | Map + move pseudocode | Movement code | Final movement branch |
| Get item/inventory | Get-item pseudocode | Not in reduced prototype | Final item branch + inventory |
| Repetition | Pseudocode | Prototype loop | Final gameplay loop |
| Input validation | Pseudocode | Movement/exit validation | Movement + item validation |
| Ending behavior | Winnable design | Prototype `exit` only | Required win/loss behavior |
| Testing/debugging | Design trace | Prototype tests | Winning/losing and command tests |

The artifacts should tell one coherent story from requirement to design to
implementation to test evidence.
