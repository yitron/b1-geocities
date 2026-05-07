"""
Backend Tests - TDD for B1 Geocities
Test database, models, and Flask app
"""

import pytest
import os
import sys

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from backend.database import init_db, get_db_connection
from backend.models import HitCounter, Guestbook


# Flask app will be imported when it exists
try:
    from backend.app import create_app
except ImportError:
    create_app = None


class TestDatabase:
    """Test database initialization and connection"""

    def test_database_init_creates_file(self):
        """
        RED: Test that init_db creates a database file
        This test should FAIL initially (no init_db function exists)
        """
        # Clean up any existing test db
        test_db = 'test_geocities.db'
        if os.path.exists(test_db):
            os.remove(test_db)

        # Initialize database
        init_db(test_db)

        # Assert database file was created
        assert os.path.exists(test_db), "Database file should be created"

        # Cleanup
        os.remove(test_db)

    def test_database_connection_works(self):
        """
        RED: Test that we can get a database connection
        This test should FAIL initially (no get_db_connection exists)
        """
        test_db = 'test_geocities.db'
        if os.path.exists(test_db):
            os.remove(test_db)

        init_db(test_db)
        conn = get_db_connection(test_db)

        assert conn is not None, "Connection should not be None"

        # Test we can execute a query
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        assert len(tables) > 0, "Should have at least one table"

        conn.close()
        os.remove(test_db)


class TestHitCounter:
    """Test HitCounter model"""

    def test_hit_counter_get_returns_count(self):
        """
        RED: Test that HitCounter.get() returns current count
        Should FAIL - no HitCounter class exists yet
        """
        test_db = 'test_geocities.db'
        if os.path.exists(test_db):
            os.remove(test_db)

        init_db(test_db)
        counter = HitCounter(test_db)

        count = counter.get()
        assert count == 0, "Initial count should be 0"

        os.remove(test_db)

    def test_hit_counter_increment_works(self):
        """
        RED: Test that HitCounter.increment() increases count
        Should FAIL - no increment method exists
        """
        test_db = 'test_geocities.db'
        if os.path.exists(test_db):
            os.remove(test_db)

        init_db(test_db)
        counter = HitCounter(test_db)

        # Increment and verify
        new_count = counter.increment()
        assert new_count == 1, "Count should be 1 after first increment"

        # Increment again
        new_count = counter.increment()
        assert new_count == 2, "Count should be 2 after second increment"

        os.remove(test_db)


class TestGuestbook:
    """Test Guestbook model"""

    def test_guestbook_add_entry(self):
        """
        RED: Test that Guestbook.add_entry() saves message
        Should FAIL - no Guestbook class exists yet
        """
        test_db = 'test_geocities.db'
        if os.path.exists(test_db):
            os.remove(test_db)

        init_db(test_db)
        guestbook = Guestbook(test_db)

        # Add entry
        entry_id = guestbook.add_entry("Test User", "Hello world!")
        assert entry_id > 0, "Should return entry ID"

        os.remove(test_db)

    def test_guestbook_get_all_returns_entries(self):
        """
        RED: Test that Guestbook.get_all() returns all entries
        Should FAIL - no get_all method exists
        """
        test_db = 'test_geocities.db'
        if os.path.exists(test_db):
            os.remove(test_db)

        init_db(test_db)
        guestbook = Guestbook(test_db)

        # Add multiple entries
        guestbook.add_entry("User1", "Message 1")
        guestbook.add_entry("User2", "Message 2")

        # Get all
        entries = guestbook.get_all()
        assert len(entries) == 2, "Should have 2 entries"
        assert entries[0]['name'] == "User1"
        assert entries[1]['message'] == "Message 2"

        os.remove(test_db)


