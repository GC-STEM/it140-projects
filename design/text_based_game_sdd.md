# Software Design Document (SDD)

- **Course**: IT 140 - Introduction to Scripting
- **Activities**: Project One, Module Six Milestone, and Project Two
- **Program**: Text-Based Adventure Game
- **Status**: Design reference; do not edit

## 0. Purpose

This SDD helps organize the project design without supplying a completed game solution. Your own design decisions belong in:

- `game_storyboard.md`
- `game_map.drawio`
- `move.pseudo`
- `get_item.pseudo`

The current Project One Guidelines and Rubric remains the official source for the graded design requirements.

## 1. Design Inputs

Use these sources while designing:

1. Project One Guidelines and Rubric
2. [`../analysis/text_based_game_srs.md`](../analysis/text_based_game_srs.md)
3. Your optional [`../src/text_based_game_sdw.md`](../src/text_based_game_sdw.md) notes
4. Course-provided sample game resources identified in the Project One activity

Sample materials demonstrate the type of game behavior expected. They do not determine your game's theme, rooms, items, villain, or map.

## 2. High-Level Game Model

The completed game needs to coordinate several kinds of state and behavior:

- **World state** — which rooms connect to which other rooms and which item belongs in each item room
- **Player location** — the room the player is currently in
- **Inventory** — the items the player has collected
- **Input** — movement and get-item commands
- **Validation** — whether a requested move or item is valid in the current state
- **Game progression** — repeated turns until the player wins or loses
- **Output** — instructions, player status, results of commands, and final outcome

Project One designs the important pieces of this model. Project Two later combines them into one working program.

## 3. Map Design Constraints

The map should make direction relationships clear.

When two rooms are connected, ask:

- Which direction moves from Room A to Room B?
- What direction should move from Room B back to Room A, if the map allows that return path?
- Does the arrangement leave a path to every required item before the villain must be encountered?

The design should be understandable without requiring the final Python dictionary to be written in Project One.

## 4. Move Process Design

The move pseudocode should represent a reusable movement process rather than one hard-coded path through the map.

The process needs to account for:

- The current room
- A movement command
- Whether the requested direction is available from the current room
- Updating the current room after a valid move
- Responding to invalid movement input
- Repetition as gameplay continues

Choose the detailed logic yourself in `move.pseudo`.

## 5. Get-Item Process Design

The get-item pseudocode should account for:

- The current room
- The item associated with that room, when present
- The player's item request
- Validation of the requested item
- Adding a valid item to inventory
- Preventing an invalid item request from behaving as though it succeeded

Choose the detailed logic yourself in `get_item.pseudo`.

## 6. Handoff to the Module Six Prototype

The Module Six Milestone does not construct the full design. Instead, it gives you a smaller movement-only implementation exercise using a provided three-room dictionary.

Use the milestone to practice:

- Translating movement logic into Python
- Working with a dictionary of room connections
- Writing a gameplay loop
- Validating commands
- Debugging one behavior at a time

Do not change your Project One design merely to match the simplified milestone scenario.

## 7. Handoff to Project Two

Project Two combines your own Project One design with later course concepts such as functions, lists, and dictionaries.

Before coding the final game, compare your four Project One artifacts and resolve inconsistencies. The final room dictionary, item associations, and command logic should reflect your own approved design.

## 8. Design Consistency Review

| Design question | Storyboard | Map | Move pseudocode | Get-item pseudocode |
| --- | :---: | :---: | :---: | :---: |
| Theme and names are consistent | Check | Check | — | — |
| Room names are consistent | Check | Check | Check as needed | Check as needed |
| Item names are consistent | Check | Check | — | Check |
| Villain location is consistent | Check | Check | — | — |
| Movement relationships are possible | — | Check | Check | — |
| Item behavior matches the scenario | Check | Check | — | Check |

If the artifacts disagree, revise them before using them as the plan for Project Two.
