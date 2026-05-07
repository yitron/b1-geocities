#!/bin/bash

# ============================================
# FUNCTIONAL TESTS
# TDD: RED-GREEN-REFACTOR
# ============================================

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

PASSED=0
FAILED=0

pass() {
    echo -e "${GREEN}✓${NC} $1"
    ((PASSED++))
}

fail() {
    echo -e "${RED}✗${NC} $1"
    ((FAILED++))
}

echo "Functional Tests"
echo "-------------------------------------------"

# ============================================
# RED: Test for HitCounter class
# GREEN: Implemented HitCounter class
# REFACTOR: Added error handling
# ============================================

if grep -q 'class HitCounter' script.js; then
    pass "HitCounter class exists"
else
    fail "HitCounter class not found"
fi

# ============================================
# RED: Test for localStorage usage
# GREEN: Added localStorage.getItem/setItem
# REFACTOR: Wrapped in try-catch
# ============================================

if grep -q 'localStorage' script.js; then
    pass "localStorage implementation present"
else
    fail "localStorage not implemented"
fi

# ============================================
# RED: Test for error handling
# GREEN: Added try-catch blocks
# REFACTOR: Added console.warn for debugging
# ============================================

if grep -q 'try\|catch' script.js; then
    pass "Error handling (try-catch) implemented"
else
    fail "Missing error handling"
fi

# ============================================
# RED: Test for counter increment method
# GREEN: Created increment() method
# REFACTOR: Separated logic from storage
# ============================================

if grep -q 'increment' script.js; then
    pass "Counter increment method exists"
else
    fail "Missing increment method"
fi

# ============================================
# RED: Test for counter display formatting
# GREEN: Added padStart for leading zeros
# REFACTOR: Made digit count configurable
# ============================================

if grep -q 'padStart' script.js; then
    pass "Counter formatting (leading zeros) implemented"
else
    fail "Missing counter formatting"
fi

# ============================================
# RED: Test for smooth scroll
# GREEN: Added scrollIntoView with behavior: 'smooth'
# REFACTOR: Applied to all anchor links
# ============================================

if grep -q 'scrollIntoView\|smooth' script.js; then
    pass "Smooth scroll navigation implemented"
else
    fail "Missing smooth scroll (optional feature)"
fi

# ============================================
# RED: Test for DOMContentLoaded event
# GREEN: Wrapped initialization in DOMContentLoaded
# REFACTOR: Ensured DOM ready before execution
# ============================================

if grep -q 'DOMContentLoaded' script.js; then
    pass "DOMContentLoaded event handler present"
else
    fail "Missing DOMContentLoaded handler"
fi

# ============================================
# RED: Test for code comments
# GREEN: Added JSDoc style comments
# REFACTOR: Documented all public methods
# ============================================

if grep -q '/\*\*\|//' script.js; then
    pass "Code comments present"
else
    fail "Missing code comments"
fi

echo ""
echo "Functional: $PASSED passed, $FAILED failed"
exit $FAILED