class TestFlaskAPI:
    """Test Flask API endpoints"""

    def test_index_route_returns_html(self):
        """
        Test that GET / returns index.html
        """
        if create_app is None:
            pytest.skip("Flask app not created yet")

        test_db = 'test_geocities.db'
        if os.path.exists(test_db):
            os.remove(test_db)

        init_db(test_db)
        app = create_app(test_db)
        client = app.test_client()

        # GET root
        response = client.get('/')
        assert response.status_code == 200, "Should return 200 OK"
        assert b'<!DOCTYPE html>' in response.data, "Should return HTML"
        assert b'HongZhuang Lim' in response.data, "Should contain user name"

        os.remove(test_db)

    def test_hit_counter_api_get_returns_count(self):
        """
        RED: Test that GET /api/hitcounter returns current count
        Should FAIL - no Flask app exists yet
        """
        if create_app is None:
            pytest.skip("Flask app not created yet")

        test_db = 'test_geocities.db'
        if os.path.exists(test_db):
            os.remove(test_db)

        init_db(test_db)
        app = create_app(test_db)
        client = app.test_client()

        # GET initial count
        response = client.get('/api/hitcounter')
        assert response.status_code == 200, "Should return 200 OK"
        data = response.get_json()
        assert 'count' in data, "Response should contain count"
        assert data['count'] == 0, "Initial count should be 0"

        os.remove(test_db)

    def test_hit_counter_api_post_increments(self):
        """
        RED: Test that POST /api/hitcounter increments count
        Should FAIL - no Flask app exists yet
        """
        if create_app is None:
            pytest.skip("Flask app not created yet")

        test_db = 'test_geocities.db'
        if os.path.exists(test_db):
            os.remove(test_db)

        init_db(test_db)
        app = create_app(test_db)
        client = app.test_client()

        # POST to increment
        response = client.post('/api/hitcounter')
        assert response.status_code == 200, "Should return 200 OK"
        data = response.get_json()
        assert 'count' in data, "Response should contain count"
        assert data['count'] == 1, "Count should be 1 after increment"

        # POST again
        response = client.post('/api/hitcounter')
        data = response.get_json()
        assert data['count'] == 2, "Count should be 2 after second increment"

        os.remove(test_db)

    def test_guestbook_api_get_returns_entries(self):
        """
        RED: Test that GET /api/guestbook returns all entries
        Should FAIL - no guestbook API endpoint exists yet
        """
        if create_app is None:
            pytest.skip("Flask app not created yet")

        test_db = 'test_geocities.db'
        if os.path.exists(test_db):
            os.remove(test_db)

        init_db(test_db)

        # Add some entries directly to database
        guestbook = Guestbook(test_db)
        guestbook.add_entry("Alice", "Hello world!")
        guestbook.add_entry("Bob", "Great site!")

        app = create_app(test_db)
        client = app.test_client()

        # GET all entries
        response = client.get('/api/guestbook')
        assert response.status_code == 200, "Should return 200 OK"
        data = response.get_json()
        assert 'entries' in data, "Response should contain entries"
        assert len(data['entries']) == 2, "Should have 2 entries"
        assert data['entries'][0]['name'] == "Alice"
        assert data['entries'][1]['name'] == "Bob"

        os.remove(test_db)

    def test_guestbook_api_post_creates_entry(self):
        """
        RED: Test that POST /api/guestbook creates new entry
        Should FAIL - no guestbook API endpoint exists yet
        """
        if create_app is None:
            pytest.skip("Flask app not created yet")

        test_db = 'test_geocities.db'
        if os.path.exists(test_db):
            os.remove(test_db)

        init_db(test_db)
        app = create_app(test_db)
        client = app.test_client()

        # POST new entry
        response = client.post('/api/guestbook', json={
            'name': 'Charlie',
            'message': 'Nice page!'
        })
        assert response.status_code == 201, "Should return 201 Created"
        data = response.get_json()
        assert 'id' in data, "Response should contain entry id"
        assert data['id'] > 0, "ID should be positive"

        # Verify entry was created
        guestbook = Guestbook(test_db)
        entries = guestbook.get_all()
        assert len(entries) == 1, "Should have 1 entry"
        assert entries[0]['name'] == 'Charlie'
        assert entries[0]['message'] == 'Nice page!'

        os.remove(test_db)

    def test_guestbook_api_post_validates_required_fields(self):
        """
        RED: Test that POST /api/guestbook validates required fields
        Should FAIL - no validation exists yet
        """
        if create_app is None:
            pytest.skip("Flask app not created yet")

        test_db = 'test_geocities.db'
        if os.path.exists(test_db):
            os.remove(test_db)

        init_db(test_db)
        app = create_app(test_db)
        client = app.test_client()

        # POST without name
        response = client.post('/api/guestbook', json={
            'message': 'Hello'
        })
        assert response.status_code == 400, "Should return 400 Bad Request"
        data = response.get_json()
        assert 'error' in data, "Response should contain error message"

        # POST without message
        response = client.post('/api/guestbook', json={
            'name': 'Dave'
        })
        assert response.status_code == 400, "Should return 400 Bad Request"
        data = response.get_json()
        assert 'error' in data, "Response should contain error message"

        # POST with empty strings
        response = client.post('/api/guestbook', json={
            'name': '',
            'message': ''
        })
        assert response.status_code == 400, "Should return 400 Bad Request"

        os.remove(test_db)
