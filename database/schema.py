CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS interviews (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    candidate TEXT,

    date TEXT,

    topic TEXT,

    duration REAL,

    overall_score REAL,

    technical_score REAL,

    communication_score REAL,

    confidence_score REAL,

    recommendation TEXT,

    report_path TEXT

);
"""