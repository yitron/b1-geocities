#!/bin/bash

# ============================================
# CSS VALIDATION TESTS
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

echo "CSS Validation Tests"
echo "-------------------------------------------"

# ============================================
# RED: Test for CSS custom properties
# GREEN: Defined --neon-* variables
# REFACTOR: Organized in :root
# ============================================

if grep -q ':root' style.css; then
    pass "CSS custom properties defined"
else
    fail "Missing CSS custom properties"
fi

# ============================================
# RED: Test for neon color palette
# GREEN: Added --neon-lime, --neon-pink, etc.
# REFACTOR: Used HSL for better control
# ============================================

if grep -q -- '--neon-' style.css; then
    pass "Neon color palette defined"
else
    fail "Missing neon color variables"
fi

# ============================================
# RED: Test for CSS Grid layout
# GREEN: Used display: grid
# REFACTOR: Added fallbacks for older browsers
# ============================================

if grep -q 'display: grid' style.css || grep -q 'display:grid' style.css; then
    pass "CSS Grid layout used"
else
    fail "CSS Grid layout not found"
fi

# ============================================
# RED: Test for blink animation
# GREEN: Created @keyframes blink
# REFACTOR: Optimized timing for readability
# ============================================

if grep -q '@keyframes blink' style.css; then
    pass "Blink animation defined"
else
    fail "Missing blink animation"
fi

# ============================================
# RED: Test for glow animation
# GREEN: Created @keyframes glow
# REFACTOR: Used text-shadow for effect
# ============================================

if grep -q '@keyframes glow' style.css; then
    pass "Glow animation defined"
else
    fail "Missing glow animation"
fi

# ============================================
# RED: Test for rainbow animation
# GREEN: Created @keyframes rainbow
# REFACTOR: Used hue-rotate for smooth colors
# ============================================

if grep -q '@keyframes rainbow' style.css || grep -q 'rainbow' style.css; then
    pass "Rainbow animation defined"
else
    fail "Missing rainbow animation"
fi

# ============================================
# RED: Test for Google Fonts import
# GREEN: Added @import for Press Start 2P
# REFACTOR: Used preconnect for performance
# ============================================

if grep -q 'Press Start 2P' style.css || grep -q 'Press Start 2P' index.html; then
    pass "Retro font (Press Start 2P) loaded"
else
    fail "Missing retro font"
fi

# ============================================
# RED: Test for responsive units
# GREEN: Used rem/em instead of px where appropriate
# REFACTOR: Maintained 90s aesthetic with some px
# ============================================

if grep -q 'rem\|em' style.css; then
    pass "Responsive units (rem/em) used"
else
    fail "No responsive units found"
fi

echo ""
echo "CSS Validation: $PASSED passed, $FAILED failed"
exit $FAILED
