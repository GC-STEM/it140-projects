# Software Requirements Specification (SRS)

* **Course**: IT 140 - Introduction to Scripting
- **Activities**: Project One, Module Six Milestone, and Project Two
- **Program**: Text-Based Adventure Game
- **Status**: Provided requirements reference; do not edit

## 0. Purpose and Source Priority

This SRS reorganizes requirements from the three graded activities that use
this repository. It does not replace the current Guidelines and Rubric in D2L
Brightspace.

If this file and current course materials differ, follow this priority:

1. Current activity Guidelines and Rubric
2. Instructor directions
3. Repository guidance

## 1. Project One | Analyze and Design Requirements

Project One is the design checkpoint. The complete game code is developed later
in Project Two.

### 1.1 Theme and Storyboard

The Project One design shall:

- **1.1.1** Describe a game theme.
- **1.1.2** Describe the basic storyline.
- **1.1.3** Identify the rooms used in the game.
- **1.1.4** Identify the items used in the game.
- **1.1.5** Identify the villain.

### 1.2 Map Requirements

The game map shall:

- **1.2.1** Include at least **eight rooms**.
- **1.2.2** Include at least **six items** when using the minimum eight-room design.
- **1.2.3** Place **one item in every room except the start room and villain room**.
- **1.2.4** Use a start room that contains no item.
- **1.2.5** Use a villain room that contains no item.
- **1.2.6** Allow the player to collect all required items before entering the
  villain room.
- **1.2.7** Represent movement using north, south, east, and west.

### 1.3 Move Pseudocode Requirements

The move pseudocode shall logically describe how the player moves between
rooms. It shall address:

- **1.3.1** Player input for a movement command.
- **1.3.2** Validation of the movement input.
- **1.3.3** Behavior after a valid movement command.
- **1.3.4** Behavior after an invalid movement command.
- **1.3.5** Output that communicates the result.
- **1.3.6** Decision branching and loops used to control the process.

### 1.4 Get-Item Pseudocode Requirements

The get-item pseudocode shall logically describe how the player gets the item
in the current room and adds it to inventory. It shall address:

- **1.4.1** Player input for an item command.
- **1.4.2** Validation of the requested item.
- **1.4.3** Behavior when the requested item is valid for the current room.
- **1.4.4** Behavior when the requested item is invalid for the current room.
- **1.4.5** Output that communicates the result.
- **1.4.6** Decision branching or loops used to control the process.

### 1.5 Project One Graded Files

Project One requires these four submissions:

- **1.5.1** `design/game_storyboard.md`
- **1.5.2** `design/game_map.drawio`
- **1.5.3** `design/move.pseudo`
- **1.5.4** `design/get_item.pseudo`

### 1.6 Project One Rubric Traceability

The Project One rubric evaluates:

- Storyboard: Theme and Map — **20%**
- Pseudocode: Logical Steps and Functionality — **30%**
- Pseudocode: Input / Output — **20%**
- Pseudocode: Program Flow — **25%**
- Clear Communication — **5%**

## 2. Module Six Milestone | Construct and Test a Reduced Prototype

The milestone is a working draft of a **simplified** text game. It intentionally
uses provided sample data and focuses on movement only.

### 2.1 Provided Prototype Dictionary

The milestone uses the course-provided three-room dictionary linking:

- Great Hall
- Bedroom
- Cellar

This dictionary is milestone sample data. It is not the student's final Project
Two world.

### 2.2 Prototype Functional Requirements

The prototype shall:

- **2.2.1** Display the room the player is currently in.
- **2.2.2** Prompt the player to enter a command.
- **2.2.3** Move the player after a valid movement command.
- **2.2.4** Accept `exit` and use the required exit condition to end the
  simplified prototype.
- **2.2.5** Reject invalid commands with an error message.
- **2.2.6** Use a gameplay loop until the exit condition is reached.
- **2.2.7** Use decision branching for movement, exit, and invalid commands.

### 2.3 Prototype Quality Requirements

The milestone code shall:

- **2.3.1** Be debugged so the required movement behavior works.
- **2.3.2** Use comments, whitespace, and appropriate naming conventions to
  support readability and maintainability.

### 2.4 Milestone Graded File

The Module Six Milestone requires:

- **2.4.1** `prototype/move_between_rooms.py`

