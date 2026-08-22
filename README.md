# IT 140 Projects | Modules Five–Seven

- **Course**: IT 140 - Introduction to Scripting
- **Sequence**: Project One → Module Six Milestone → Project Two
- **Program**: Text-Based Adventure Game

**Project progress:** **0 Start Here** → [1 Analyze](analysis/README.md) → [2 Design | M5](design/README.md) → [3 Prototype | M6](prototype/README.md) → [4 Construct | M7](src/README.md) → [5 Test](tests/README.md)

## Start With the Current Guidelines and Rubrics

This repository supports three graded activities that build on one another:

1. **Module Five | Project One** — design the game.
2. **Module Six | Milestone** — build a simplified movement prototype.
3. **Module Seven | Project Two** — construct and test the complete game.

Before beginning each checkpoint, open its current **Guidelines and Rubric** in
[D2L Brightspace](https://learn.snhu.edu/). Those course materials are the
official source for requirements, grading, and submission instructions.

The repository documents reorganize those requirements into a simplified
software-development workflow. If a repository document and the current D2L
materials differ, follow the current D2L materials.

## About This Repository

Keep the **same personal repository** for Modules Five, Six, and Seven. Your
design work from Project One becomes input to the Module Six prototype and the
final Project Two game.

The repository follows this simplified development sequence:

> **Analyze → Design → Prototype → Construct → Test**

The main folders are:

```text
it140-projects/
├── analysis/
│   └── text_based_game_srs.md
├── design/
│   ├── game_storyboard.md
│   ├── game_map.drawio
│   ├── move.pseudo
│   └── get_item.pseudo
├── prototype/
│   └── move_between_rooms.py
├── src/
│   ├── text_based_game.py
│   └── text_based_game_sdw.md
├── tests/
│   └── game_test_plan.md
└── README.md
```

### What You May Edit

Your graded work is limited to these checkpoint files:

- `design/game_storyboard.md`
- `design/game_map.drawio`
- `design/move.pseudo`
- `design/get_item.pseudo`
- `prototype/move_between_rooms.py`
- `src/text_based_game.py`

You may also edit these optional working files:

- `prototype/move_between_rooms_sdw.md`
- `src/text_based_game_sdw.md`
- `tests/game_test_plan.md`

Leave the READMEs, SRS, SDD, provided reference images, tests, `.github`
files, repository configuration, and other course-managed files unchanged
unless your instructor or course instructions tell you otherwise.

## Set Up Your Personal Projects Repository

Complete these steps only once.

If you already created an `it140-projects` repository in your GitHub account
or already have an `it140-projects` folder in `~/Repos`, open that existing
repository instead of creating another one.

From the VS Code integrated terminal:

```bash
cd ~/Repos
gh auth setup-git
gh api --method PUT /user/starred/GC-STEM/it140-projects
gh repo create it140-projects --template GC-STEM/it140-projects --private --clone
cd it140-projects
git remote -v
```

Review the final output and confirm that the repository belongs to your
GitHub account.

> [!NOTE]
> GitHub is used to develop and back up your work. **Submission, grading, and
> instructor feedback remain in D2L Brightspace.**

## Module Five | Project One

Project One is the **Design** checkpoint.

Open the [Analyze Phase](analysis/README.md), then the
[Design Phase](design/README.md).

Complete the four graded Project One design files:

1. [`design/game_storyboard.md`](design/game_storyboard.md)
2. [`design/game_map.drawio`](design/game_map.drawio)
3. [`design/move.pseudo`](design/move.pseudo)
4. [`design/get_item.pseudo`](design/get_item.pseudo)

The storyboard and map describe **your** game world. The two pseudocode files
describe the movement and get-item processes that later become part of the
final game.

Before submission, compare the four artifacts for consistent room names,
items, villain placement, and movement behavior.

Submit the Project One deliverables in D2L Brightspace according to the
current Project One Guidelines and Rubric.

## Module Six | Milestone

Keep the same repository after Project One.

Open the [Prototype Phase](prototype/README.md) and complete:

- [`prototype/move_between_rooms.py`](prototype/move_between_rooms.py)

The milestone intentionally uses the small provided dragon-game dictionary.
It is a simplified movement prototype, not the complete Project Two game.

Run it from the repository root:

```bash
python3 prototype/move_between_rooms.py
```

Use the milestone checklist and
[`tests/game_test_plan.md`](tests/game_test_plan.md) to test valid movement,
invalid input, and the required exit behavior.

Submit the milestone file in D2L Brightspace according to the current Module
Six Milestone Guidelines and Rubric.

## Module Seven | Project Two

Keep the same repository again.

Open the [Construct Phase](src/README.md) and complete:

- [`src/text_based_game.py`](src/text_based_game.py)

Build the final game from **your Project One design**, not from the small
Module Six dictionary.

Then use the [Test Phase](tests/README.md) to check movement, item collection,
invalid commands, a complete winning path, and a complete losing path.

Run the final game from the repository root:

```bash
python3 src/text_based_game.py
```

Submit the final source file in D2L Brightspace according to the current
Project Two Guidelines and Rubric.

## Save Your Work to GitHub

Save normally while you work. Periodically commit and push the files that
students are allowed to edit:

```bash
cd ~/Repos/it140-projects
git status
git add \
  design/game_storyboard.md \
  design/game_map.drawio \
  design/move.pseudo \
  design/get_item.pseudo \
  prototype/move_between_rooms.py \
  prototype/move_between_rooms_sdw.md \
  src/text_based_game.py \
  src/text_based_game_sdw.md \
  tests/game_test_plan.md
git commit -m "Save IT 140 project progress"
git push
```

Git ignores unchanged files, so listing files you have not edited does not
add extra content to the commit.

## Review the Automated Repository Checks

Each push runs the **Project Checks** workflow in your personal repository.

The checks understand that this repository spans three modules:

- Before the prototype changes, CI checks the **Project One** design
  checkpoint.
- After `prototype/move_between_rooms.py` changes, CI checks Project One plus
  the **Module Six Milestone** checkpoint.
- After `src/text_based_game.py` changes, CI checks the earlier work plus the
  **Project Two** checkpoint.

While you are actively completing a checkpoint, a red **X** can simply mean a
required starter `TODO:` remains or not all files for that checkpoint have
been changed yet.

The checks verify items such as:

- Course-managed files remain present.
- Student changes stay within the allowed working and deliverable files.
- Project One design files differ from their starter state.
- The Draw.io game map remains readable XML.
- The Module Six prototype keeps the required simplified room dictionary and
  contains the expected basic programming structures.
- The Project Two source is valid Python and contains the expected basic
  program structures.
- Repository configuration and Markdown links remain internally consistent.
- The repository social-preview image remains a valid, appropriately sized
  PNG.

The checks **do not** assign a grade or prove that your map is winnable, that
all game logic is correct, or that your final program satisfies every rubric
criterion. Use the current Guidelines and Rubric and perform the required
manual testing.

To review a run:

1. Open your personal `it140-projects` repository on GitHub.
2. Select **Actions**.
3. Open the most recent **Project Checks** run.
4. Open **Check projects repository** to see which check needs attention.

## Return to Existing Work

You create this personal repository only once.

When returning later:

1. Open VS Code.
2. Select **File > Open Folder**.
3. Open `~/Repos/it140-projects`.
4. Run `git status`.
5. Continue from the current project checkpoint.

If another computer does not yet have your repository, clone your existing
personal repository rather than creating a new one from the template.

## Help and Support

Start with the [IT 140 Projects Wiki](https://github.com/GC-STEM/it140-projects/wiki)
for supplemental explanations and common questions.

Use repository [Issues](https://github.com/GC-STEM/it140-projects/issues) for
reproducible technical problems with the repository, starter files, or
repository instructions.

Use repository
[Discussions](https://github.com/GC-STEM/it140-projects/discussions) for
repository-related questions that may help other students.

Do **not** post completed graded solutions.

Contact your instructor through the course-approved D2L Brightspace channel
for questions about assignment requirements, submissions, grading, rubric
feedback, deadlines, accommodations, or your individual work.
