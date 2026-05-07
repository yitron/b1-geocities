#!/bin/bash
# run.sh - Start B1 Geocities Flask server

set -e  # Exit on error

echo "===== Starting B1 Geocities Server ====="
echo

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run ./install.sh first"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Check if database exists
if [ ! -f "geocities.db" ]; then
    echo "Database not found. Initializing..."
    python -c "from backend.database import init_db; init_db()"
    echo "✅ Database initialized"
fi

# Start Flask server
echo "Starting Flask server on http://localhost:7878"
echo "Opening browser in 2 seconds..."
echo "Press Ctrl+C to stop"
echo

export FLASK_APP=backend.app:create_app
export FLASK_ENV=development

# Open browser after Flask starts (run in background)
(sleep 2 && open http://localhost:7878) &

# Start Flask server (foreground)
flask run --port 7878
