"""
Database initialization and connection for B1 Geocities
SQLite database with hit_counter and guestbook tables
"""

import sqlite3


def init_db(db_path='geocities.db'):
    """
    Initialize SQLite database with required tables

    Args:
        db_path: Path to database file

    Returns:
        None
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create hit_counter table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hit_counter (
            id INTEGER PRIMARY KEY,
            count INTEGER NOT NULL DEFAULT 0,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create guestbook table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS guestbook (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Initialize hit counter if not exists
    cursor.execute('INSERT OR IGNORE INTO hit_counter (id, count) VALUES (1, 0)')

    conn.commit()
    conn.close()


def get_db_connection(db_path='geocities.db'):
    """
    Get a database connection

    Args:
        db_path: Path to database file

    Returns:
        sqlite3.Connection object
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn
