from pathlib import Path
import json

DATA_DIR = Path("data")

class QuestionLoader:

    @staticmethod
    def load(topic):

        filepath = DATA_DIR / f"{topic}.json"

        if not filepath.exists():
            raise FileNotFoundError(f"{filepath} not found.")

        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)