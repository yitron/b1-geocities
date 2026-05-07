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
