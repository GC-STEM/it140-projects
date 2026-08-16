# IT 140 Projects | Modules Five Through Seven

- **Course**: IT 140 - Introduction to Scripting
- **Activities**: Project One, Module Six Milestone, and Project Two
- **Program**: Text-Based Adventure Game
- **Repository use**: Create one personal repository in Module Five and continue using it through Module Seven

**Project progress:** **0 Start Here** → [1 Analyze](analysis/README.md) → [2 Design | M5 Project One](design/README.md) → [3 Prototype | M6 Milestone](prototype/README.md) → [4 Construct | M7 Project Two](src/README.md) → [5 Test](tests/README.md)

## Start With the Current Guidelines and Rubrics

This repository supports three graded activities that build on the same text-based game:

| Module | Graded activity | Main purpose | Required deliverable(s) |
| --- | --- | --- | --- |
| **5** | **Project One** | Design your game before coding it | `game_storyboard.md`, `game_map.drawio`, `move.pseudo`, `get_item.pseudo` |
| **6** | **Module Six Milestone** | Build and test a simplified movement prototype | `move_between_rooms.py` |
| **7** | **Project Two** | Develop and test the complete text-based game | `text_based_game.py` |

Before beginning work for a module, open that activity's **Guidelines and Rubric** in [D2L Brightspace](https://learn.snhu.edu/). The current Guidelines and Rubric is the official source for requirements, grading criteria, and submission instructions. This repository provides starter files, requirements references, working files, and step-by-step guidance to help you complete those requirements.

> [!IMPORTANT]
> You will use the **same personal `it140-projects` repository for Modules Five, Six, and Seven**. Do not create a new project repository in Module Six or Module Seven.

> [!NOTE]
> GitHub is used to develop and back up your work. **Project submission, grading, and instructor feedback remain in D2L Brightspace.**

## How the Three Activities Fit Together

The project follows a simplified Software Development Life Cycle (SDLC), but the phases are spread across three modules:

> **Analyze → Design → Prototype → Construct → Test**

- **Module Five — Project One:** analyze the game requirements and create the graded design artifacts.
- **Module Six — Milestone:** build a simplified movement-only prototype using a provided three-room dictionary. This gives you practice translating movement pseudocode into working Python.
- **Module Seven — Project Two:** use your Project One design and what you learned from the milestone to construct, debug, and test the complete game.

The Module Six prototype is intentionally smaller than the final game. It does **not** include the complete items, inventory, villain, or win/loss behavior required in Project Two.

## About This Repository

The main student-work folders are:

```text
it140-projects/
├── analysis/
│   ├── README.md
│   └── text_based_game_srs.md
├── design/
│   ├── README.md
│   ├── text_based_game_sdd.md
│   ├── game_storyboard.md
│   ├── game_map.drawio
│   ├── move.pseudo
│   └── get_item.pseudo
├── prototype/
│   ├── README.md
│   └── move_between_rooms.py
├── src/
│   ├── README.md
│   └── text_based_game.py
├── tests/
│   ├── README.md
│   └── game_test_plan.md
├── text_based_game_sdw.md
└── README.md
```

This repository may also contain course-managed configuration files and folders that are not shown above. Leave those files unchanged unless your instructor or course instructions tell you otherwise.

### What You May Edit

Your graded work is completed in these files:

**Module Five — Project One**

- [`design/game_storyboard.md`](design/game_storyboard.md)
- [`design/game_map.drawio`](design/game_map.drawio)
- [`design/move.pseudo`](design/move.pseudo)
- [`design/get_item.pseudo`](design/get_item.pseudo)

**Module Six — Milestone**

- [`prototype/move_between_rooms.py`](prototype/move_between_rooms.py)

**Module Seven — Project Two**

- [`src/text_based_game.py`](src/text_based_game.py)

You may also edit these recommended working files:

- [`text_based_game_sdw.md`](text_based_game_sdw.md) — Software Development Worksheet (SDW); not submitted unless your instructor directs otherwise
- [`tests/game_test_plan.md`](tests/game_test_plan.md) — manual test notes; not a required graded deliverable

Leave the READMEs, SRS, SDD, repository configuration, and other provided course-managed files unchanged unless your instructor or course instructions tell you otherwise.

## Set Up Your Personal Project Repository

Complete these steps **once in Module Five** before beginning Project One.

If you already created an `it140-projects` repository in your GitHub account or already have an `it140-projects` folder in `~/Repos`, do not repeat these steps. Open your existing repository instead.

### 1. Open the VS Code Integrated Terminal

In VS Code, select:

> **Terminal > New Terminal**

> [!IMPORTANT]
> Windows users must use a **PowerShell** or **Git Bash** terminal in VS Code for the commands in this file. Do not use Command Prompt (`cmd.exe`).

### 2. Confirm Your GitHub Account

Run:

```bash
gh auth status
```

Confirm that the active account is the GitHub account you use for IT 140.

