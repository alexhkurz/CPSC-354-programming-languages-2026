#!/usr/bin/env python3
"""Sync HackMD notes listed in lecture-by-lecture.md into notes-hackmd/."""

import argparse
import re
import subprocess
import sys
from pathlib import Path


GENERIC_LINK_TEXTS = {
    "introduction", "examples", "definitions", "background", "summary",
    "notes", "lecture", "homework", "solution", "exercise", "exercises",
    "overview", "conclusion", "references", "example",
}

GENERIC_TITLE_PATTERNS = [
    re.compile(r"^\s*CPSC-354\s*(?:2026)?\s*[:\-–—]?\s*Homework\s+\d+\s*$", re.IGNORECASE),
    re.compile(r"^\s*Homework\s+\d+\s*$", re.IGNORECASE),
    re.compile(r"^\s*Solution\s+Homework\s+\d+\s*$", re.IGNORECASE),
    re.compile(r"^\s*Lecture\s+\d+\s*$", re.IGNORECASE),
    re.compile(r"^\s*Quiz\s+\d+\s*$", re.IGNORECASE),
]


def repo_root() -> Path:
    # run.py lives in .agents/skills/update-notes-hackmd/
    return Path(__file__).resolve().parents[3]


def normalize_url(url: str) -> str:
    """Return canonical HackMD URL without query, fragment, or trailing slash."""
    return url.split("#")[0].split("?")[0].rstrip("/")


def extract_lecture_links(lecture_path: Path) -> list[tuple[str, str]]:
    """Return [(url, link_text)] for all HackMD links in lecture-by-lecture."""
    text = lecture_path.read_text(encoding="utf-8")
    # Markdown links; link text may span lines.
    pattern = re.compile(r"\[(.*?)\]\((https?://hackmd\.io/[^)\s]+)\)", re.DOTALL)
    found = []
    for m in pattern.finditer(text):
        link_text = " ".join(m.group(1).split())
        url = normalize_url(m.group(2))
        found.append((url, link_text))

    # Any bare HackMD URLs not already inside a markdown link.
    text_no_links = pattern.sub("", text)
    for m in re.finditer(r"https?://hackmd\.io/[^\s)\]]+", text_no_links):
        found.append((normalize_url(m.group(0)), ""))

    # Deduplicate, preserving first appearance.
    seen: set[str] = set()
    result = []
    for url, link_text in found:
        if url not in seen:
            seen.add(url)
            result.append((url, link_text))
    return result


def existing_snapshots(notes_dir: Path) -> tuple[set[str], set[int], set[str]]:
    """Return (existing_urls, used_numbers, existing_slugs)."""
    readme = notes_dir / "README.md"
    existing_urls: set[str] = set()
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        for m in re.finditer(r"\[[^\]]+\]\((https?://hackmd\.io/[^)]+)\)", text):
            existing_urls.add(normalize_url(m.group(1)))

    used_numbers: set[int] = set()
    existing_slugs: set[str] = set()
    for f in notes_dir.glob("[0-9][0-9]-*.md"):
        if f.name == "README.md":
            continue
        m = re.match(r"(\d{2})-(.+)\.md$", f.name)
        if m:
            used_numbers.add(int(m.group(1)))
            existing_slugs.add(m.group(2).lower())
    return existing_urls, used_numbers, existing_slugs


def slugify(text: str, max_words: int = 12) -> str:
    """Create a lowercase hyphenated slug."""
    text = text.lower()
    # keep letters, digits, spaces, hyphens; replace everything else with space
    text = re.sub(r"[^a-z0-9\s-]+", " ", text)
    words = text.split()
    if len(words) > max_words:
        words = words[:max_words]
    return "-".join(words).strip("-")


def informative_link_text(link_text: str) -> bool:
    """True if link text gives a useful short name (not a generic single word)."""
    if not link_text:
        return False
    lt = link_text.strip().lower()
    if lt in GENERIC_LINK_TEXTS:
        return False
    if re.search(r"\d", link_text):
        return True
    if len(lt.split()) > 1:
        return True
    if re.search(r"[A-Z]{2,}", link_text):
        return True
    return False


def title_is_generic(display_title: str) -> bool:
    return any(p.match(display_title) for p in GENERIC_TITLE_PATTERNS)


def derive_slug_and_title(
    url: str, link_text: str, note_text: str
) -> tuple[str, str]:
    """Return (filename_slug, readme_title)."""
    # First # heading in the downloaded note.
    heading = None
    for line in note_text.splitlines():
        m = re.match(r"^#\s+(.+)$", line)
        if m:
            heading = m.group(1).strip()
            break

    # Strip course prefix from heading for display.
    display_title = heading or ""
    if display_title:
        display_title = re.sub(
            r"^\s*CPSC-354\s*(?:2026)?\s*[:\-–—]\s*",
            "",
            display_title,
            flags=re.IGNORECASE,
        ).strip()
        display_title = re.sub(r"^--\s*", "", display_title)

    # Determine slug source.
    if informative_link_text(link_text):
        slug = slugify(link_text)
    elif display_title:
        slug = slugify(display_title)
    else:
        slug = "note"

    if not slug:
        slug = "note"

    # Determine README title.
    if display_title and not title_is_generic(display_title):
        readme_title = display_title
    elif informative_link_text(link_text):
        readme_title = link_text
    elif display_title:
        readme_title = display_title
    else:
        readme_title = "Untitled HackMD note"

    # If the heading is generic (e.g. "Homework 2") but the link text gives an
    # abbreviation like (RT1), append the abbreviation to the title.
    if title_is_generic(display_title) and link_text:
        m = re.search(r"\(([A-Z0-9]{2,})\)", link_text)
        if m:
            abbr = m.group(1)
            if abbr.lower() not in readme_title.lower():
                readme_title = f"{readme_title.strip()} ({abbr})"

    return slug, readme_title


