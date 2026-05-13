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

# Detect platform and set Python path
if [ -f "venv/bin/python" ]; then
    # Linux/macOS
    PYTHON="venv/bin/python"
    FLASK="venv/bin/flask"
elif [ -f "venv/Scripts/python.exe" ]; then
    # Windows (Git Bash/MSYS)
    PYTHON="venv/Scripts/python.exe"
    FLASK="venv/Scripts/flask.exe"
else
    echo "❌ Could not find Python in virtual environment"
    exit 1
fi

# Check if database exists
if [ ! -f "geocities.db" ]; then
    echo "Database not found. Initializing..."
    $PYTHON -c "from backend.database import init_db; init_db()"
    echo "✅ Database initialized"
fi

# Start Flask server
echo "Starting Flask server on http://localhost:7878"
echo "Opening browser in 2 seconds..."
echo "Press Ctrl+C to stop"
echo

export FLASK_APP=backend.app:create_app
export FLASK_ENV=development

# Detect browser opener command
if command -v open &> /dev/null; then
    BROWSER_CMD="open"  # macOS
elif command -v xdg-open &> /dev/null; then
    BROWSER_CMD="xdg-open"  # Linux
elif command -v start &> /dev/null; then
    BROWSER_CMD="start"  # Windows
else
    BROWSER_CMD=""
fi

# Open browser after Flask starts (run in background)
if [ -n "$BROWSER_CMD" ]; then
    (sleep 2 && $BROWSER_CMD http://localhost:7878) &
fi

# Start Flask server (foreground)
$FLASK run --port 7878
