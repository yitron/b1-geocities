# Development Approach

**Project:** B1 Geocities Revival
**Type:** Individual Use (Personal Homepage)
**Last Updated:** 2026-05-06

---

## Table of Contents

1. [Project Positioning](#project-positioning)
2. [How We Collaborate](#how-we-collaborate)
3. [Tools & Why](#tools--why)
4. [Key Learnings](#key-learnings)
5. [Prompt Patterns That Work](#prompt-patterns-that-work)
6. [Development Log](#development-log)

---

## Project Positioning

**Use Case:** Individual Use - Personal Homepage/Portfolio

**Why Individual:**
- Single-user experience (no multi-user features)
- Personal branding and online presence
- localStorage is per-browser (individual data)
- Showcases one person's involvement with AI DAI program

**Target User:** One person maintaining their professional homepage

---

## How We Collaborate

### Specification-Driven Development

**Core Principle:** Product gets built along the way through iterative decisions

**Our Workflow:**
1. **You ask questions** → structural decisions (test organization, file structure)
2. **I propose solutions** → you approve or refine
3. **We log decisions** → captured in this document
4. **Product evolves** → built incrementally with each decision

### Division of Work

**Human (You):**
- Define requirements and scope
- Make structural decisions (ask me when unsure)
- Approve/reject AI proposals
- Test and validate outputs
- Refine and give feedback
- Git operations (commit, push)

**AI (Claude):**
- Generate code (HTML/CSS/JS)
- Propose solutions for structural questions
- Implement features based on requirements
- Suggest best practices
- Debug issues
- Create documentation structure
- **Permission Mode:** Ask before major structural changes

**Split:** ~85% AI code generation / ~15% Human direction

### TDD: RED-GREEN-REFACTOR

Every feature follows this cycle:

**RED Phase:**
```bash
# Write failing test first
# Example: Test for HitCounter class exists
if grep -q 'class HitCounter' script.js; then
    pass "HitCounter class exists"
else
    fail "HitCounter class not found"
fi
```

**GREEN Phase:**
```javascript
// Implement minimum code to pass
class HitCounter {
    constructor() { }
}
```

**REFACTOR Phase:**
```javascript
// Clean up, add error handling, document
class HitCounter {
    constructor(storageKey = 'aidai_hit_count') {
        this.storageKey = storageKey;
        // ... proper implementation
    }
}
```

### Test Structure

**Component Tests (tests/):** Robust, detailed tests
- `html_validation.sh` - HTML structure & semantics
- `css_validation.sh` - CSS quality & features
- `accessibility.sh` - WCAG compliance
- `functional.sh` - JavaScript features

**Aggregated Test (test.sh):** Essential functionality only
- Core files exist
- HTML5 structure valid
- HitCounter implemented
- 90s aesthetic present
- No build dependencies

**Run Tests:**
```bash
./test.sh              # Quick essential checks + all component suites
./tests/functional.sh  # Run specific component suite
```

---

## Tools & Why

| Tool | Purpose | Why This One |
|------|---------|--------------|
| **Vanilla HTML/CSS/JS** | Core implementation | No build step required, opens directly in browser |
| **localStorage** | Hit counter persistence | No backend needed, instant persistence |
| **CSS Grid** | Layout | Modern alternative to deprecated tables |
| **Google Fonts (CDN)** | Typography | Widely cached, no CORS issues |
| **test.sh** | Validation | Quick automated checks |
| **Git** | Version control | Track progress, show development process |

**Key Constraint:** Must work without npm/webpack/build tools

---

## Key Learnings

### #1: Semantic HTML First
**Learning:** Start with semantic tags (`<nav>`, `<main>`, `<section>`) not `<div>` soup
**Why:** Better accessibility, clearer structure
**Applied:** Entire HTML structure uses semantic elements

### #2: CSS Variables for Maintainability
**Learning:** Use CSS custom properties for colors/values that repeat
**Why:** Easy to update in one place
**Applied:** All neon colors defined as `--neon-*` variables

### #3: localStorage Needs Error Handling
**Learning:** localStorage can fail (privacy mode, quota exceeded)
**Why:** Prevent crashes in edge cases
**Applied:** Try/catch blocks in HitCounter class

### #4: WCAG Contrast Matters
**Learning:** Neon colors can fail contrast requirements
**Why:** Accessibility compliance
**Applied:** Adjusted pink from #FF1493 to #FF69B4 for 4.5:1 ratio

### #5: Animation Accessibility
**Learning:** Some users get motion sick from animations
**Why:** WCAG AAA recommendation
**Applied:** Added `@media (prefers-reduced-motion)` support

---

## Prompt Patterns That Work

### ✅ Good Prompts

**Specific with constraints:**
```
"Create a HitCounter class using localStorage with error handling.
Must work in browsers without localStorage. Format as 7 digits."
```

**Examples included:**
```
"Use neon colors like Geocities: lime #00FF00, hot pink #FF1493,
cyan #00FFFF, yellow #FFFF00"
```

**Context for debugging:**
```
"The counter resets to 1 instead of incrementing. Here's the load()
method: [paste code]. What's wrong?"
```

### ❌ Less Effective Prompts

**Too vague:**
```
"Add a counter" → Missing: where, how, what format?
```

**No constraints:**
```
"Make it colorful" → Which colors? How vibrant?
```

**No context:**
```
"It doesn't work" → What doesn't work? What error?
```

---

## Decision Log

### Decision #1: Test Organization (2026-05-06)

**Question:** How should tests be organized?

**Options Considered:**
1. Single test.sh with all tests inline
2. Split into component tests in tests/ directory
3. Separate test files by feature

**Decision:** Option 2 - Component tests in tests/ directory

**Rationale:**
- Main test.sh aggregates and tests only essentials
- Component tests (tests/*.sh) are robust and detailed
- Easier to maintain and extend
- Follows separation of concerns

**Structure:**
```
tests/
├── html_validation.sh    # Detailed HTML tests
├── css_validation.sh     # Detailed CSS tests
├── accessibility.sh      # WCAG compliance tests
└── functional.sh         # JavaScript functionality tests

test.sh                   # Aggregator (essential tests only)
```

### Decision #2: TDD Style (2026-05-06)

**Question:** What testing methodology to follow?

**Decision:** RED-GREEN-REFACTOR TDD

**Implementation:**
- Each test file shows RED-GREEN-REFACTOR comments
- Tests written before implementation
- Comments explain what changed in each phase

**Example:**
```bash
# RED: Test for HitCounter class
# GREEN: Implemented class HitCounter { }
# REFACTOR: Added error handling and localStorage
```

### Decision #3: Specification-Driven Development (2026-05-06)

**Question:** How do we collaborate on structural decisions?

**Decision:** Permission-first, question-driven approach

**Process:**
1. AI asks for approval on structural changes
2. Human makes decisions (you decide test structure, file organization)
3. Decisions logged in this document
4. Product builds incrementally with each decision

**Benefit:** Product evolves through decisions, not blind implementation

### Decision #4: Git Workflow (2026-05-06)

**Question:** Who handles git operations?

**Decision:** Human handles all git operations

**Rationale:**
- Git commits, pushes, and GitHub operations are human-controlled
- AI provides suggested commit messages
- AI prepares code and documentation
- Human executes git commands to maintain control

**Implementation:**
- Human initializes fresh repos
- Human creates commits with AI-suggested messages
- Human creates GitHub repositories
- Human pushes to remote

---

## Development Log

### 2026-05-06: Initial Implementation + Test Restructure

**What We Built:**
- Semantic HTML5 structure
- 90s Geocities aesthetic with CSS
- localStorage-based hit counter
- Accessibility features (WCAG AA)

**Collaboration Highlights:**
- You requested maximum neon chaos → AI implemented vibrant colors
- You wanted no build tools → AI suggested vanilla JS approach
- You needed accessibility → AI added WCAG compliance from start

**Iterations:**
- Colors: 2 iterations (initial too subdued → increased saturation)
- Counter: 4 iterations (debugging localStorage persistence)
- Accessibility: 1 pass (contrast adjustments)

**Time:** ~2-3 hours total

**What Worked:**
- Clear upfront constraints (no frameworks, no build)
- Specific design references (Geocities aesthetic)
- Iterative refinement on colors

**What We'd Do Different:**
- Specify exact hex colors earlier
- Test localStorage edge cases from start

---

## Notes for Next Session

**To Add:**
- Mobile responsive version (optional enhancement)
- Global hit counter backend (if needed)
- More pages (About, Tools, Community)

**To Remember:**
- Keep 90s aesthetic while maintaining accessibility
- Test in all three browsers (Chrome, Firefox, Safari)
- Validate HTML/CSS before committing

---

## Quick Reference

**File Structure:**
```
b1-geocities/
├── index.html      # Main page
├── style.css       # Styling
├── script.js       # Hit counter logic
├── test.sh         # Aggregated test runner (essentials)
├── tests/          # Component test suites (robust)
│   ├── html_validation.sh
│   ├── css_validation.sh
│   ├── accessibility.sh
│   └── functional.sh
└── docs/
    └── DEVELOPMENT_APPROACH.md  # This file (living document)
```

**Key Commands:**
```bash
# Open locally
open index.html

# Run tests
./test.sh

# Serve locally (optional)
python3 -m http.server 8000
```

**AI Model Used:** Claude Sonnet 4.5 (claude-sonnet-4-5-20250929)
