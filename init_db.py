#!/usr/bin/env python3
import sqlite3


if __name__ == '__main__':
    db_name = 'auth.db'
    conn = sqlite3.connect(db_name)

    print(f'\nCreating "{db_name}"...')
    c = conn.cursor()
    query_drop = 'DROP TABLE IF EXISTS "TBLUSER";'

    query_create = """
    CREATE TABLE "TBLUSER" (
        "USERNAME"	TEXT NOT NULL UNIQUE PRIMARY KEY,
        "IS_ACTIVE"	INTEGER DEFAULT 0,
        "IS_ADMIN"	INTEGER DEFAULT 0,
        "PASSWORD"	TEXT,
        "FK_ROLE" TEXT
        
    );
    """
    c.execute(query_drop)
    c.execute(query_create)
    conn.commit()
    conn.close()
    print(f'\nNew SQLite db - "{db_name}" has been created!!!\n')