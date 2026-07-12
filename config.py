from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

LOG_DIR = BASE_DIR / "interview_logs"

DATABASE_PATH = BASE_DIR / "database" / "history.db"

APP_NAME = "InterviewAI"

VERSION = "1.0.0"

AUTHOR = "Vaijesh Sindpure"

OLLAMA_MODEL = "llama3.1:8b"

RECORD_DURATION = 8

WHISPER_MODEL = "base"

INTERVIEW_QUESTIONS = 5

RECORD_DURATION = 15

MAX_FOLLOWUPS = 2