import sqlite3


def create_tables(conn):
    conn.execute("""
    CREATE TABLE students (
    name varchar(20),
    age INTEGER,
    city TEXT
    )
    """)