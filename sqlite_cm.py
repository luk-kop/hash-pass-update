import sqlite3


class UseDatabase:
    """
    Context manager for SQLite db connection.
    """
    def __init__(self, db_config: dict) -> None:
        self.db_config = db_config

    def __enter__(self) -> 'cursor':
        self.conn = sqlite3.connect(**self.db_config)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()