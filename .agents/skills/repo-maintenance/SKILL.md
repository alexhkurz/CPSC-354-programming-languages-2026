---
name: repo-maintenance
description: Maintenance conventions for the CPSC-354 Programming Languages (2026) repo — file layout, naming, prose style, notes-hackmd snapshot workflow, LaTeX builds, and git workflow. Use when editing, adding, or reorganizing files in this repository.
---

# Repo maintenance — CPSC-354 Programming Languages (2026)

Public course repository. Canonical course content (syllabus, lecture notes,
assignments, shared resources) lives here. Drafts and not-yet-released material
(quizzes, solutions) belong in the private sister repo
`CPSC-354-programming-languages-2026-private` until administered.

## General conventions

- Prefer US spelling in course prose.
- Keep the lecture-by-lecture index (`lecture-by-lecture.md`) in sync when
  adding or renaming course materials — it is the table of contents.
- Filenames: lowercase, hyphen-separated (`syllabus-long.md`,
  `lecture-by-lecture.md`).
- Do not commit build artifacts (`.aux`, `.log`, `.fdb_latexmk`, `.fls`) or
  `.DS_Store`; check `.gitignore` first.
- Commit messages are short and lowercase-ish (e.g. `quiz 1`, `30min, ...`);
  match the style of `git log`.

## LaTeX

- Build with `pdflatex -interaction=nonstopmode <file>.tex` from the file's
  directory; commit the regenerated `.pdf` together with the `.tex` source.

## Maintaining `notes-hackmd/`

`notes-hackmd/` stores local Markdown snapshots of HackMD notes, numbered
`NN-name.md` (`01-…`, `02-…`, …). The folder exists for backup and offline
processing; HackMD remains the editable source.

When adding a new HackMD note:

1. Download the raw markdown:
   ```bash
   curl -sL "<hackmd-url>/download" -o notes-hackmd/<NN>-<slug>.md
   ```
   Appending `/download` to a HackMD URL returns the raw Markdown.
2. Pick `<NN>` as the next unused two-digit number and `<slug>` as a short
   lowercase hyphenated title (check the note's `#` heading).
3. Add a numbered entry to `notes-hackmd/README.md` in the existing format:
   `N. [Title](<hackmd-url>) — local file: \`NN-slug.md\` — <short description>`.
   The link target must be the HackMD URL, never a relative path into the
   local repo — the README at `notes-hackmd/README.md` says
   "read on HackMD", and the local files are backup snapshots only.
4. Links to the note elsewhere in the repo (e.g. `lecture-by-lecture.md`)
   likewise point to the HackMD URL.

When refreshing an existing note, re-download to the same filename (the local
copy is a snapshot; do not hand-edit it — edit on HackMD and re-download).

## Cross-assistant notes

- This file is the single source of truth for maintenance rules. Do not
  duplicate it under `.devin/` or `.cursor/`; those locations only contain
  pointers here.
- `AGENTS.md` at the repo root points here for assistants that read it.
