<!-- To see this file in a clean, formatted view, select ▼ in the upper-right corner of the editor pane, then select "Markdown Preview". -->

# IT 140 Projects | Modules Five–Seven | Text-Based Game Projects

---

> [!IMPORTANT]
> **GitHub repository options**
>
> **Do not select Fork or Use this template.** These options will interfere with the repository setup commands later in this README.
>
> * 🚫 **Fork — Do not use**
> * 🚫 **Use this template — Do not use**
> * ⭐ **Star** — The setup commands later in this README will bookmark this repository for you.
> * 👁️ **Watch**
>   * **Students:** Not recommended. Watching is not needed and may generate unnecessary notifications.
>   * **Faculty:** Consider selecting **Watch → Custom → Releases + Issues** to receive major repository updates and follow reported issues.

---

> [!NOTE]
> **🆕 New for 2026 C-5:** IT 140 now uses GitHub repositories to provide assignment starter files, development resources, and supporting documentation.
>
> If you find a problem with this GitHub repository or its instructions, or have a suggestion for improvement, please open [GitHub Issues](https://github.com/GC-STEM/it140-projects/issues) to review existing issues or create a new issue.

---

* **Course**: IT 140 - *Introduction to Scripting*
- **Task Titles**:
  - **5-3**: Project One Submission
  - **6-4**: Milestone: Moving Between Rooms
  - **7-3**: Project Two Submission
* **Task Type**: Required, graded, one submission required for each task
* **Repository Version**: 1.0.4
* **Repository Version DTG**: 2026-09-07-14-30
- **Program**: Text-Based Adventure Game
- **Repository Model**: One personal repository used across all three modules

> [!NOTE]
> The IT 140 project SDLC is distributed across **three modules**. Do not create
> a new project repository for each task.
>
> **Module 5:** Analyze + Design → submit Project One
> **Module 6:** Construct + Test a simplified prototype → submit the Milestone
> **Module 7:** Construct + Test the final game → submit Project Two

## Three Graded Checkpoints

| Module | Task | SDLC work | Graded deliverables | What carries forward |
| --- | --- | --- | --- | --- |
| 5 | Project One | Analyze + Design | `design/game_storyboard.md`, `design/game_map.drawio`, `design/move.pseudo`, `design/get_item.pseudo` | Your approved game world and command designs |
| 6 | Module Six Milestone | Construct + Test a reduced movement prototype | `prototype/move_between_rooms.py` | Movement/dictionary/loop experience and instructor feedback |
| 7 | Project Two | Construct + Test the complete game | `src/text_based_game.py` | Final implementation based on your Module 5 design, informed by Module 6 practice |

The Module Six prototype is intentionally **not** the complete Project Two
program. It uses a small course-provided dragon-game dictionary and an `exit`
ending so you can practice one part of the final system in a smaller problem.

## Start With the Current Guidelines and Rubric

Before beginning each checkpoint, open that task's current **Guidelines and
Rubric** in [D2L Brightspace](https://learn.snhu.edu/).

Those pages are the official sources for requirements, grading criteria, and
submission instructions. Repository documents reorganize those requirements
into a development workflow; they do not replace the D2L instructions.

Use this source priority if instructions ever differ:

1. Current task **Guidelines and Rubric** in D2L Brightspace
2. Instructions from your instructor
3. Current repository README and phase README files
4. Supplemental project Wiki pages

## How the Folders Map to the Three Modules

```text
it140-projects/
├── analysis/                   # Requirements reference across M5–M7
│   ├── README.md
│   └── text_based_game_srs.md
├── design/                     # M5 Project One: graded design deliverables
│   ├── README.md
│   ├── game_storyboard.md      # graded M5
│   ├── game_map.drawio         # graded M5
│   ├── move.pseudo             # graded M5
│   ├── get_item.pseudo         # graded M5
│   └── text_based_game_sdd.md  # course-provided reference
├── prototype/                  # M6 Milestone: reduced construct/test cycle
│   ├── README.md
│   ├── move_between_rooms.py   # graded M6
│   └── move_between_rooms_sdw.md
├── src/                        # M7 Project Two: final construction
│   ├── README.md
│   ├── text_based_game.py      # graded M7
│   └── text_based_game_sdw.md
├── tests/                      # M6/M7 testing guidance and working notes
│   ├── README.md
│   └── game_test_plan.md
└── README.md
```

Course-provided flowchart images and repository-management files are supporting
materials. They are not additional student submissions.

## What You May Edit

### Module Five | Project One

Required graded work:

- [`design/game_storyboard.md`](design/game_storyboard.md)
- [`design/game_map.drawio`](design/game_map.drawio)
- [`design/move.pseudo`](design/move.pseudo)
- [`design/get_item.pseudo`](design/get_item.pseudo)

### Module Six | Milestone

Required graded work:

- [`prototype/move_between_rooms.py`](prototype/move_between_rooms.py)

Optional working notes:

- [`prototype/move_between_rooms_sdw.md`](prototype/move_between_rooms_sdw.md)
- [`tests/game_test_plan.md`](tests/game_test_plan.md)

### Module Seven | Project Two

Required graded work:

- [`src/text_based_game.py`](src/text_based_game.py)

Optional working notes:

- [`src/text_based_game_sdw.md`](src/text_based_game_sdw.md)
- [`tests/game_test_plan.md`](tests/game_test_plan.md)

Leave the READMEs, SRS, SDD, reference images, CI files, tests, and repository
configuration unchanged unless current course instructions tell you otherwise.

## Set Up Your Personal Projects Repository

Complete these steps only once, normally when beginning Project One.

If you already have an `it140-projects` repository in your GitHub account or an
`it140-projects` folder in `~/Repos`, open that existing repository instead of
creating another one.

From the VS Code integrated terminal:

```bash
cd ~/Repos
gh auth setup-git
gh api --method PUT user/starred/GC-STEM/it140-projects
gh repo create it140-projects --template GC-STEM/it140-projects --private --clone
cd it140-projects
git remote -v
```

Review the final output and confirm that the repository belongs to your GitHub
account.

> [!NOTE]
> GitHub is used to develop and back up your work. **Submission, grading, and
> instructor feedback remain in D2L Brightspace.**

# Module Five | Project One

Project One covers the **Analyze and Design** portions of the project SDLC.
You are designing the game, not building the complete Python program yet.

## 1. Analyze the Project

Open [`analysis/README.md`](analysis/README.md).

Use the Project One Guidelines and Rubric, sample game resources, and the
[Text-Based Game SRS](analysis/text_based_game_srs.md) to identify:

- The game goal and losing condition
- The minimum room and item requirements
- The start-room and villain-room constraints
- What makes the map winnable
- The two command types: movement and getting an item
- The inputs, outputs, decisions, and repetition needed by those processes

## 2. Design the Game

Open [`design/README.md`](design/README.md) and complete all four graded design
files.

Project One is finished when your storyboard, map, movement pseudocode, and
get-item pseudocode form **one consistent design**.

### Project One Handoff

Keep these files after submitting them. They are not throwaway exercises.
In Module Seven, they become the source for your final room/item dictionary and
command logic. Review Project One instructor feedback before coding the final
game.

## 3. Save and Submit Project One

From the repository root, you may save the Project One work with:

```bash
git status
git add design/game_storyboard.md design/game_map.drawio
git add design/move.pseudo design/get_item.pseudo
git commit -m "Complete Project One design"
git push
```

Submit the four Project One files in D2L Brightspace according to the current
Project One **What to Submit** instructions.

# Module Six | Milestone

The milestone is a **reduced Construct + Test iteration**. It gives you practice
translating movement design into Python before you build the complete game.

## 1. Reopen the Same Repository

Do not create a second project repository. Open your existing
`~/Repos/it140-projects` folder.

Review:

- Your Project One [`design/move.pseudo`](design/move.pseudo)
- Any Project One instructor feedback
- The Module Six Milestone Guidelines and Rubric
- The Milestone Simplified Text Game Flowchart and supporting resources in D2L

## 2. Construct the Simplified Movement Prototype

Open [`prototype/README.md`](prototype/README.md) and complete:

- [`prototype/move_between_rooms.py`](prototype/move_between_rooms.py)

The milestone intentionally uses the **course-provided three-room dragon-game
dictionary**. Do not replace it with your Project One world for this checkpoint.

The prototype includes movement, an `exit` command, a gameplay loop, decision
branching, and input validation. It intentionally leaves out items, inventory,
the villain, and final win/loss behavior.

## 3. Test and Submit the Milestone

Use the Module Six section of [`tests/README.md`](tests/README.md) and, if
helpful, record results in [`tests/game_test_plan.md`](tests/game_test_plan.md).

Save the milestone with:

```bash
git status
git add prototype/move_between_rooms.py
git add prototype/move_between_rooms_sdw.md tests/game_test_plan.md
git commit -m "Complete Module Six movement milestone"
git push
```

Submit `move_between_rooms.py` in D2L Brightspace according to the current
milestone **What to Submit** instructions.

### Module Six Handoff

Keep the milestone file and instructor feedback. In Module Seven, you may reuse
or adapt useful movement, dictionary, branching, and loop ideas—but the final
game must switch back to **your Project One game world** and must end through
the required win/loss conditions rather than the milestone-only `exit` ending.

# Module Seven | Project Two

Project Two is the **final Construct + Test iteration** of the SDLC.

## 1. Reconcile Earlier Work Before Coding

Open [`src/README.md`](src/README.md). Review these inputs together:

1. Current Project Two Guidelines and Rubric
2. Project One storyboard
3. Project One game map
4. Project One movement pseudocode
5. Project One get-item pseudocode
6. Project One instructor feedback
7. Module Six prototype and instructor feedback
8. Project Two sample flowchart/output resources

Resolve design inconsistencies before creating the final room/item dictionary.

## 2. Construct the Complete Game

Complete:

- [`src/text_based_game.py`](src/text_based_game.py)

The final source must use **your Project One rooms, items, villain, and map**.
The milestone's three-room sample dictionary is not the final game data.

## 3. Test the Complete Game

Use [`tests/README.md`](tests/README.md) to test at least:

- Valid and invalid movement
- Valid and invalid item commands
- Inventory updates
- A complete winning path
- A complete losing path
- Readability and removal of unfinished starter placeholders

Use your map to plan deterministic playthroughs instead of relying on random
exploration.

## 4. Save and Submit Project Two

```bash
git status
git add src/text_based_game.py
git add src/text_based_game_sdw.md tests/game_test_plan.md
git commit -m "Complete Project Two text game"
git push
```

Submit `text_based_game.py` in D2L Brightspace according to the current Project
Two **What to Submit** instructions.

# Review the Automated Repository Checks

Each push runs the **Project Checks** workflow. The checks understand the
three-checkpoint sequence:

- **Module 5:** Project One design files must be completed.
- **Module 6:** Project One remains complete and the milestone prototype must be
  completed.
- **Module 7:** Project One and the milestone remain complete and the final
  Project Two source must be completed.

The active checkpoint is inferred from which later graded file has been changed.
A red **X** while you are still working can simply mean a checkpoint is not yet
complete.

The checks verify basic structure and completion state. They do **not** assign a
grade, prove that your map is winnable, or prove that every path through your
final game is correct. Manual requirement-based testing is still required.

To review a run:

1. Open your personal `it140-projects` repository on GitHub.
2. Select **Actions**.
3. Open the most recent **Project Checks** run.
4. Open **Check projects repository** for details.

# Return to Existing Work

You create the personal repository only once. When returning in a later module:

1. Open VS Code.
2. Select **File > Open Folder**.
3. Open `~/Repos/it140-projects`.
4. Run `git status`.
5. Continue from the current module checkpoint.

If you move to another computer, clone your existing personal repository. Do
not create a new repository from the course template just because the module
changed.

# Help and Support

Start with the [IT 140 Projects Wiki](https://github.com/GC-STEM/it140-projects/wiki)
for supplemental explanations.

Use repository [Issues](https://github.com/GC-STEM/it140-projects/issues) for a
reproducible technical problem with repository files, starter content, or
repository instructions.

Use repository
[Discussions](https://github.com/GC-STEM/it140-projects/discussions) for
repository-related questions that may help other students.

Do **not** post completed graded solutions.

Contact your instructor through the course-approved D2L Brightspace channel for
questions about requirements, submissions, grading, feedback, deadlines,
accommodations, or your individual work.
