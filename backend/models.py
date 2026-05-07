"""
Data models for B1 Geocities
HitCounter and Guestbook models
"""

from backend.database import get_db_connection


class HitCounter:
    """Model for managing global hit counter"""

    def __init__(self, db_path='geocities.db'):
        """Initialize HitCounter with database path"""
        self.db_path = db_path

    def get(self):
        """
        Get current hit counter value

        Returns:
            int: Current count
        """
        conn = get_db_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT count FROM hit_counter WHERE id = 1')
        result = cursor.fetchone()
        conn.close()
        return result['count'] if result else 0

    def increment(self):
        """
        Increment hit counter by 1

        Returns:
            int: New count value
        """
        conn = get_db_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE hit_counter
            SET count = count + 1,
                last_updated = CURRENT_TIMESTAMP
            WHERE id = 1
        ''')
        conn.commit()

        # Get new count
        cursor.execute('SELECT count FROM hit_counter WHERE id = 1')
        result = cursor.fetchone()
        new_count = result['count']

        conn.close()
        return new_count


class Guestbook:
    """Model for managing guestbook entries"""

    def __init__(self, db_path='geocities.db'):
        """Initialize Guestbook with database path"""
        self.db_path = db_path

    def add_entry(self, name, message):
        """
        Add a new guestbook entry

        Args:
            name: Visitor name
            message: Visitor message

        Returns:
            int: ID of inserted entry
        """
        conn = get_db_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO guestbook (name, message) VALUES (?, ?)',
            (name, message)
        )
        conn.commit()
        entry_id = cursor.lastrowid
        conn.close()
        return entry_id

    def get_all(self):
        """
        Get all guestbook entries (newest first)

        Returns:
            list: List of entry dictionaries
        """
        conn = get_db_connection(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, name, message, timestamp
            FROM guestbook
            ORDER BY timestamp DESC
        ''')
        entries = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return entries
