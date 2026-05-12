"""
Frontend Tests - TDD for B1 Geocities
Test HTML structure and content
"""

import pytest
import os
from pathlib import Path


class TestHTMLStructure:
    """Test HTML file structure and content"""

    def test_index_html_exists(self):
        """
        RED: Test that index.html exists
        Should FAIL - no index.html exists yet
        """
        html_path = Path('index.html')
        assert html_path.exists(), "index.html should exist"

    def test_index_html_has_doctype(self):
        """
        RED: Test that index.html has HTML5 doctype
        Should FAIL - no index.html exists yet
        """
        html_path = Path('index.html')
        if not html_path.exists():
            pytest.skip("index.html does not exist yet")

        content = html_path.read_text()
        assert '<!DOCTYPE html>' in content, "Should have HTML5 doctype"

    def test_index_html_has_title(self):
        """
        RED: Test that index.html has title with user name
        Should FAIL - no index.html exists yet
        """
        html_path = Path('index.html')
        if not html_path.exists():
            pytest.skip("index.html does not exist yet")

        content = html_path.read_text()
        assert '<title>' in content, "Should have title tag"
        assert 'HongZhuang' in content or 'Lim' in content, "Title should contain user name"

    def test_index_html_has_hit_counter(self):
        """
        RED: Test that index.html has hit counter element
        Should FAIL - no index.html exists yet
        """
        html_path = Path('index.html')
        if not html_path.exists():
            pytest.skip("index.html does not exist yet")

        content = html_path.read_text()
        assert 'hitcounter' in content.lower(), "Should have hit counter element"

    def test_index_html_has_guestbook(self):
        """
        RED: Test that index.html has guestbook element
        Should FAIL - no index.html exists yet
        """
        html_path = Path('index.html')
        if not html_path.exists():
            pytest.skip("index.html does not exist yet")

        content = html_path.read_text()
        assert 'guestbook' in content.lower(), "Should have guestbook element"

    # TDD Cycle 7a: Tiled Background Tests
    def test_body_has_background_image(self):
        """
        RED: Test that body has CSS background-image property
        Should FAIL - no tiled background exists yet
        """
        html_path = Path('index.html')
        if not html_path.exists():
            pytest.skip("index.html does not exist yet")

        content = html_path.read_text()
        # Check for background-image in <body> style attribute or <style> tag
        assert 'background-image' in content, "Should have background-image CSS property"

    def test_background_image_repeats(self):
        """
        RED: Test that background uses repeat property
        Should FAIL - no background-repeat exists yet
        """
        html_path = Path('index.html')
        if not html_path.exists():
            pytest.skip("index.html does not exist yet")

        content = html_path.read_text()
        # Check for background-repeat in CSS
        assert 'background-repeat' in content or 'background:' in content, "Should have background-repeat or shorthand"

    # TDD Cycle 7b: Browser Badges Tests
    def test_browser_badges_section_exists(self):
        """
        RED: Test that browser badges section exists
        Should FAIL - no badges section exists yet
        """
        html_path = Path('index.html')
        if not html_path.exists():
            pytest.skip("index.html does not exist yet")

        content = html_path.read_text()
        # Check for "Best Viewed In" or similar text
        content_lower = content.lower()
        assert 'best viewed' in content_lower or 'browser' in content_lower, "Should have browser badges section"

    def test_browser_badges_has_modern_browsers(self):
        """
        RED: Test that badges mention modern browsers
        Should FAIL - no browser links exist yet
        """
        html_path = Path('index.html')
        if not html_path.exists():
            pytest.skip("index.html does not exist yet")

        content = html_path.read_text()
        content_lower = content.lower()
        # Check for at least 2 modern browsers mentioned
        modern_browsers = ['chrome', 'firefox', 'safari', 'edge']
        found = sum(1 for browser in modern_browsers if browser in content_lower)
        assert found >= 2, f"Should mention at least 2 modern browsers, found {found}"

    # TDD Cycle 7c: Email Link with Icon Tests
    def test_email_link_exists(self):
        """
        RED: Test that mailto link exists
        Should FAIL - no email link exists yet
        """
        html_path = Path('index.html')
        if not html_path.exists():
            pytest.skip("index.html does not exist yet")

        content = html_path.read_text()
        assert 'mailto:' in content, "Should have mailto: link"

    def test_email_link_has_icon_or_emoji(self):
        """
        RED: Test that email link has visual indicator (icon/emoji)
        Should FAIL - no email icon exists yet
        """
        html_path = Path('index.html')
        if not html_path.exists():
            pytest.skip("index.html does not exist yet")

        content = html_path.read_text()
        # Check for email-related emoji or icon
        has_emoji = '📧' in content or '✉' in content or '💌' in content
        has_icon = 'envelope' in content.lower() or 'email-icon' in content.lower()
        assert has_emoji or has_icon, "Email link should have icon or emoji"

    # TDD Cycle 8: Frame Layout Tests
    def test_layout_has_two_columns(self):
        """
        RED: Test that page has two-column layout structure
        Should FAIL - no frame layout exists yet
        """
        html_path = Path('index.html')
        if not html_path.exists():
            pytest.skip("index.html does not exist yet")

        content = html_path.read_text()
        # Check for sidebar and main content structure
        has_sidebar = 'sidebar' in content.lower() or 'side-panel' in content.lower()
        has_main = 'main-content' in content.lower() or 'content-area' in content.lower()
        assert has_sidebar and has_main, "Should have sidebar and main content sections"

    def test_sidebar_exists_with_hitcounter(self):
        """
        RED: Test that sidebar contains hit counter
        Should FAIL - hitcounter not in sidebar yet
        """
        html_path = Path('index.html')
        if not html_path.exists():
            pytest.skip("index.html does not exist yet")

        content = html_path.read_text()
        content_lower = content.lower()

        # Find sidebar section
        assert 'sidebar' in content_lower or 'side-panel' in content_lower, "Sidebar should exist"

        # Check that sidebar contains hitcounter
        # Simple check: look for sidebar before hitcounter in the HTML flow
        sidebar_pos = content_lower.find('sidebar') if 'sidebar' in content_lower else content_lower.find('side-panel')
        hitcounter_pos = content_lower.find('hitcounter')

        assert hitcounter_pos > 0, "Hit counter should exist"
        assert sidebar_pos < hitcounter_pos, "Hit counter should be after sidebar in HTML structure"

    def test_sidebar_has_overflow_scroll(self):
        """
        RED: Test that sidebar has scrolling enabled
        Should FAIL - no overflow CSS on sidebar yet
        """
        html_path = Path('index.html')
        if not html_path.exists():
            pytest.skip("index.html does not exist yet")

        content = html_path.read_text()
        # Check for overflow-y: auto or scroll in CSS
        has_overflow = 'overflow-y: auto' in content or 'overflow-y: scroll' in content or 'overflow: auto' in content
        assert has_overflow, "Should have overflow scrolling CSS"

    def test_main_content_has_overflow_scroll(self):
        """
        RED: Test that main content has scrolling enabled
        Should FAIL - no overflow CSS on main content yet
        """
        html_path = Path('index.html')
        if not html_path.exists():
            pytest.skip("index.html does not exist yet")

        content = html_path.read_text()
        # Check for overflow-y: auto or scroll in CSS (should appear at least twice - sidebar + main)
        overflow_count = content.count('overflow-y: auto') + content.count('overflow-y: scroll') + content.count('overflow: auto')
        assert overflow_count >= 2, f"Should have overflow scrolling on both sidebar and main (found {overflow_count})"

    def test_layout_uses_flexbox_or_grid(self):
        """
        RED: Test that layout uses modern CSS layout (flexbox or grid)
        Should FAIL - no flexbox/grid layout yet
        """
        html_path = Path('index.html')
        if not html_path.exists():
            pytest.skip("index.html does not exist yet")

        content = html_path.read_text()
        has_flex = 'display: flex' in content or 'display:flex' in content
        has_grid = 'display: grid' in content or 'display:grid' in content
        assert has_flex or has_grid, "Should use flexbox or grid for layout"
