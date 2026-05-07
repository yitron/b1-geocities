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

    return app