The milestone does not require items, inventory, a villain, or Project Two
win/loss behavior.

### 2.5 Milestone Rubric Traceability

The Module Six Milestone rubric evaluates:

- Functionality — **30%**
- Gameplay Loop — **10%**
- Decision Branching — **20%**
- Input Validation — **20%**
- Debugging — **10%**
- Industry Standard Best Practices — **10%**

## 3. Project Two | Construct and Test the Complete Game

Project Two constructs the complete game from the student's Project One design.
The Module Six prototype is a useful implementation exercise, but its sample
world and `exit` ending are not the final system requirements.

### 3.1 Source File and Organization

The final program shall:

- **3.1.1** Be developed in `src/text_based_game.py`.
- **3.1.2** Include the student's full name in a comment at the top of the file,
  as required by the Project Two directions.
- **3.1.3** Use comments, whitespace, and appropriate naming conventions.

### 3.2 Functions

The final program shall use one or more functions to organize required behavior,
including:

- **3.2.1** Showing the commands the player can enter.
- **3.2.2** Showing player status, including current room, inventory, and the
  item in the current room when applicable.

The activity allows this behavior to be separated into multiple functions or
combined as long as the required functionality is present.

### 3.3 Main Function and Game Data

The final program shall:

- **3.3.1** Include a `main()` function containing the overall gameplay.
- **3.3.2** Run `main()` when the program is executed.
- **3.3.3** Create a dictionary linking rooms to valid neighboring rooms.
- **3.3.4** Link items to the rooms in which they belong.
- **3.3.5** Use the student's Project One storyboard and map as the source for
  the full game data.

### 3.4 Gameplay Loop and Commands

The final program shall:

- **3.4.1** Use a gameplay loop.
- **3.4.2** Display the player's status during gameplay.
- **3.4.3** Accept movement commands.
- **3.4.4** Accept get-item commands when an item is present.
- **3.4.5** Use function calls as required by the student's chosen organization.
- **3.4.6** Use decision branching to handle supported commands.
- **3.4.7** Validate player input and respond appropriately to invalid commands.
- **3.4.8** Update the current room after a valid movement command.
- **3.4.9** Add a valid item to inventory after the required get-item action.

### 3.5 Win and Loss Conditions

The final gameplay loop shall continue until the player wins or loses.

- **3.5.1** The player wins by collecting all required items before encountering
  the villain.
- **3.5.2** The player loses by entering the villain room before collecting all
  required items.
- **3.5.3** The program shall display output for winning and losing outcomes.
- **3.5.4** The milestone's `exit` ending shall not replace the final win/loss
  conditions.

### 3.6 Debugging Requirements

The completed game shall be tested and debugged for at least:

- **3.6.1** Valid movement.
- **3.6.2** Invalid movement.
- **3.6.3** Valid item collection.
- **3.6.4** Invalid item commands.
- **3.6.5** Winning behavior.
- **3.6.6** Losing behavior.

### 3.7 Project Two Rubric Traceability

The Project Two rubric evaluates:

- Functions — **10%**
- Main Function: Dictionary — **10%**
- Main Function: Gameplay Loop — **15%**
- Main Function: Function Calls — **5%**
- Main Function: Decision Branching — **20%**
- Input Validation — **20%**
- Debugging — **10%**
- Industry Standard Best Practices — **10%**

## 4. Cross-Module Handoff Requirements

| Earlier artifact | Later use |
| --- | --- |
| Project One storyboard | Defines the student's final theme, rooms, items, and villain |
| Project One map | Defines room connections and item placement for the final dictionary |
| Project One move pseudocode | Guides movement logic in the milestone and final game |
| Project One get-item pseudocode | Guides item/inventory logic in Project Two |
| Module Six prototype | Provides movement/dictionary/loop practice and feedback for Project Two |
| Module Six instructor feedback | Identifies corrections to consider before final integration |

The later checkpoint may require revisions based on instructor feedback, but
sample milestone data should not overwrite the student's approved Project One
design.

## 5. Out of Scope Unless Added by Current Course Instructions

Do not treat extra commercial-game features as required merely because they are
common elsewhere. Core requirements do not state a need for:

- Graphical interfaces
- Save/load systems
- Multiplayer/network features
- File-based persistence
- Combat systems beyond the required villain outcome

Optional enhancements should never replace or break required behavior.
