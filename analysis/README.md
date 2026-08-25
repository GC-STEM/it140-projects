# Analyze Phase | Requirements Across Modules Five–Seven

**Project sequence:** [Start Here](../README.md) → **M5 Analyze** →
[M5 Design](../design/README.md) →
[M6 Construct/Test Prototype](../prototype/README.md) →
[M7 Construct](../src/README.md) → [M7 Test](../tests/README.md)

## Purpose

Analysis asks **what the system must do** before you decide how to design or
code it.

The IT 140 text-game project spans three graded activities. The current
Guidelines and Rubric for each activity is the official source of requirements.
The [Software Requirements Specification (SRS)](text_based_game_srs.md)
reorganizes those requirements by checkpoint so you can see what stays the same
and what changes as the project develops.

## The Requirements Grow Across Three Modules

| Module | Question to answer | Result |
| --- | --- | --- |
| 5 | What complete game are you proposing, and how should its two main command processes work? | Project One design |
| 6 | Can you translate the movement idea into a small working Python prototype? | Movement milestone |
| 7 | Can you integrate your complete design into a working, tested game? | Project Two final program |

The Module Six sample does not replace your Project One game requirements. It
reduces the problem temporarily so you can practice construction and testing.

## Module Five | Initial Analysis

Use:

- Project One Guidelines and Rubric in D2L Brightspace
- Sample Dragon Text Game supporting materials
- [Text-Based Game SRS](text_based_game_srs.md), Section 1

Identify the following before designing:

### Game Goal and World

- What must the player collect to win?
- What causes the player to lose?
- What is the minimum number of rooms?
- What is the minimum number of items?
- Which rooms may not contain items?
- What must be true about the map so the game can be won?

### Commands and Program Behavior

The final game needs two command families:

1. **Move between rooms** using north, south, east, or west.
2. **Get an item** from the current room.

For each process, identify:

- Input the player provides
- Validation that must occur
- Decisions the program must make
- Output the player receives
- What behavior repeats

Do not begin with Python syntax. Project One grades the **design**.

## Module Six | Reanalyze the Reduced Scope

Before coding the milestone, return to the requirements and deliberately reduce
the scope.

The milestone includes:

- The provided three-room dragon dictionary
- Current-room output
- Movement commands
- `exit`
- A gameplay loop
- Decision branching
- Input validation
- Debugging and readable code

The milestone intentionally excludes:

- Your Project One room map
- Items and inventory
- A villain
- Final win/loss logic

This reduced scope is a development strategy, not a change to your final game
design.

## Module Seven | Reanalyze Before Integration

Before Project Two, review:

- Project One design files and instructor feedback
- Module Six code and instructor feedback
- Project Two Guidelines and Rubric
- Project Two supporting flowchart/output materials
- [Text-Based Game SRS](text_based_game_srs.md), Section 3

Ask:

- Which Project One design decisions become data in the final dictionary?
- Which movement ideas from the milestone can be reused or adapted?
- Which milestone-only behaviors must be removed or replaced?
- What additional behavior is required for items, inventory, functions,
  winning, and losing?

## Analyze Checkpoint

Before continuing, you should be able to explain this traceability path:

> **Requirements → Project One design → Module Six prototype experience →
> Project Two implementation → testing evidence**

You should also be able to distinguish **course-provided sample data** from
**your own final game data**.

## Help and Support

For supplemental explanations, see the
[IT 140 Projects Wiki](https://github.com/GC-STEM/it140-projects/wiki).

For activity requirements, grading, or feedback, contact your instructor
through D2L Brightspace.

## Next Step

In Module Five, continue to the [Design Phase](../design/README.md).
