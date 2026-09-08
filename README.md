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
> **🆕 New for 2026 C-5:** IT 140 now uses GitHub repositories to provide project starter files, development resources, and supporting documentation.
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
> The IT 140 project SDLC is distributed across **three modules**. Do not create a new project repository for each task.
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

The Module Six prototype is intentionally **not** the complete Project Two program. It uses a small course-provided dragon-game dictionary and an `exit` ending so you can practice one part of the final system in a smaller problem.

## Start With the Current Guidelines and Rubric

Before beginning each checkpoint, open that task's current **Guidelines and Rubric** in [D2L Brightspace](https://learn.snhu.edu/).

Those pages are the official sources for requirements, grading criteria, and submission instructions. Repository documents reorganize those requirements into a development workflow; they do not replace the D2L instructions.

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

Course-provided flowchart images and repository-management files are supporting materials. They are not additional student submissions.

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

Leave the READMEs, SRS, SDD, reference images, CI files, tests, and repository configuration unchanged unless current course instructions tell you otherwise.

## Set Up or Open Your Personal Projects Repository

You create your personal `it140-projects` repository only once, normally when beginning Project One. Continue using the same personal repository in Modules Six and Seven.

> [!IMPORTANT]
> **Windows users:** Run all `bash` command blocks in this README in a **Git Bash** terminal. Do not use PowerShell or Command Prompt for these command blocks.

### If You Have Not Created It Yet

First confirm the GitHub account you use for IT 140:

```bash
gh auth status
```

If the correct account is not active, use the GitHub CLI sign-in or account-switching instructions from the Module One Setup Tasks before continuing.

Then run:

<!-- ci:command-test id=setup-personal-repo fixture=empty-repos expect=repo -->
```bash
cd ~/Repos
gh auth setup-git
gh api --method PUT user/starred/GC-STEM/it140-projects
gh repo create it140-projects --template GC-STEM/it140-projects --private --clone
cd it140-projects
git remote -v
```

Review the final output and confirm that the repository belongs to **your GitHub account**.

> [!NOTE]
> These creation commands are for the first successful setup only. Do not create another personal project repository when the course moves to Module Six or Module Seven.

### If You Already Created It on This Device

Open the existing local clone:

<!-- ci:command-test id=open-existing-repo fixture=existing-repo expect=repo -->
```bash
cd ~/Repos/it140-projects
code .
```

*Reminder*. In terminal commands, **`~`** means your home folder, and **`.`** means the current working directory. `code .` opens the current folder in VS Code.

