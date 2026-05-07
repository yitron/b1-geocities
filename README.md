# B1 Geocities - Legacy Software Modernization Showcase

**A personal homepage combining 90s Geocities design aesthetic with modern Python/Flask/SQLite backend**

## Overview

This project demonstrates **legacy software modernization** - taking the beloved 90s Geocities aesthetic and reimplementing it with modern, maintainable technology. Built using **true Test-Driven Development (TDD)** methodology following the 4D process (DISCOVER → DEFINE → DEVELOP → DELIVER).

**Purpose:** DAI Selection Submission - Prototype B1 (Individual Use Case)

**Approach:** Specification-driven development with RED-GREEN-REFACTOR TDD cycles

## About Me

**Name:** HongZhuang Lim "Z"

**Tagline:** Programmer Saved by Grace

**Scripture:** Ecclesiastes 9:10 (KJV)
> "Whatsoever thy hand findeth to do, do it with thy might;
> for there is no work, nor device, nor knowledge, nor wisdom,
> in the grave, whither thou goest."

**Family:** Married, 2 kids

**Motto:** Less is more

## Features

- **90s Geocities Aesthetic:** Light background, bright neon accents, Comic Sans font
- **Global Hit Counter:** Persistent visitor count stored in SQLite database
- **Guestbook:** Sign and view messages from visitors
- **Under Construction:** Classic 90s web element
- **WCAG AA Accessibility:** Designed with color contrast and semantic HTML
- **Full-Stack Architecture:** Python/Flask backend with SQLite database

## Tech Stack

- **Backend:** Python 3.10+, Flask 3.0
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **Testing:** pytest 7.4+
- **Linting:** Ruff 0.1+

## Installation

### Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/b1-geocities.git
cd b1-geocities

# Run installation (installs dependencies AND runs tests)
./install.sh

# Start the server
./run.sh
```

### Manual Installation

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
python -c "from backend.database import init_db; init_db()"

# Run tests
pytest tests/

# Start server
export FLASK_APP=backend.app:create_app
flask run --port 7878
```

## Usage

### Quick Start (Automated)

1. Run `./install.sh` to set up the environment (creates venv, installs deps, runs tests)
2. Run `./run.sh` to start the server (automatically opens browser)
3. Visit http://localhost:7878 (opens automatically)
4. Enjoy the 90s nostalgia with modern reliability!

**Note:** The scripts automatically activate `venv/` when they run. You don't need to manually activate the venv for normal usage.

### Manual Usage (Interactive)

If you want to run commands manually (e.g., for development):

```bash
# Activate virtual environment
source venv/bin/activate

# Now you can use Python/pip/pytest directly
python --version
pip list
pytest tests/ -v

# Deactivate when done
deactivate
```

## API Endpoints

### Hit Counter

**GET /api/hitcounter**
- Returns: `{"count": <number>}`
- Description: Get current visitor count

**POST /api/hitcounter**
- Returns: `{"count": <number>}`
- Description: Increment visitor count and return new value

### Guestbook (Coming Soon)

**GET /api/guestbook**
- Returns: `{"entries": [...]}`
- Description: Get all guestbook entries

**POST /api/guestbook**
- Body: `{"name": "string", "message": "string"}`
- Returns: `{"id": <number>}`
- Description: Add new guestbook entry

## Testing

The project was built using **true TDD methodology**:

- **RED:** Write failing tests first
- **GREEN:** Write minimal code to pass tests
- **REFACTOR:** Clean up and improve code quality

### Run Tests

```bash
# Run all tests
./test.sh

# Or use pytest directly
python3 -m pytest tests/ -v

# Run specific test files
python3 -m pytest tests/test_backend.py -v
python3 -m pytest tests/test_frontend.py -v
```

### Test Coverage

- **13 tests total** (all passing)
- 2 database tests
- 4 model tests
- 2 Flask API tests
- 5 frontend structure tests

## Project Structure

```
b1-geocities/
├── backend/
│   ├── __init__.py
│   ├── app.py           # Flask application factory
│   ├── database.py      # SQLite database initialization
│   └── models.py        # HitCounter and Guestbook models
├── tests/
│   ├── test_backend.py  # Backend unit tests
│   └── test_frontend.py # Frontend structure tests
├── _archive/            # Previous non-TDD implementation
├── index.html           # Main page (90s Geocities aesthetic)
├── requirements.txt     # Python dependencies
├── install.sh          # Installation script
├── run.sh              # Server startup script
├── test.sh             # Test runner script
├── DEVELOPMENT.md      # Full development journal
├── DEVELOPMENT_APPROACH.md  # Methodology documentation
└── README.md           # This file
```

## Development Approach

This project follows the **4D Methodology**:

1. **DISCOVER** - Requirements gathering and clarification
2. **DEFINE** - Architecture design and test strategy planning
3. **DEVELOP** - TDD implementation (RED-GREEN-REFACTOR)
4. **DELIVER** - Documentation and final polish

See `DEVELOPMENT.md` for the complete development journal with timestamps and decisions.

See `DEVELOPMENT_APPROACH.md` for methodology details and decision logs.

## TDD Cycles Completed

1. ✅ **Database Layer** (2 tests) - SQLite initialization and connection
2. ✅ **Models Layer** (4 tests) - HitCounter and Guestbook models
3. ✅ **Hit Counter API** (2 tests) - Flask endpoints for hit counter
4. ✅ **Frontend HTML** (5 tests) - 90s aesthetic homepage structure

## Why This Approach?

**Legacy Modernization:** Shows ability to respect classic design while applying modern engineering practices

**True TDD:** Tests written BEFORE code, proving specification-driven development

**Simplicity:** "Less is more" - minimal dependencies, clear structure, easy to understand

**Collaboration Quality:** Focus on working code and good documentation over credentials

## License

This project is for DAI selection submission purposes.

## Contact

**HongZhuang Lim "Z"**
- This project demonstrates human-AI collaboration focused on quality over experience
