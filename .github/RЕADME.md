<!--
MAINTAINER NOTE:
This filename intentionally contains a Cyrillic capital IE: Е (U+0415)
instead of the ASCII capital E: E (U+0045).

It is visually similar to README.md, but GitHub does not treat it as the
special .github/README.md file that would override the repository-root README.

Do not "correct" the filename unless this behavior is no longer desired.
-->

# About the `.github` Folder

> [!IMPORTANT]
> Do **not** modify or delete the `.github/` folder or any files in it. This
> folder is for repository administration. It is not part of the student
> procedures or graded deliverables for the projects.

## What Is Here?

This repository uses `.github/` for GitHub-specific configuration:

- `ISSUE_TEMPLATE/` — forms for reporting a repository problem or requesting
  an improvement
- `ci/README.md` — CI guidance for students, faculty, and maintainers
- `ci/check_repository.py` — repository and progressive project-checkpoint
  validation
- `ci/check_starter.py` — validates the intentionally incomplete course starter
- `ci/check_readme_commands.py` — validates cross-platform README command blocks
- `workflows/tests.yml` — active **IT 140 Checks** workflow
- `workflows/readme-commands.yml` — Linux, macOS, and Windows/Git Bash README
  command checks for the public course repository
- `workflows/external-links.yml` — external-link checks
- `social-preview.png` — the repository social-preview image

The former `workflows/tests.yml.disabled` file is no longer part of the CI
design and should be removed.

## Automated Repository Checks

The active checks have different purposes:

### Personal Student Repositories

The student-facing **Project checkpoint check** provides limited formative
feedback for the progressive Module Five → Module Six → Module Seven sequence.

A newly created personal repository is a neutral state. The workflow does not
treat untouched graded starter files as a student error. Once graded work
begins, the active checkpoint can report incomplete required artifacts,
damaged starter structure, Python syntax/structure problems, or unexpected
changes to course-managed files.

For Module Six and Module Seven Python work, Ruff feedback is advisory and does
not by itself make student CI fail.

### Public Course Repository

The course repository uses separate checks to protect the full starter package,
including documentation, starter artifacts, Python files, configuration, README
command blocks, and external links.

For the detailed CI lifecycle and maintainer guidance, see
[`ci/README.md`](ci/README.md).

## Issue or Project Question?

Use a GitHub Issue for a technical problem with the provided repository,
documentation, starter files, or automated checks.

Do **not** use an Issue to request or post a completed graded solution.

Codio Virtual Desktop performance, access, or outage problems belong with the
IT Service Desk. Course IDE setup and lifecycle-script problems use the Module
One setup support guidance.

Questions about project requirements, grading, submissions, deadlines,
accommodations, or instructor feedback belong with your instructor in D2L
Brightspace.

For additional information about the `.github` folder, see the
[Module One Setup Tasks `.github` README](https://github.com/GC-STEM/it140-m1-setup-tasks/blob/main/.github/R%D0%95ADME.md).
