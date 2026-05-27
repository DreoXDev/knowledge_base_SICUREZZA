from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def is_ignored(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return rel.parts[0] in {"99_Archive", "plans"} or rel.as_posix() == "README.md"

md_files = sorted(p for p in ROOT.rglob("*.md") if not is_ignored(p))
note_names = {p.stem: p for p in md_files}
relative_paths = {p.relative_to(ROOT).as_posix(): p for p in md_files}
relative_no_ext = {p.relative_to(ROOT).with_suffix("").as_posix(): p for p in md_files}

broken = []
todos = []
orphans = []

link_re = re.compile(r"\[\[([^\]|#]+)")
todo_re = re.compile(r"\b(TODO|da completare)\b", re.IGNORECASE)

linked = set()

for path in md_files:
    text = path.read_text(encoding="utf-8", errors="replace")
    for match in link_re.finditer(text):
        target = match.group(1).strip()
        linked.add(target)
        if target in note_names or target in relative_paths or target in relative_no_ext:
            continue
        broken.append((path.relative_to(ROOT).as_posix(), target))
    for i, line in enumerate(text.splitlines(), 1):
        if todo_re.search(line):
            todos.append((path.relative_to(ROOT).as_posix(), i, line.strip()))

for path in md_files:
    if path.parts[-2:] == ("00_Project", "Final_Audit_Report.md"):
        continue
    if path.stem not in linked and path.relative_to(ROOT).as_posix() not in linked and path.relative_to(ROOT).with_suffix("").as_posix() not in linked:
        if path.relative_to(ROOT).parts[0] not in {"00_Project", "01_Raw_Assets", "99_Archive", "scripts"}:
            orphans.append(path.relative_to(ROOT).as_posix())

report = []
report.append("# Vault Check Report")
report.append("")
report.append(f"Markdown files: {len(md_files)}")
report.append(f"Broken links: {len(broken)}")
report.append(f"TODO/da completare/da verificare lines: {len(todos)}")
report.append(f"Potential orphan notes: {len(orphans)}")
report.append("")

report.append("## Broken links")
if broken:
    for file, target in broken:
        report.append(f"- `{file}` -> `[[{target}]]`")
else:
    report.append("- None")
report.append("")

report.append("## TODO-like lines")
if todos:
    for file, line, text in todos[:100]:
        report.append(f"- `{file}:{line}` {text}")
    if len(todos) > 100:
        report.append(f"- ... {len(todos) - 100} more")
else:
    report.append("- None")
report.append("")

report.append("## Potential orphan notes")
if orphans:
    for file in orphans:
        report.append(f"- `{file}`")
else:
    report.append("- None")

out = ROOT / "06_Exports" / "final_audit_report.txt"
out.parent.mkdir(exist_ok=True)
out.write_text("\n".join(report) + "\n", encoding="utf-8")
print("\n".join(report))
