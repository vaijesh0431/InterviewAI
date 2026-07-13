import json
from pathlib import Path
from datetime import datetime

# Directory where interview reports will be stored
OUTPUT_DIR = Path("interview_logs/reports")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def export_json(report):
    """
    Export the interview report as a JSON file.

    Args:
        report (dict): Final interview report.

    Returns:
        Path: Path to the exported JSON file.
    """

    filename = datetime.now().strftime("%Y%m%d_%H%M%S.json")

    filepath = OUTPUT_DIR / filename

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(
            report,
            file,
            indent=4,
            ensure_ascii=False
        )

    return filepath