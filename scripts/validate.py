#!/usr/bin/env python3
"""Validate every skills/*/SKILL.md against the repo's format standards."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SECTIONS = ["## Purpose", "## Key Concepts", "## Application",
            "## Examples", "## Common Pitfalls", "## References"]
TYPES = {"component", "interactive", "workflow"}

errors = []
skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
for path in skills:
    folder = path.parent.name
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{folder}: missing frontmatter")
        continue
    fm = dict(line.split(":", 1) for line in m.group(1).splitlines() if ":" in line)
    fm = {k.strip(): v.strip() for k, v in fm.items()}
    if fm.get("name") != folder:
        errors.append(f"{folder}: name '{fm.get('name')}' does not match folder")
    if len(fm.get("name", "")) > 64:
        errors.append(f"{folder}: name over 64 characters")
    desc = fm.get("description", "")
    if not desc.startswith("Use when"):
        errors.append(f"{folder}: description must start with 'Use when'")
    if len(desc) > 200:
        errors.append(f"{folder}: description is {len(desc)} chars (max 200)")
    if fm.get("type") not in TYPES:
        errors.append(f"{folder}: type must be one of {sorted(TYPES)}")
    if not fm.get("intent"):
        errors.append(f"{folder}: missing intent")
    positions = [text.find(s + "\n") for s in SECTIONS]
    for s, pos in zip(SECTIONS, positions):
        if pos == -1:
            errors.append(f"{folder}: missing section '{s}'")
    found = [p for p in positions if p != -1]
    if found != sorted(found):
        errors.append(f"{folder}: sections out of order")
    if "—" in text:
        errors.append(f"{folder}: contains an em dash")

print(f"Checked {len(skills)} skills.")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print("All skills valid.")