>*Note*
> If VS Code opens in Restricted Mode, your `~/Repos` folder should already be trusted if you completed the Module One course IDE setup. Normally, you will not see this warning.
>
> If you see the **Restricted Mode** warning bar:
>
> ![Restricted Mode warning bar in VS Code](https://raw.githubusercontent.com/GC-STEM/it140-m2-assignment/main/.github/assets/22_vscode_restricted_mode_bar.png)
>
> 1. Click **Manage** on the **Restricted Mode** warning bar.
> 2. In **Workspace Trust**, find **Trusted Folders & Workspaces**.
> 3. Use the control in that section to add a trusted folder.
> 4. In the folder selection window, go to your home folder and select the entire **Repos** folder.
> 5. Confirm the folder selection and trust it when prompted.
> 6. Verify that your **Repos** folder appears under **Trusted Folders & Workspaces**.
>
> Trust the entire `~/Repos` folder rather than only `it140-projects`. VS Code applies trust to all subfolders of a trusted parent folder.

### Understand the Related Copies

Your course project normally has three related copies:

* **Public course template on GitHub:** `GC-STEM/it140-projects`. This is the course-provided starting point. Do not fork or edit this copy.
* **Your personal GitHub repository:** `it140-projects` in your own GitHub account. This stores work you push to GitHub across Modules Five–Seven.
* **A local clone on a device:** Usually `~/Repos/it140-projects`. This is the copy you open in VS Code and edit.

The setup command creates the personal GitHub repository and then creates its local clone on the device where you run the command.

### If Your Personal Repository Exists but This Device Does Not Have a Local Clone

Clone your existing personal repository rather than creating a new one:

<!-- ci:command-test id=clone-existing-repo fixture=empty-repos expect=repo -->
```bash
cd ~/Repos
gh repo clone "$(gh api user --jq .login)/it140-projects"
cd it140-projects
git status
```

### If You Work on More Than One Device

Using one device for the projects is the simplest and safest approach. Because the same repository carries work across three modules, always synchronize before switching devices.

Before leaving the device where you have been working:

<!-- ci:command-test id=sync-before-switch fixture=existing-repo expect=repo -->
```bash
cd ~/Repos/it140-projects
git status
git add design/game_storyboard.md design/game_map.drawio design/move.pseudo design/get_item.pseudo
git add prototype/move_between_rooms.py prototype/move_between_rooms_sdw.md
git add src/text_based_game.py src/text_based_game_sdw.md tests/game_test_plan.md
git commit -m "Save IT 140 project progress"
git push
```

On the other device, before editing any project file:

<!-- ci:command-test id=sync-after-switch fixture=existing-repo expect=repo -->
```bash
cd ~/Repos/it140-projects
git pull --ff-only
git status
```

> [!WARNING]
> If `git pull --ff-only` or `git push` reports an error or says the histories cannot be fast-forwarded, **stop and do not make more changes on either device** until you get help. Do not try random merge, reset, or force-push commands.

> [!IMPORTANT]
> **Saving your work to GitHub does not submit any project or milestone.** Submission, grading, and instructor feedback remain in D2L Brightspace.

# Module Five | Project One

Project One covers the **Analyze and Design** portions of the project SDLC. You are designing the game, not building the complete Python program yet.

## 1. Analyze the Project

Open [`analysis/README.md`](analysis/README.md).

Use the Project One Guidelines and Rubric, sample game resources, and the [Text-Based Game SRS](analysis/text_based_game_srs.md) to identify:

- The game goal and losing condition
- The minimum room and item requirements
- The start-room and villain-room constraints
- What makes the map winnable
- The two command types: movement and getting an item
- The inputs, outputs, decisions, and repetition needed by those processes

## 2. Design the Game

Open [`design/README.md`](design/README.md) and complete all four graded design files.

Project One is finished when your storyboard, map, movement pseudocode, and get-item pseudocode form **one consistent design**.

### Project One Handoff

Keep these files after submitting them. They are not throwaway exercises. In Module Seven, they become the source for your final room/item dictionary and command logic. Review Project One instructor feedback before coding the final game.

## 3. Save and Submit Project One

Before submitting, save your Project One work to your personal GitHub repository:

<!-- ci:command-test id=save-project-one fixture=existing-repo expect=repo -->
```bash
cd ~/Repos/it140-projects
git status
git add design/game_storyboard.md design/game_map.drawio
git add design/move.pseudo design/get_item.pseudo
git commit -m "Complete Project One design"
git push
```

These commands:

* `git status` shows the current state of your local repository.
* `git add` prepares the four Project One design files to be saved.
* `git commit` saves a snapshot in your local Git repository.
* `git push` uploads that commit to your personal GitHub repository.

If Git reports `nothing to commit, working tree clean`, your current files have already been committed. The `git push` command will still check whether GitHub is up to date.

Submit the four Project One files in D2L Brightspace according to the current Project One **What to Submit** instructions.

# Module Six | Milestone

The milestone is a **reduced Construct + Test iteration**. It gives you practice translating movement design into Python before you build the complete game.

## 1. Reopen the Same Repository

Do not create a second project repository.

<!-- ci:command-test id=open-module-six fixture=existing-repo expect=repo -->
```bash
cd ~/Repos/it140-projects
code .
```

Review:

- Your Project One [`design/move.pseudo`](design/move.pseudo)
- Any Project One instructor feedback
- The Module Six Milestone Guidelines and Rubric
- The Milestone Simplified Text Game Flowchart and supporting resources in D2L

## 2. Construct the Simplified Movement Prototype

Open [`prototype/README.md`](prototype/README.md) and complete:

- [`prototype/move_between_rooms.py`](prototype/move_between_rooms.py)

The milestone intentionally uses the **course-provided three-room dragon-game dictionary**. Do not replace it with your Project One world for this checkpoint.

The prototype includes movement, an `exit` command, a gameplay loop, decision branching, and input validation. It intentionally leaves out items, inventory, the villain, and final win/loss behavior.

## 3. Test and Submit the Milestone

Use the Module Six section of [`tests/README.md`](tests/README.md) and, if helpful, record results in [`tests/game_test_plan.md`](tests/game_test_plan.md).

Before submitting, save the milestone:

<!-- ci:command-test id=save-module-six fixture=existing-repo expect=repo -->
```bash
cd ~/Repos/it140-projects
git status
git add prototype/move_between_rooms.py
git add prototype/move_between_rooms_sdw.md tests/game_test_plan.md
git commit -m "Complete Module Six movement milestone"
git push
```

Submit `move_between_rooms.py` in D2L Brightspace according to the current milestone **What to Submit** instructions.

### Module Six Handoff

Keep the milestone file and instructor feedback. In Module Seven, you may reuse or adapt useful movement, dictionary, branching, and loop ideas—but the final game must switch back to **your Project One game world** and must end through the required win/loss conditions rather than the milestone-only `exit` ending.

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

The final source must use **your Project One rooms, items, villain, and map**. The milestone's three-room sample dictionary is not the final game data.

## 3. Test the Complete Game

Use [`tests/README.md`](tests/README.md) to test at least:

- Valid and invalid movement
- Valid and invalid item commands
- Inventory updates
- A complete winning path
- A complete losing path
- Readability and removal of unfinished starter placeholders

Use your map to plan deterministic playthroughs instead of relying on random exploration.

## 4. Save and Submit Project Two

Before submitting, save your completed Project Two work:

<!-- ci:command-test id=save-project-two fixture=existing-repo expect=repo -->
```bash
cd ~/Repos/it140-projects
git status
git add src/text_based_game.py
git add src/text_based_game_sdw.md tests/game_test_plan.md
git commit -m "Complete Project Two text game"
git push
```

Submit `text_based_game.py` in D2L Brightspace according to the current Project Two **What to Submit** instructions.

# Review the Automated Repository Checks

Each push to a personal repository runs the **IT 140 Checks** workflow. The student-facing **Project checkpoint check** understands the three-checkpoint sequence:

- **Module 5:** After Project One graded work begins, all four Project One design files are expected to be completed.
- **Module 6:** After the milestone source changes, Project One must remain complete and the milestone prototype must be completed.
- **Module 7:** After the final source changes, Project One and the milestone must remain complete and the final Project Two source must be completed.

A newly created personal repository should **not** fail merely because all graded files are still untouched starter files. Changes only to optional working notes also do not start a graded checkpoint.

Once graded work begins, a failed check is formative development feedback. For example, it can indicate that a checkpoint is only partly complete, a starter TODO remains, a Python file has a syntax problem, or a course-managed file changed unexpectedly.

For Module Six and Module Seven Python work, Ruff provides **advisory code-style feedback**. Ruff suggestions do not by themselves make the student workflow fail.

The checks verify basic structure and completion state. They do **not** assign a grade, prove that your map is winnable, or prove that every path through your final game is correct. Manual requirement-based testing is still required.

To review a run:

1. Open your personal `it140-projects` repository on GitHub.
2. Select **Actions**.
3. Open the most recent **IT 140 Checks** run.
4. Open **Project checkpoint check** and review the summary.
5. Review **Code style feedback** when Module Six or Module Seven Python has changed.

# Return to Existing Work

You create the personal repository only once. When returning in a later module:

<!-- ci:command-test id=return-existing-work fixture=existing-repo expect=repo -->
```bash
cd ~/Repos/it140-projects
git pull --ff-only
git status
code .
```

> [!NOTE]
> Run `git pull --ff-only` before editing when another device may have newer commits. If this command fails, stop and get help before making changes.

If your personal repository exists on GitHub but the current device has no local clone, use the [clone-existing-repo](#if-your-personal-repository-exists-but-this-device-does-not-have-a-local-clone) instructions above. Do not create a new repository from the course template just because the module changed.

# Help and Support

Start with the [IT 140 Projects Wiki](https://github.com/GC-STEM/it140-projects/wiki) for supplemental explanations.

- Use repository [Issues](https://github.com/GC-STEM/it140-projects/issues) for a reproducible technical problem with provided repository files, starter content, documentation, or automated checks.
- Use repository [Discussions](https://github.com/GC-STEM/it140-projects/discussions) for repository-related questions that may help other students and do not request a completed graded solution.
- For **Codio Virtual Desktop performance, access, or outage problems**, contact the **IT Service Desk** using the link on the main menu bar in D2L Brightspace.
- For **course IDE setup or lifecycle-script problems**, see [Setup Problems and Support](https://github.com/GC-STEM/it140-m1-setup-tasks/wiki/Setup-Problems-and-Support).
- Contact your instructor through D2L Brightspace for requirements, submissions, grading, feedback, deadlines, accommodations, or questions about your individual work.

Do **not** post completed graded solutions, credentials, access tokens, or private identifying information in public GitHub Issues or Discussions.
