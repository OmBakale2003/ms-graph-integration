import csv
from datetime import datetime
from pathlib import Path

def json_to_csv(rows) -> str:
    if not rows:
        print("No data found in Graph response")
        return ""

    # Build filename with timestamp
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    out_dir = Path("test_scripts") / "graph_test_output"
    out_dir.mkdir(parents=True, exist_ok=True)
    filename = out_dir / f"graph_users_{timestamp}.csv"

    # Collect ALL possible keys across users
    all_keys = set()
    for row in rows:
        all_keys.update(row.keys())

    fieldnames = sorted(all_keys)

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for row in rows:
            writer.writerow(row)

    print(f"CSV created successfully: {filename}")
    return str(filename)