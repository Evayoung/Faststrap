"""Tests for Breadcrumb component."""

from fasthtml.common import to_xml

from faststrap.components.navigation import Breadcrumb


def test_breadcrumb_basic():
    """Breadcrumb renders with items."""
    breadcrumb = Breadcrumb(("Home", "/"), ("Library", "/library"), ("Data", None))
    html = to_xml(breadcrumb)

    assert "Home" in html
    assert "Library" in html
    assert "Data" in html
    assert "breadcrumb" in html


def test_breadcrumb_last_active():
    """Last breadcrumb item is active by default."""
    breadcrumb = Breadcrumb(("Home", "/"), ("Page", None))
    html = to_xml(breadcrumb)

    assert "active" in html
    assert 'aria-current="page"' in html


def test_breadcrumb_explicit_active():
    """Breadcrumb can have explicit active item."""
    breadcrumb = Breadcrumb(
        ("Home", "/", False), ("Library", "/library", True), ("Data", None, False)
    )
    html = to_xml(breadcrumb)

    assert "Library" in html
    assert "active" in html


def test_breadcrumb_links():
    """Breadcrumb creates links for non-active items."""
    breadcrumb = Breadcrumb(("Home", "/"), ("Products", "/products"), ("Item", None))
    html = to_xml(breadcrumb)

    assert 'href="/"' in html
    assert 'href="/products"' in html


def test_breadcrumb_custom_classes():
    """Breadcrumb merges custom classes."""
    breadcrumb = Breadcrumb(("Home", "/"), ("Page", None), cls="custom-breadcrumb")
    html = to_xml(breadcrumb)

    assert "breadcrumb" in html
    assert "custom-breadcrumb" in html


def test_breadcrumb_aria_label():
    """Breadcrumb has proper ARIA label."""
    breadcrumb = Breadcrumb(("Home", "/"), ("Page", None))
    html = to_xml(breadcrumb)

    assert 'aria-label="breadcrumb"' in html


def test_breadcrumb_single_item():
    """Breadcrumb works with single item."""
    breadcrumb = Breadcrumb(("Home", None))
    html = to_xml(breadcrumb)

    assert "Home" in html
    assert "active" in html


def test_breadcrumb_htmx():
    """Breadcrumb supports HTMX attributes."""
    breadcrumb = Breadcrumb(("Home", "/"), ("Page", None), hx_boost="true")
    html = to_xml(breadcrumb)

    assert 'hx-boost="true"' in html


def test_breadcrumb_data_attributes():
    """Breadcrumb handles data attributes."""
    breadcrumb = Breadcrumb(("Home", "/"), ("Page", None), data_testid="nav-breadcrumb")
    html = to_xml(breadcrumb)

    assert 'data-testid="nav-breadcrumb"' in html
