#!/bin/bash
# install.sh - Install dependencies and run tests for B1 Geocities

set -e  # Exit on error

echo "===== B1 Geocities Installation ====="
echo

# Check Python version
echo "Checking Python version..."
python3 --version
echo

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi
echo

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo

# Install dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt
echo "✅ Dependencies installed"
echo

# Initialize database
echo "Initializing database..."
python -c "from backend.database import init_db; init_db(); print('✅ Database initialized')"
echo

# Run tests
echo "Running tests..."
pytest tests/ -v
echo

echo "===== Installation Complete ====="
echo "Run ./run.sh to start the server"
