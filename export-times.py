import os
from datetime import datetime
from collections import defaultdict

logbook = "Logbook"
rows = []

for filename in sorted(os.listdir(logbook)):
    if not filename.endswith(".md"): continue
    date = filename[:-3]  # 2025-11-19

    with open(os.path.join(logbook, filename), "r", encoding="utf-8") as f:
        for line in f:
            if "→" not in line: continue
            if not line.strip().startswith("-"): continue

            parts = line.split("→")
            if len(parts) != 2: continue

            time_part = parts[0].strip().lstrip("- ").split("–")  # start–end
            if len(time_part) != 2: continue
            start, end = time_part[0].strip(), time_part[1].strip()

            tags = parts[1].strip().split()
            students = [t for t in tags if t.startswith("#") and t[1:].isalpha()]
            subjects = [t for t in tags if t.startswith("#") and t[1:].isalpha() and t not in students]

            notes_start = line.find(parts[1]) + len(parts[1])
            notes = line[notes_start:].strip()
            if notes.startswith("#"): notes = ""  # next tag line

            for student in students:
                for subject in subjects:
                    rows.append({
                        "date": date,
                        "student": student[1:],
                        "subject": subject[1:],
                        "start": start,
                        "end": end,
                        "notes": notes
                    })

# Write CSV
import csv
with open("homeschool-time-report.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["date","student","subject","start","end","notes"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Exported {len(rows)} rows to homeschool-time-report.csv")
