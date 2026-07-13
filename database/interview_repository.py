from datetime import datetime


class InterviewRepository:
    """
    Repository for saving interview summaries
    into the SQLite database.
    """

    def __init__(self, db):
        self.db = db
    
    def fetch_all(self):
        """
        Fetch all interview records from the database.
        """

        query = """
            SELECT *
            FROM interviews
            ORDER BY id DESC
            """

        return self.db.fetchall(query)

    def save(self, report):

        query = """
        INSERT INTO interviews (

            candidate,
            date,
            topic,
            duration,
            overall_score,
            technical_score,
            communication_score,
            confidence_score,
            recommendation,
            report_path

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        values = (

            report.get("candidate", "Guest"),

            datetime.now().strftime("%Y-%m-%d %H:%M"),

            report.get("topic", "Unknown"),

            report.get("duration", 0),

            report.get("overall_score", 0),

            report.get("technical_score", 0),

            report.get("communication_score", 0),

            report.get("confidence_score", 0),

            report.get("recommendation", "Unknown"),

            report.get("report_path", ""),

        )

        self.db.execute(query, values)