If the correct account is listed but not active, run:

```bash
gh auth switch --user your-github-username
```

If the account is not listed, run:

```bash
gh auth login --web
```

Then run `gh auth status` again.

### 3. Create and Clone Your Personal Repository

Copy the entire command block and paste it into the VS Code integrated terminal:

```bash
cd ~/Repos
gh auth setup-git
gh api --method PUT /user/starred/GC-STEM/it140-projects
gh repo create it140-projects --template GC-STEM/it140-projects --private --clone
cd it140-projects
git remote -v
```

The commands star the course template, create a **private** personal repository from the current template, clone it into `~/Repos`, and show the remote connected to your local copy.

If a command reports an error, do not repeat the entire block. Read the error message and use the [Help and Support](#help-and-support) resources.

### 4. Open the Repository in VS Code

1. Select **File > Open Folder**.
2. Open `~/Repos/it140-projects`.
3. Confirm that `it140-projects` is the top-level folder shown in the Explorer.

You will keep using this same folder and personal GitHub repository through Module Seven.

---

# Module Five | Project One

## 1. Analyze the Game Requirements

Open the [Analyze Phase instructions](analysis/README.md).

Use the Project One Guidelines and Rubric and the provided [Software Requirements Specification (SRS)](analysis/text_based_game_srs.md) to identify:

- The required theme and storyline information
- Minimum room and item counts
- Start-room and villain-room constraints
- What must make the game winnable
- The two kinds of player commands required in the full game
- The required input, output, decisions, and loops for movement and getting items

You may record short planning notes in [`text_based_game_sdw.md`](text_based_game_sdw.md).

## 2. Create the Project One Designs

Open the [Design Phase instructions](design/README.md).

Complete all four Project One deliverables:

1. [`design/game_storyboard.md`](design/game_storyboard.md)
2. [`design/game_map.drawio`](design/game_map.drawio)
3. [`design/move.pseudo`](design/move.pseudo)
4. [`design/get_item.pseudo`](design/get_item.pseudo)

Project One is a **design project**. Do not replace the required design artifacts with Python code.

> [!NOTE]
> The current Project One directions refer to provided flowcharts for the move-between-rooms and get-item processes. Use those flowcharts as references for the two pseudocode deliverables; they are not listed as separate student-created submission files in the current Guidelines and Rubric.

## 3. Save Your Module Five Work to GitHub

From the repository root:

```bash
git status
git add text_based_game_sdw.md design/game_storyboard.md design/game_map.drawio design/move.pseudo design/get_item.pseudo
git commit -m "Complete Project One design"
git push
```

## 4. Submit Project One in D2L Brightspace

Return to the current **Project One Guidelines and Rubric** in D2L Brightspace before submitting.

Submit the required Project One files in the formats specified there:

- Storyboard: `.md`
- Map: `.drawio`
- Move pseudocode: `.pseudo`
- Get-item pseudocode: `.pseudo`

Do **not** submit the SRS, SDD, SDW, README files, or your GitHub repository unless the Guidelines and Rubric or your instructor specifically tells you to do so.

---

# Module Six | Milestone

## 1. Return to Your Existing Project Repository

Do **not** create another repository.

Open:

```text
~/Repos/it140-projects
```

If you are on a different computer and the repository is not there, clone your existing personal repository:

```bash
cd ~/Repos
gh repo clone "$(gh api user --jq .login)/it140-projects"
cd it140-projects
git status
```

## 2. Build the Simplified Movement Prototype

Open the [Prototype Phase instructions](prototype/README.md), then complete:

[`prototype/move_between_rooms.py`](prototype/move_between_rooms.py)

The milestone uses a provided simplified three-room dragon-game dictionary and focuses on:

- Displaying the current room
- Accepting movement or `exit` commands
- Using decision branching
- Using a gameplay loop
- Validating commands
- Ending the loop when the player exits
- Debugging and readability

Use your Project One movement pseudocode as a design reference where it applies, but follow the **Module Six Milestone Guidelines and Rubric** for the milestone's required simplified behavior.

## 3. Test and Save the Prototype

Run the program from the repository root:

```bash
python3 prototype/move_between_rooms.py
```

On Windows, if the course IDE provides `python` instead of `python3`, use:

```powershell
python prototype/move_between_rooms.py
```

Then save your work:

```bash
git status
git add text_based_game_sdw.md prototype/move_between_rooms.py tests/game_test_plan.md
git commit -m "Complete Module Six movement milestone"
git push
```

## 4. Submit the Module Six Milestone in D2L Brightspace

Return to the current **Module Six Milestone Guidelines and Rubric** before submitting.

Submit the required Python source file:

- `move_between_rooms.py`

GitHub does not submit the milestone for grading.

---

# Module Seven | Project Two

## 1. Continue in the Same Repository

Open the same personal `it140-projects` repository you used for Project One and the milestone.

Before editing Project Two code, review:

- Your Project One storyboard and map
- Your Project One move and get-item pseudocode
- Your Module Six milestone code
- Any instructor feedback from Project One or the milestone
- The current Project Two Guidelines and Rubric

## 2. Construct the Full Game

Open the [Construct Phase instructions](src/README.md), then complete:

[`src/text_based_game.py`](src/text_based_game.py)

Project Two extends beyond the milestone. The final game must use **your Project One design** and include the complete required behavior, including rooms, items, inventory, villain, commands, status output, win/loss conditions, functions, input validation, a gameplay loop, and industry-standard readability practices.

Do not keep the milestone's simplified `exit`-room condition as the final game's end condition. Project Two ends when the player **wins or loses** according to the current Project Two requirements.

## 3. Test the Full Game

Open the [Test Phase instructions](tests/README.md).

Use your own map to test several paths, including:

- Valid movement
- Invalid movement
- Valid item collection
- Invalid item commands
- Inventory updates
- A complete winning path
- A losing path that reaches the villain too early

Record useful test notes in [`tests/game_test_plan.md`](tests/game_test_plan.md).

## 4. Save Your Final Project Work to GitHub

```bash
git status
git add text_based_game_sdw.md src/text_based_game.py tests/game_test_plan.md
git commit -m "Complete Project Two text-based game"
git push
```

## 5. Submit Project Two in D2L Brightspace

Return to the current **Project Two Guidelines and Rubric** before submitting.

Submit the required Python source file:

- `text_based_game.py`

Do **not** submit the milestone prototype as a substitute for the Project Two file.

## Return to an Existing Project

You create your personal `it140-projects` repository only once.

When you return later:

1. Open VS Code.
2. Select **File > Open Folder**.
3. Open `~/Repos/it140-projects`.
4. Continue working where you stopped.

If you work on more than one computer, push your current work from the first computer before cloning or pulling it on another computer.

## Restore Your Local Copy From GitHub

Use this when your local folder is damaged or confusing but the copy you previously pushed to GitHub is good.

### CVD, Linux, macOS, or Git Bash on Windows

```bash
cd ~/Repos
mv it140-projects "it140-projects-local-backup-$(date +%Y%m%d-%H%M%S)"
gh repo clone "$(gh api user --jq .login)/it140-projects"
cd it140-projects
git status
```

### Windows PowerShell

```powershell
cd ~/Repos
Rename-Item it140-projects "it140-projects-local-backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
gh repo clone "$(gh api user --jq .login)/it140-projects"
cd it140-projects
git status
```

Your previous local folder remains in `~/Repos` as a backup.

## Start Over From the Current Course Template

Use this only when you intentionally want to restart the entire Modules Five–Seven project sequence from the current course template.

> [!WARNING]
> Starting over does not automatically copy your existing Project One designs, milestone code, or Project Two code into the new repository. Preserve your existing work first.

### CVD, Linux, macOS, or Git Bash on Windows

```bash
cd ~/Repos
backup="it140-projects-backup-$(date +%Y%m%d-%H%M%S)"
mv it140-projects "$backup"
gh repo rename "$backup" --repo "$(gh api user --jq .login)/it140-projects" --yes
gh repo create it140-projects --template GC-STEM/it140-projects --private --clone
cd it140-projects
git remote -v
```

### Windows PowerShell

```powershell
cd ~/Repos
$backup = "it140-projects-backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
Rename-Item it140-projects $backup
gh repo rename $backup --repo "$(gh api user --jq .login)/it140-projects" --yes
gh repo create it140-projects --template GC-STEM/it140-projects --private --clone
cd it140-projects
git remote -v
```

## Help and Support

The README files contain the current step-by-step instructions for each project phase. The [IT 140 Projects Wiki](https://github.com/GC-STEM/it140-projects/wiki) provides supplemental information about:

- The three-module project workflow
- Project One design artifacts
- The Module Six prototype
- Project Two construction and testing
- Working with project files in VS Code
- Git and GitHub workflows
- Sources, citations, and AI use
- Common project questions and technical support

Use [GitHub Issues](https://github.com/GC-STEM/it140-projects/issues) to report a technical problem with the provided course repository, starter files, documentation, or course tools.

Use [GitHub Discussions](https://github.com/GC-STEM/it140-projects/discussions) for repository-related questions when appropriate. **Do not ask for or post completed solutions to graded project or milestone work.**

Post questions about course content that are not specific to this repository in your section's **General Questions** discussion topic.

For questions about submissions, grading, deadlines, accommodations, or instructor feedback, contact your instructor through D2L Brightspace.

## Academic Integrity and AI Use

Keep your personal project repository **private**. Do not publish completed project solutions or post them in public Discussions, Issues, forums, or answer-sharing sites.

If you use generative AI or other outside sources while working on a graded activity, follow the current course and assignment guidance. Acknowledge and cite sources when required. The repository Wiki includes additional guidance, but the current D2L activity instructions control if they differ.