def derive_description(
    url: str, link_text: str, lecture_text: str, note_text: str
) -> str:
    """Try to extract a short description from lecture context or note body."""
    # Find the markdown link in the lecture file and use the rest of the line.
    url_pat = re.escape(url) + r"(?:\?[^)]*)?(?:#[^)]*)?"
    m = re.search(
        r"\[[^\]]+\]\(" + url_pat + r"\)[ \t]*[.,;:.]?[ \t]*([^\n]*)",
        lecture_text,
        re.DOTALL,
    )
    if m:
        rest = m.group(1).strip()
        rest = re.sub(r"^[.,;:\s]+", "", rest)
        rest = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", rest)
        rest = rest.strip(".,;: ")
        if rest:
            return rest

    # Fallback: first non-empty paragraph of the note (after the title).
    lines = note_text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines):
                para = lines[j].strip()
                if para and not para.startswith(("---", ":::", "<!--")):
                    para = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", para)
                    para = re.sub(r"[*_`]+", "", para)
                    return para[:80]
    return ""


def next_number(used: set[int]) -> int:
    for i in range(1, 1000):
        if i not in used:
            return i
    raise RuntimeError("No free note number")


def download_note(url: str) -> str:
    """Download the raw Markdown for a HackMD note."""
    cmd = ["curl", "-fsSL", f"{url}/download"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Failed to download {url}/download: {result.stderr}")
    return result.stdout


def make_unique_slug(slug: str, existing_slugs: set[str]) -> str:
    base = slug
    counter = 2
    while slug.lower() in existing_slugs:
        slug = f"{base}-{counter}"
        counter += 1
    return slug


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sync HackMD notes from lecture-by-lecture.md into notes-hackmd/"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without writing files",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually download and create files",
    )
    args = parser.parse_args()

    root = repo_root()
    lecture = root / "lecture-by-lecture.md"
    notes_dir = root / "notes-hackmd"
    readme = notes_dir / "README.md"

    if not lecture.exists():
        print(f"Error: {lecture} not found", file=sys.stderr)
        sys.exit(1)
    if not notes_dir.exists():
        print(f"Error: {notes_dir} not found", file=sys.stderr)
        sys.exit(1)

    lecture_text = lecture.read_text(encoding="utf-8")
    links = extract_lecture_links(lecture)
    existing_urls, used_numbers, existing_slugs = existing_snapshots(notes_dir)

    new_links = [(url, lt) for url, lt in links if url not in existing_urls]

    if not new_links:
        print("No new HackMD notes to snapshot.")
        return

    if not args.apply:
        print(f"Found {len(new_links)} new note(s). Use --apply to download.")

    next_n = next_number(used_numbers)
    new_entries = []
    for url, link_text in new_links:
        note_text = download_note(url)
        slug, title = derive_slug_and_title(url, link_text, note_text)
        slug = make_unique_slug(slug, existing_slugs)
        description = derive_description(url, link_text, lecture_text, note_text)

        filename = f"{next_n:02d}-{slug}.md"
        existing_slugs.add(slug.lower())
        used_numbers.add(next_n)

        new_entries.append({
            "number": next_n,
            "url": url,
            "title": title,
            "filename": filename,
            "description": description,
            "note_text": note_text,
        })

        print(
            f"  {filename}\n"
            f"    title:       {title}\n"
            f"    url:         {url}\n"
            f"    description: {description[:70]}{'…' if len(description) > 70 else ''}"
        )

        next_n = next_number(used_numbers)

    if args.dry_run or not args.apply:
        if args.dry_run:
            print("Dry run: no files written.")
        return

    # Write files.
    for e in new_entries:
        (notes_dir / e["filename"]).write_text(e["note_text"], encoding="utf-8")
        print(f"Created {e['filename']}")

    # Update README.
    readme_lines = [
        f"{e['number']}. [{e['title']}]({e['url']}) — local file: `{e['filename']}` — {e['description']}"
        for e in new_entries
    ]
    readme_text = readme.read_text(encoding="utf-8") if readme.exists() else "# HackMD notes (PL 2026)\n\n"
    if not readme_text.endswith("\n"):
        readme_text += "\n"
    readme_text += "\n".join(readme_lines) + "\n"
    readme.write_text(readme_text, encoding="utf-8")
    print(f"Updated {readme}")


if __name__ == "__main__":
    main()
