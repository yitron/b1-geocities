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

    # Check if venv module is available
    if python3 -m venv --help &> /dev/null; then
        # Try to use built-in venv
        if python3 -m venv venv 2>/dev/null; then
            echo "✅ Virtual environment created"
        else
            # venv failed (likely ensurepip issue), try without pip
            echo "⚠️  ensurepip not available, creating venv without pip..."
            python3 -m venv --without-pip venv

            # Manually install pip into the venv
            echo "Installing pip into virtual environment..."

            # Detect venv Python path
            if [ -f "venv/bin/python" ]; then
                VENV_PYTHON="venv/bin/python"
            elif [ -f "venv/Scripts/python.exe" ]; then
                VENV_PYTHON="venv/Scripts/python.exe"
            else
                echo "❌ Could not find Python in virtual environment"
                exit 1
            fi

            if command -v curl &> /dev/null; then
                curl -sS https://bootstrap.pypa.io/get-pip.py | $VENV_PYTHON
            elif command -v wget &> /dev/null; then
                wget -qO- https://bootstrap.pypa.io/get-pip.py | $VENV_PYTHON
            else
                echo "❌ Error: curl or wget required to install pip"
                echo "Please install curl: your package manager may have it"
                exit 1
            fi

            echo "✅ Virtual environment created and pip installed"
        fi
    else
        # venv not available, try virtualenv
        echo "⚠️  Python venv module not found, checking for virtualenv..."

        if ! python3 -m virtualenv --help &> /dev/null; then
            echo "Installing virtualenv package..."
            python3 -m pip install --user virtualenv
        fi

        python3 -m virtualenv venv
        echo "✅ Virtual environment created using virtualenv"
    fi
else
    echo "✅ Virtual environment already exists"
fi
echo

# Detect platform and set paths to venv executables
if [ -f "venv/bin/python" ]; then
    # Linux/macOS
    PYTHON="venv/bin/python"
    PIP="venv/bin/pip"
    PYTEST="venv/bin/pytest"
elif [ -f "venv/Scripts/python.exe" ]; then
    # Windows (Git Bash/MSYS)
    PYTHON="venv/Scripts/python.exe"
    PIP="venv/Scripts/pip.exe"
    PYTEST="venv/Scripts/pytest.exe"
else
    echo "❌ Could not find Python in virtual environment"
    exit 1
fi

echo "✅ Using Python from: $PYTHON"
echo

# Install dependencies
echo "Installing dependencies..."
$PIP install -q -r requirements.txt
echo "✅ Dependencies installed"
echo

# Initialize database
echo "Initializing database..."
$PYTHON -c "from backend.database import init_db; init_db(); print('✅ Database initialized')"
echo

# Run tests
echo "Running tests..."
$PYTEST tests/ -v
echo

echo "===== Installation Complete ====="
echo "Run ./run.sh to start the server"
