<!-- To see this file in a clean, formatted view, select ▼ in the upper-right corner of the editor pane, then select "Markdown Preview". -->

# IT 140 Projects | GitHub Continuous Integration Guide

This guide explains the GitHub Actions checks used in the IT 140 Projects repository across Modules Five–Seven.

> [!IMPORTANT]
> **GitHub continuous integration (CI) provides feedback. It does not grade or submit a project or milestone.** Students submit the required files in **D2L Brightspace**, and the current D2L Guidelines and Rubrics determine grades.

## About CI

### What CI Means Here

**Continuous integration (CI)** is automated checking that runs after repository changes are saved to GitHub. GitHub Actions provides CI for this repository.

The projects repository separates two purposes:

* **Student CI** gives formative feedback about the progressive Module Five, Module Six, and Module Seven graded checkpoints.
* **Course-repository CI** protects the public starter repository, documentation, starter artifacts, command instructions, and supporting files.

### Important Terms

| Term | Meaning |
| --- | --- |
| **course repository** | `GC-STEM/it140-projects`, the public starter repository maintained for the course |
| **personal repository** | The private `it140-projects` repository a student creates once and continues using through Modules Five–Seven |
| **workflow** | Instructions in `.github/workflows/` that tell GitHub Actions what to run |
| **workflow run** | One execution of a workflow |
| **Project checkpoint check** | The student-facing job that checks repository integrity and the currently active graded checkpoint |
| **Course repository check** | The maintainer-facing job that validates the public projects package |
| **README command checks** | Cross-platform checks for Bash command blocks in README files |
| **advisory Ruff feedback** | Python style/quality suggestions that do not by themselves make student CI fail |

## Student CI

### Progressive Checkpoint Model

Students use one personal repository across three graded checkpoints:

| Checkpoint | Graded files |
| --- | --- |
| **Module Five — Project One** | `design/game_storyboard.md`, `design/game_map.drawio`, `design/move.pseudo`, `design/get_item.pseudo` |
| **Module Six — Milestone** | `prototype/move_between_rooms.py` |
| **Module Seven — Project Two** | `src/text_based_game.py` |

Student CI infers the active checkpoint from which later graded source file has changed.

The progression is cumulative:

1. Once Module Five graded work begins, all four Project One design files are expected to be completed.
2. Once `prototype/move_between_rooms.py` changes, Project One must remain complete and the Module Six prototype must meet its basic structural checks.
3. Once `src/text_based_game.py` changes, Project One and the Module Six milestone must remain complete and Project Two must meet its basic structural checks.

### Fresh Personal Repositories Are Neutral

The starter files are intentionally incomplete. Creating a personal repository is not a student error.

Therefore:

* a brand-new personal repository with no graded-file changes should not fail merely because project work has not started;
* changes only to optional working notes do not start a graded checkpoint; and
* once a graded checkpoint begins, incomplete or damaged required artifacts can produce formative failures.

This behavior avoids a failed GitHub Actions notification immediately after repository setup while preserving useful feedback after work begins.

### What the Project Check Can Verify

Depending on the active checkpoint, student CI can check areas such as:

* required course files remain present;
* committed changes stay within student-editable files;
* required earlier checkpoint files changed from the starter state;
* the Project One Draw.io map remains parseable XML;
* starter TODO prompts are removed from required design files;
* Module Six Python has valid syntax and expected basic movement-program structure;
* Project Two Python has valid syntax and expected basic game-program structure; and
* course-managed documentation and configuration remain intact.

These are structural and completion checks. They do **not** prove:

* that a Project One map is winnable;
* that pseudocode is logically correct;
* that every gameplay path works;
* that Python meets every rubric criterion; or
* that the work has been submitted.

### Advisory Code Style Feedback

When a student changes the Module Six or Module Seven Python source, the workflow can run Ruff on the changed project Python file.

Ruff feedback is **advisory** in student CI. A Ruff suggestion does not by itself make the workflow fail.

Students should still review code readability and current rubric expectations.

### How Students Should Use CI Feedback

A useful workflow is:

> **Work → Run/Test → Commit → Push → Review CI → Improve**

To review feedback:

1. Open the personal `it140-projects` repository on GitHub.
2. Select **Actions**.
3. Open the most recent **IT 140 Checks** workflow run.
4. Open **Project checkpoint check**.
5. Read the summary and the first failing step, if any.
6. Review **Code style feedback** when Python work changed.

A green result is not a grade and does not submit the checkpoint.

## When Something Fails

### Normal Development Feedback

After graded work begins, a failure may indicate:

* only some Project One graded files have changed;
* a required TODO or starter placeholder remains;
* a Draw.io file is damaged;
* a Module Six or Module Seven Python file has a syntax or required-structure problem; or
* a course-managed file was modified, removed, renamed, or added unexpectedly.

