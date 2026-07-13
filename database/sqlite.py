import sqlite3
import os


class JobDatabase:
    def __init__(self, db_path="database/jobs.db"):
        os.makedirs("database", exist_ok=True)

        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company TEXT,
                title TEXT,
                location TEXT,
                url TEXT UNIQUE
            )
        """)

        self.conn.commit()

    def save(self, job):
        try:
            self.cursor.execute(
                """
                INSERT INTO jobs(company, title, location, url)
                VALUES (?, ?, ?, ?)
                """,
                (
                    job.company,
                    job.title,
                    job.location,
                    job.apply_link,
                ),
            )
            self.conn.commit()
            return True

        except sqlite3.IntegrityError:
            return False