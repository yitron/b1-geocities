#!/bin/bash

# ============================================
# ACCESSIBILITY TESTS (WCAG AA)
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

echo "Accessibility Tests (WCAG AA)"
echo "-------------------------------------------"

# ============================================
# RED: Test for ARIA landmarks
# GREEN: Added role="navigation" to nav
# REFACTOR: Also added role="main" to main
# ============================================

if grep -q 'role="navigation"' index.html; then
    pass "ARIA navigation landmark present"
else
    fail "Missing ARIA navigation landmark"
fi

if grep -q 'role="main"' index.html; then
    pass "ARIA main landmark present"
else
    fail "Missing ARIA main landmark"
fi

# ============================================
# RED: Test for ARIA labels
# GREEN: Added aria-label to navigation links
# REFACTOR: Made labels descriptive
# ============================================

if grep -q 'aria-label' index.html; then
    pass "ARIA labels present"
else
    fail "Missing ARIA labels"
fi

# ============================================
# RED: Test for link security attributes
# GREEN: Added rel="noopener noreferrer" to external links
# REFACTOR: Applied to all external links
# ============================================

external_links=$(grep -o 'target="_blank"' index.html | wc -l)
if [ "$external_links" -gt 0 ]; then
    if grep -q 'rel="noopener' index.html; then
        pass "External links have security attributes"
    else
        fail "External links missing rel='noopener'"
    fi
fi

# ============================================
# RED: Test for focus indicators
# GREEN: Ensured default focus visible
# REFACTOR: Enhanced with custom focus styles
# ============================================

if grep -q ':focus' style.css; then
    pass "Focus indicators defined"
else
    fail "Missing focus indicator styles"
fi

# ============================================
# RED: Test for color contrast comments
# GREEN: Added contrast ratio notes in CSS
# REFACTOR: Adjusted colors to meet WCAG AA
# ============================================

if grep -qi 'contrast\|wcag' style.css; then
    pass "Color contrast considerations documented"
else
    fail "No color contrast documentation"
fi

# ============================================
# RED: Test for reduced motion support
# GREEN: Added @media (prefers-reduced-motion)
# REFACTOR: Disabled animations when requested
# ============================================

if grep -q 'prefers-reduced-motion' style.css; then
    pass "Reduced motion support implemented"
else
    fail "Missing reduced motion support (TODO)"
fi

echo ""
echo "Accessibility: $PASSED passed, $FAILED failed"
exit $FAILED