Correct one problem, test again, commit and push the correction, and review the new workflow run.

### Possible Repository or CI Problems

A repository or CI problem is more likely when:

* a newly created personal repository fails before any graded file is changed;
* GitHub Actions fails during checkout or Python setup;
* the feedback clearly does not match the files stored in the personal repository; or
* several students report the same infrastructure failure.

Use the support routing in the root [README](../../README.md). Do not post completed graded solutions, credentials, access tokens, or private identifying information in public GitHub Issues or Discussions.

## Faculty Guidance

CI is **formative feedback**, not grading automation.

When helping a student:

* identify which project checkpoint the student is working on;
* use the first reported CI problem to focus troubleshooting;
* remember that Ruff is advisory in student CI;
* use the current D2L Guidelines and Rubric for grading; and
* treat a green workflow as one development signal, not proof of completeness or quality.

If many students encounter the same GitHub Actions setup failure, investigate a repository or platform problem before assuming identical student errors.

## Course Repository CI

### Course Repository Check

[`tests.yml`](../workflows/tests.yml) runs a separate **Course repository check** in `GC-STEM/it140-projects`.

The course job validates areas such as:

* required files and stable documentation sections;
* local Markdown links;
* JSON and TOML configuration;
* Project One Draw.io and reference image integrity;
* course and starter Python syntax;
* Ruff checks for course/starter Python;
* the repository social-preview image; and
* the intentionally incomplete course starter through [`check_starter.py`](./check_starter.py).

[`check_repository.py`](./check_repository.py) contains repository and checkpoint checks shared by course and personal repositories. Student mode changes the checkpoint-completion behavior without weakening protection of course-managed files.

### README Command Checks

[`readme-commands.yml`](../workflows/readme-commands.yml) runs only in the public course repository and validates README command blocks on:

| Environment | Shell |
| --- | --- |
| Linux | Bash |
| macOS | zsh |
| Windows | Git Bash from Git for Windows |

[`check_readme_commands.py`](./check_readme_commands.py) checks every fenced `bash`, `sh`, or `shell` block in README-style documentation for syntax and cross-platform policy violations. It also smoke-tests selected procedural blocks marked with comments such as:

```text
<!-- ci:command-test id=return-existing-work fixture=existing-repo expect=repo -->
```

The smoke tests use disposable directories and harmless command shims. They verify path handling and documented command sequences without creating real GitHub repositories, commits, or VS Code sessions.

The checker rejects patterns that conflict with the course command convention, including:

* Command Prompt `%USERPROFILE%` syntax in Bash blocks;
* PowerShell `$env:` syntax in Bash blocks;
* Windows drive paths in cross-platform Bash blocks;
* backslashes with `~` or `$HOME`; and
* `code ~/Repos/...` instead of `cd ...` followed by `code .`.

### External Link Checks

[`external-links.yml`](../workflows/external-links.yml) protects external links in course-managed Markdown. External sites can fail temporarily; confirm a link is actually stale before replacing it.

## Maintainer Guidance

### Preserve the Student CI Lifecycle

When modifying CI, preserve these states:

1. **Untouched personal starter:** neutral; no failure solely because work has not started.
2. **Optional notes only:** neutral; no graded checkpoint begins.
3. **Module Five begins:** all four Project One graded designs are evaluated together.
4. **Module Six begins:** Project One remains required and the milestone source is evaluated.
5. **Module Seven begins:** Project One and Module Six remain required and the final source is evaluated.
6. **Student Ruff feedback:** advisory only.
7. **Every state:** a green workflow is not a grade or submission.

Do not add the repository's provided Python tests as required student CI unless the project requirements themselves change.

### When Course CI Fails

Fix the cause rather than weakening a check merely to make the workflow green. Confirm whether a change intentionally altered a required file, section marker, editable path, starter artifact, or command sequence.

### When README Command Checks Fail

Run the checker locally from the repository root when the applicable shell is available:

```bash
python3 .github/ci/check_readme_commands.py --shell bash --platform linux
```

On GitHub, review all three matrix jobs because a command can be valid in one shell environment and fail in another.

### Legacy Disabled Workflow

The former `.github/workflows/tests.yml.disabled` file is no longer part of the active CI design and should be deleted. Keeping one clear active workflow reduces confusion for maintainers.

## Summary

Key points:

* One personal repository supports the progressive Module Five → Module Six → Module Seven project sequence.
* A fresh personal repository is neutral until graded work begins.
* Optional working-note changes do not start a graded checkpoint.
* Student CI checks basic repository integrity and checkpoint structure, not rubric quality.
* Ruff feedback for student Python is advisory.
* Course CI protects the starter package, documentation, commands, and configuration.
* README commands are checked on Linux/Bash, macOS/zsh, and Windows/Git Bash.
* D2L Brightspace remains the submission and grading system.
