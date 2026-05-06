#!/bin/bash

# ============================================
# B1 GEOCITIES - AGGREGATED TEST RUNNER
# Tests only essential functionality
# Robust component tests in tests/
# ============================================

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "=========================================="
echo "B1 GEOCITIES - ESSENTIAL TESTS"
echo "=========================================="
echo ""

TOTAL_PASSED=0
TOTAL_FAILED=0

# ============================================
# ESSENTIAL TEST 1: Core files exist
# ============================================

echo "1. Core Files Check"
echo "-------------------------------------------"

if [ -f "index.html" ] && [ -f "style.css" ] && [ -f "script.js" ]; then
    echo -e "${GREEN}✓${NC} All core files present (index.html, style.css, script.js)"
    ((TOTAL_PASSED++))
else
    echo -e "${RED}✗${NC} Missing core files"
    ((TOTAL_FAILED++))
fi

echo ""

# ============================================
# ESSENTIAL TEST 2: HTML is valid HTML5
# ============================================

echo "2. HTML5 Structure"
echo "-------------------------------------------"

if grep -q "<!DOCTYPE html>" index.html && \
   grep -q '<html lang=' index.html && \
   grep -q '<nav' index.html && \
   grep -q '<main' index.html; then
    echo -e "${GREEN}✓${NC} HTML5 semantic structure present"
    ((TOTAL_PASSED++))
else
    echo -e "${RED}✗${NC} Invalid HTML5 structure"
    ((TOTAL_FAILED++))
fi

echo ""

# ============================================
# ESSENTIAL TEST 3: HitCounter functionality
# ============================================

echo "3. HitCounter Implementation"
echo "-------------------------------------------"

if grep -q "class HitCounter" script.js && \
   grep -q "localStorage" script.js; then
    echo -e "${GREEN}✓${NC} HitCounter class with localStorage implemented"
    ((TOTAL_PASSED++))
else
    echo -e "${RED}✗${NC} HitCounter not properly implemented"
    ((TOTAL_FAILED++))
fi

echo ""

# ============================================
# ESSENTIAL TEST 4: 90s aesthetic elements
# ============================================

echo "4. Geocities Aesthetic"
echo "-------------------------------------------"

if grep -q -- '--neon-' style.css && \
   grep -q '@keyframes' style.css; then
    echo -e "${GREEN}✓${NC} Neon colors and animations present"
    ((TOTAL_PASSED++))
else
    echo -e "${RED}✗${NC} Missing 90s aesthetic elements"
    ((TOTAL_FAILED++))
fi

echo ""

# ============================================
# ESSENTIAL TEST 5: No build dependencies
# ============================================

echo "5. Zero Dependencies Check"
echo "-------------------------------------------"

if [ ! -f "package.json" ] && [ ! -f "webpack.config.js" ]; then
    echo -e "${GREEN}✓${NC} No build dependencies (vanilla HTML/CSS/JS)"
    ((TOTAL_PASSED++))
else
    echo -e "${RED}✗${NC} Found build dependencies (should be zero)"
    ((TOTAL_FAILED++))
fi

echo ""

# ============================================
# RUN COMPONENT TEST SUITES (detailed)
# ============================================

echo "=========================================="
echo "RUNNING COMPONENT TEST SUITES"
echo "=========================================="
echo ""

COMPONENT_FAILED=0

# HTML Validation Suite
echo "Running HTML validation suite..."
./tests/html_validation.sh
if [ $? -ne 0 ]; then ((COMPONENT_FAILED++)); fi
echo ""

# CSS Validation Suite
echo "Running CSS validation suite..."
./tests/css_validation.sh
if [ $? -ne 0 ]; then ((COMPONENT_FAILED++)); fi
echo ""

# Accessibility Suite
echo "Running accessibility suite..."
./tests/accessibility.sh
if [ $? -ne 0 ]; then ((COMPONENT_FAILED++)); fi
echo ""

# Functional Suite
echo "Running functional suite..."
./tests/functional.sh
if [ $? -ne 0 ]; then ((COMPONENT_FAILED++)); fi
echo ""

# ============================================
# FINAL SUMMARY
# ============================================

echo "=========================================="
echo "TEST SUMMARY"
echo "=========================================="
echo ""
echo "Essential Tests: $TOTAL_PASSED passed, $TOTAL_FAILED failed"
echo "Component Suites: $((4 - COMPONENT_FAILED)) passed, $COMPONENT_FAILED failed"
echo ""

if [ $TOTAL_FAILED -eq 0 ] && [ $COMPONENT_FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ All tests passed!${NC}"
    echo ""
    echo "Ready to run:"
    echo "  open index.html"
    exit 0
else
    echo -e "${RED}✗ Some tests failed${NC}"
    exit 1
fi
