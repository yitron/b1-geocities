#!/bin/bash
# test.sh - Aggregated test runner for B1 Geocities

set -e  # Exit on error

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo "=========================================="
echo "B1 GEOCITIES - TEST RUNNER"
echo "=========================================="
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run ./install.sh first"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Run all pytest tests
echo "Running pytest tests..."
pytest tests/ -v

# Check exit code
if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ All tests passed!${NC}"
    echo ""
    echo "To start the server, run:"
    echo "  ./run.sh"
    exit 0
else
    echo ""
    echo -e "${RED}❌ Some tests failed${NC}"
    exit 1
fi
