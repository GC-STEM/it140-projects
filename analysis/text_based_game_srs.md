# Software Requirements Specification (SRS)

- **Course**: IT 140 - Introduction to Scripting
- **Activities**: Project One, Module Six Milestone, and Project Two
- **Program**: Text-Based Adventure Game
- **Status**: Provided requirements reference; do not edit

## 0. Purpose and Source Priority

This SRS reorganizes requirements from the three graded activities that use this repository. It does not replace the current Guidelines and Rubric in D2L Brightspace.

If this file and the current activity Guidelines and Rubric differ, follow the **Guidelines and Rubric**.

## 1. Project One | Game Design Requirements

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
- **1.2.2** Include at least **six items**.
- **1.2.3** Place one item in each item-containing room.
- **1.2.4** Use a start room that contains no item.
- **1.2.5** Use a villain room that contains no item.
- **1.2.6** Arrange rooms so the player can collect all required items before entering the villain room.
- **1.2.7** Use movement between rooms in the four supported directions: north, south, east, and west.

### 1.3 Move Pseudocode Requirements

The move pseudocode shall logically describe how the player moves between rooms. It shall address:

- **1.3.1** Player input for a movement command.
- **1.3.2** Validation of the movement input.
- **1.3.3** What happens when the movement command is valid.
- **1.3.4** What happens when the movement command is invalid.
- **1.3.5** Output needed to communicate the result to the player.
- **1.3.6** Decision branching and loops needed to control the process.

### 1.4 Get-Item Pseudocode Requirements

The get-item pseudocode shall logically describe how the player gets the item in the current room and adds it to inventory. It shall address:

- **1.4.1** Player input for an item command.
- **1.4.2** Validation of the requested item.
- **1.4.3** What happens when the requested item is the valid item in the current room.
- **1.4.4** What happens when the requested item is invalid for the current room.
- **1.4.5** Output needed to communicate the result to the player.
- **1.4.6** Decision branching or loops needed to control the process.

### 1.5 Project One File Requirements

Project One graded deliverables are:

- **1.5.1** `game_storyboard.md`
- **1.5.2** `game_map.drawio`
- **1.5.3** `move.pseudo`
- **1.5.4** `get_item.pseudo`

Project One is a design activity. The complete game code is developed later in Project Two.

## 2. Module Six Milestone | Simplified Prototype Requirements

The Module Six Milestone is a working draft of a **simplified** text game. The provided milestone scenario uses a small dragon-themed room dictionary and focuses on movement only.

### 2.1 Provided Prototype Dictionary

The prototype uses the provided three-room dictionary linking:

- Great Hall
- Bedroom
- Cellar

The milestone dictionary represents valid room-to-room movement for the simplified prototype.

### 2.2 Prototype Functional Requirements

The prototype shall:

- **2.2.1** Display the room the player is currently in.
- **2.2.2** Prompt the player to enter a command.
- **2.2.3** Accept valid movement commands that move the player between linked rooms.
- **2.2.4** Accept `exit` as a command that ends the simplified prototype.
- **2.2.5** Reject invalid commands with an error message.
- **2.2.6** Use a gameplay loop so commands continue until the exit condition is reached.
- **2.2.7** Use decision branching to handle movement, exit, and invalid commands.

### 2.3 Prototype Quality Requirements

The milestone code shall:

- **2.3.1** Be debugged so the required movement behavior works.
- **2.3.2** Use comments, whitespace, and appropriate naming conventions to support readability and maintainability.

### 2.4 Milestone File Requirement

The graded Module Six Milestone deliverable is:

- **2.4.1** `move_between_rooms.py`

The milestone does not require the complete item, inventory, villain, or win/loss behavior of Project Two.

## 3. Project Two | Full Game Requirements

Project Two constructs the complete game based on the student's Project One design.

### 3.1 Source File and Organization

The final program shall:

- **3.1.1** Be developed in `text_based_game.py`.
- **3.1.2** Include the student's full name in a comment at the top of the file, as required by the Project Two directions.
- **3.1.3** Use industry-standard comments, whitespace, and appropriate naming conventions.

### 3.2 Functions

The final program shall use one or more functions to organize required behavior, including:

- **3.2.1** Showing the commands the player can enter.
- **3.2.2** Showing player status, including the current room, inventory, and the item in the current room when applicable.

The directions allow this behavior to be organized in separate functions or combined, as long as the required functionality is present.

### 3.3 Main Function and Game Data

The final program shall:

- **3.3.1** Include a `main()` function containing the overall gameplay functionality.
- **3.3.2** Run `main()` when the program is executed.
- **3.3.3** Create a dictionary that links rooms to valid neighboring rooms.
- **3.3.4** Link items to the rooms in which they belong.
- **3.3.5** Use the student's Project One storyboard and map as the source for the full game data.

### 3.4 Gameplay Loop and Commands

The final program shall:

- **3.4.1** Use a gameplay loop.
- **3.4.2** Display the player's status during gameplay.
- **3.4.3** Accept player commands to move between rooms.
- **3.4.4** Accept player commands to get an item from the current room when an item is present.
- **3.4.5** Use decision branching to handle the supported commands.
- **3.4.6** Validate player input and respond appropriately to invalid commands.
- **3.4.7** Update the current room when a valid movement command is entered.
- **3.4.8** Add a valid item to the player's inventory when the required get-item action is completed.

### 3.5 Win and Loss Conditions

The final gameplay loop shall continue until the player wins or loses.

- **3.5.1** The player wins by collecting all required items before encountering the villain.
- **3.5.2** The player loses by entering the villain room before collecting all required items.
- **3.5.3** The program shall display output for both the winning and losing outcomes.
- **3.5.4** The milestone's simplified `exit`-room ending is not the final Project Two ending condition.

### 3.6 Debugging Requirements

The completed game shall be run and debugged to check at least:

- **3.6.1** Valid movement.
- **3.6.2** Invalid movement.
- **3.6.3** Valid item collection.
- **3.6.4** Invalid item commands.
- **3.6.5** Winning behavior.
- **3.6.6** Losing behavior.

## 4. Course-Concept Boundaries

Use concepts taught by the time each activity occurs. The project sequence is intended to bring together course topics such as:

- Input and output
- Variables and strings
- Decision branching
- Loops
- Functions
- Lists
- Dictionaries

The current assignment directions, course content, and instructor guidance determine which techniques are expected.

## 5. Out of Scope Unless Added by Current Course Instructions

Do not treat extra game features as required merely because they are common in commercial games. Examples that are not part of the stated core requirements include:

- Graphical interfaces
- Save/load systems
- Combat systems beyond the required villain outcome
- Multiple player characters
- Network or multiplayer features
- File-based game persistence

Optional enhancements should never replace or break the required behavior.
