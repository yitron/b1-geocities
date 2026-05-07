"""
Flask Application for B1 Geocities
API endpoints for hit counter and guestbook
"""

from flask import Flask, jsonify, request, send_from_directory
from backend.models import HitCounter, Guestbook
from backend.database import init_db
import os


def create_app(db_path='geocities.db'):
    """
    Create and configure Flask application

    Args:
        db_path: Path to SQLite database

    Returns:
        Flask app instance
    """
    app = Flask(__name__)
    app.config['DATABASE'] = db_path

    # Initialize database
    init_db(db_path)

    @app.route('/')
    def index():
        """Serve the main index.html page"""
        # Get the project root directory (one level up from backend/)
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return send_from_directory(root_dir, 'index.html')

    @app.route('/api/hitcounter', methods=['GET'])
    def get_hitcounter():
        """Get current hit counter value"""
        counter = HitCounter(app.config['DATABASE'])
        count = counter.get()
        return jsonify({'count': count})

    @app.route('/api/hitcounter', methods=['POST'])
    def increment_hitcounter():
        """Increment hit counter and return new value"""
        counter = HitCounter(app.config['DATABASE'])
        count = counter.increment()
        return jsonify({'count': count})

    @app.route('/api/guestbook', methods=['GET'])
    def get_guestbook():
        """Get all guestbook entries"""
        guestbook = Guestbook(app.config['DATABASE'])
        entries = guestbook.get_all()
        return jsonify({'entries': entries})

    @app.route('/api/guestbook', methods=['POST'])
    def post_guestbook():
        """Add new guestbook entry"""
        data = request.get_json()

        # Validate required fields
        if not data:
            return jsonify({'error': 'Request body required'}), 400

        name = data.get('name', '').strip()
        message = data.get('message', '').strip()

        if not name:
            return jsonify({'error': 'Name is required'}), 400
        if not message:
            return jsonify({'error': 'Message is required'}), 400

        # Add entry to database
        guestbook = Guestbook(app.config['DATABASE'])
        entry_id = guestbook.add_entry(name, message)

        return jsonify({'id': entry_id}), 201

    return app
