---
name: update-notes-hackmd
description: Sync new HackMD notes from lecture-by-lecture.md into the notes-hackmd/ snapshot folder.
allowed-tools:
  - read
  - exec
  - edit
  - write
permissions:
  allow:
    - Read(lecture-by-lecture.md)
    - Read(notes-hackmd/**)
    - Write(notes-hackmd/**)
    - Exec(python3 .agents/skills/update-notes-hackmd/run.py)
    - Exec(git status)
    - Exec(git diff)
    - Exec(git add)
---

Sync HackMD notes listed in `lecture-by-lecture.md` but not yet present in `notes-hackmd/`.

The companion script `.agents/skills/update-notes-hackmd/run.py` does the heavy lifting:

1. **Preview** what would be downloaded:
   ```bash
   python3 .agents/skills/update-notes-hackmd/run.py --dry-run
   ```
2. **Apply** the sync:
   ```bash
   python3 .agents/skills/update-notes-hackmd/run.py --apply
   ```
3. **Review** the generated `notes-hackmd/<NN>-<slug>.md` filename and the new `notes-hackmd/README.md` entry. If a slug is poor, rename the file and update the README line by hand. Do **not** hand-edit the snapshot body — edit on HackMD and re-download.
4. Check `git status` and, when ready, stage and commit with a short lowercase message such as `notes-hackmd: add hw3 (rt2)`.

What the script does:

- Parses `lecture-by-lecture.md` for `https://hackmd.io/...` URLs.
- Skips URLs already listed in `notes-hackmd/README.md`.
- Downloads the raw Markdown via `curl -fsSL <url>/download`.
- Picks the next unused two-digit number.
- Derives a short lowercase hyphenated slug from the link text (preferring informative text like `hw3 (RT2)`) or from the note's `#` heading.
- Saves the snapshot as `notes-hackmd/<NN>-<slug>.md`.
- Appends an entry to `notes-hackmd/README.md` in the existing format:
  `N. [Title](<hackmd-url>) — local file: \`<NN>-<slug>.md\` — <short description>`.

If no new URLs are found, the script prints `No new HackMD notes to snapshot.`
