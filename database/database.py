import sqlite3

from config import DATABASE_PATH


class Database:
    """
    SQLite database manager for InterviewAI.
    """

    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.connection.cursor()

    def initialize(self):
        """
        Create database tables if they don't exist.
        """

        from database.schema import CREATE_TABLE

        self.cursor.execute(CREATE_TABLE)
        self.connection.commit()

    def execute(self, query, values=()):
        """
        Execute INSERT, UPDATE, DELETE queries.
        """

        self.cursor.execute(query, values)
        self.connection.commit()

    def fetchall(self, query, values=()):
        """
        Fetch multiple records.
        """

        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def fetchone(self, query, values=()):
        """
        Fetch a single record.
        """

        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def close(self):
        """
        Close database connection.
        """

        self.connection.close()