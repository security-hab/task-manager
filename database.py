import sqlite3


def connectDB(dbName="users.db"):
    conn = sqlite3.connect(dbName)
    return conn


def createTables(conn):
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
    )"""
    )
    conn.commit()


def closeDB(conn):
    conn.close()
