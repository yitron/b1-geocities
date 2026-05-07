#!/bin/bash

# ============================================
# HTML VALIDATION TESTS
# TDD: RED-GREEN-REFACTOR
# ============================================

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
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

echo "HTML Validation Tests"
echo "-------------------------------------------"

# ============================================
# RED: Test for HTML5 doctype
# GREEN: Added <!DOCTYPE html> to index.html
# REFACTOR: Ensured proper capitalization
# ============================================

if grep -q "<!DOCTYPE html>" index.html; then
    pass "HTML5 doctype present"
else
    fail "Missing HTML5 doctype"
fi

# ============================================
# RED: Test for language attribute
# GREEN: Added <html lang="en">
# REFACTOR: Used proper language code
# ============================================

if grep -q '<html lang=' index.html; then
    pass "HTML lang attribute present"
else
    fail "Missing HTML lang attribute"
fi

# ============================================
# RED: Test for character encoding
# GREEN: Added <meta charset="UTF-8">
# REFACTOR: Placed in correct head order
# ============================================

if grep -q '<meta charset=' index.html; then
    pass "Character encoding declared"
else
    fail "Missing character encoding"
fi

# ============================================
# RED: Test for viewport meta tag
# GREEN: Added viewport meta for responsive design
# REFACTOR: Used standard viewport settings
# ============================================

if grep -q '<meta name="viewport"' index.html; then
    pass "Viewport meta tag present"
else
    fail "Missing viewport meta tag"
fi

# ============================================
# RED: Test for semantic nav element
# GREEN: Replaced div with <nav>
# REFACTOR: Added role="navigation"
# ============================================

if grep -q '<nav' index.html; then
    pass "Semantic <nav> element present"
else
    fail "Missing semantic <nav> element"
fi

# ============================================
# RED: Test for semantic main element
# GREEN: Wrapped main content in <main>
# REFACTOR: Added role="main"
# ============================================

if grep -q '<main' index.html; then
    pass "Semantic <main> element present"
else
    fail "Missing semantic <main> element"
fi

# ============================================
# RED: Test for semantic section elements
# GREEN: Used <section> for content blocks
# REFACTOR: Added IDs for navigation
# ============================================

if grep -q '<section' index.html; then
    pass "Semantic <section> elements present"
else
    fail "Missing semantic <section> elements"
fi

# ============================================
# RED: Test for proper heading hierarchy
# GREEN: Implemented h1 -> h2 -> h3 structure
# REFACTOR: Ensured single h1 per page
# ============================================

h1_count=$(grep -o '<h1' index.html | wc -l)
if [ "$h1_count" -eq 1 ]; then
    pass "Single <h1> heading (proper hierarchy)"
else
    fail "Multiple or missing <h1> headings (found: $h1_count)"
fi

# ============================================
# RED: Test for external stylesheet link
# GREEN: Added <link rel="stylesheet" href="style.css">
# REFACTOR: Ensured proper MIME type
# ============================================

if grep -q '<link rel="stylesheet" href="style.css">' index.html; then
    pass "External stylesheet linked"
else
    fail "Missing external stylesheet link"
fi

# ============================================
# RED: Test for external script
# GREEN: Added <script src="script.js">
# REFACTOR: Moved to bottom of body for performance
# ============================================

if grep -q '<script src="script.js"' index.html; then
    pass "External JavaScript linked"
else
    fail "Missing external JavaScript link"
fi

echo ""
echo "HTML Validation: $PASSED passed, $FAILED failed"
exit $FAILED
