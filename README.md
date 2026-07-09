# IT 140 Projects: Text Adventure Game

<!-- To see this file in a clean, formatted view, right-click on the filename and choose “Open Preview.” -->

- **Course**: IT 140 - *Introduction to Scripting*
- **Activities**:
  - 5-3: Project One Submission
  - 6-4: Milestone: Moving Between Rooms
  - 7-3: Project Two Submission
- **Program Name**: `text_based_game`

> [!WARNING]
> This repository is incomplete and under active development. Code, documentation, structure, and features may change frequently. Check back for updates.
> This repository is primarily to hold coding-related course materials for import into Codio. It is not intended for direct faculty or student use unless approved for that purpose.

To complete this activity, follow the Software Development Life Cycle (SDLC). The top-level steps are listed below. See the [To-Do List](./text_based_game_todo.md) for detailed, step-by-step instructions.

## Getting Started

1. **Analyze** the [problem and requirements](./analysis/text_based_game_srs.md) to understand what needs to be done. Record your understanding of the problem and requirements in your [SDW worksheet](./analysis/text_based_game_sdw.md).

2. **Design** a solution that meets specification. Review the [Software Design Document](./design/text_based_game_sdd.md), {{along with its | and create a}} [flowchart](./design/text_based_game.drawio) and low-level [pseudocode](./design/text_based_game.pseudo).

3. **Construct** a working program in [`text_based_game.py`](./src/text_based_game.py) that implements the designed solution.

4. **Test** the program to ensure it works correctly and meets the requirements. Debug any issues that arise during testing. Test again until all issues are resolved.

5. **Submit** activity deliverables for grading and feedback. See the activity Guidelines and Rubric for what to submit and how your work will be evaluated.

## Supporting Materials

The following resources may help support your work on the project:

### Activity Repository

The activity repository is organized to match the courseSoftware Development Life Cycle (SDLC). This structure will help you organize your work and ensure that you are following the SDLC process effectively. Each folder contains specific files related to that phase of the SDLC, as outlined below:

```text
it140_projects/
│
├── analysis/                    # 1. Analysis: understand the problem
│   ├── text_based_game_sdw.md   # Software Development Worksheet (SDW) to plan your work
│   └── text_based_game_srs.md   # Software Requirements Specification (SRS)
│
├── design/                      # 2. Design: plan the solution
│   ├── text_based_game_sdd.md   # Software Design Document (SDD)
│   ├── text_based_game.drawio   # Flowchart: visual outline of project logic
│   └── text_based_game.pseudo   # Pseudocode: step-by-step logic before coding
│
├── src/                         # 3. Construction: write the code
│   ├── move_between_rooms.py    # M6: moving between rooms (src) code file
│   └── text_based_game.py       # P2: Python source (src) code file
│
├── tests/                           # 4. Test: check that code meets requirements
│   ├── test_move_between_rooms.py   # M6: Test moving between rooms code file
│   └── test_text_based_game.py      # Automated integration tests
│
├── text_based_game_todo.md      # Step-by-step directions for this activity
└── README.md                    # Start here: activity overview
```

*Note*. This repository may include additional files not listed in the main repository structure. These folders and files are essential for maintaining a well-organized and high-quality codebase, but they are not part of the Software Development Life Cycle (SDLC) and are not meant to be modified by students. Just ignore these as you work on the activity, and focus on the main repository files listed above.

## Activity Development Environment

| # | **Software Purpose**   | **Software Name**        |
|:-:| ---------------------- | ------------------------ |
| 1 | Version Control        | Git & GitHub CLI         |
| 2 | Programming Language   | PL Runtime               |
| 3 | Code Editor or IDE     | Visual Studio Code       |
|---| **CE/IDE Extensions**  | ------------------------ |
| 4 | Language Support       | {{PL Extension}}         |
| 5 | Code Linter/Formatter  | {{L/F Extension}}        |
| 6 | Diagram Support        | hediet.vscode-drawio     |
| 7 | Pseudocode Support     | i2p-hub.i2p-pseudo       |
| 8 | Code Spell Checker     | streetsidesoftware.code-spell-checker |
| 9 | Dependencies           | See {{requirements.txt}} |

### Additional Resources

- [Kaggle Notebook]({{Add link or delete}})
- [YouTube Video]({{Add link or delete}})
- [Zotero Collection]({{Add link or delete}})
