<!--
MAINTAINER NOTE:
This filename intentionally contains a Cyrillic capital IE: Е (U+0415)
instead of the ASCII capital E: E (U+0045).

GitHub therefore does not treat it as .github/README.md and it does not
override the repository-root README.
-->

# About the `.github` Folder

> [!IMPORTANT]
> Do **not** modify or delete the `.github/` folder or its files. They support
> repository administration and are not student deliverables.

## What Is Here?

This repository uses `.github/` for GitHub-specific configuration:

- `ISSUE_TEMPLATE/` — forms for reporting repository problems or requesting
  improvements
- `ci/` — validation scripts used by the active Project Checks workflow
- `workflows/tests.yml` — active repository and checkpoint-aware project checks
- `workflows/external-links.yml` — manual and scheduled Markdown link checking
- `workflows/tests.yml.disabled` — intentionally disabled legacy test workflow
- `social-preview.png` — repository social-preview image

These files support the repository itself. They are not graded project files.

## Automated Repository Checks

The active **Project Checks** workflow runs after pushes and pull requests.

In a personal repository, the checks progress with the project sequence:

1. Project One design files
2. Module Six prototype
3. Project Two final source

The workflow validates repository integrity and basic structural requirements.
It does not assign a grade or replace rubric-based review and manual testing.

The **External Links** workflow checks links in Markdown files. Its scheduled
weekly run is limited to the canonical `GC-STEM` course repository so personal
repositories created from the template do not each run a weekly link crawl.

## Issue or Project Question?

Use a GitHub Issue for a technical problem with the provided repository,
documentation, starter files, or course tools.

Do **not** use an Issue to request or post completed graded project solutions.

Questions about requirements, grading, submissions, deadlines,
accommodations, or instructor feedback belong with your instructor in D2L
Brightspace.
