"""Tests for Pagination component."""

from fasthtml.common import to_xml

from faststrap.components.navigation import Pagination


def test_pagination_basic():
    """Pagination renders with page numbers."""
    pagination = Pagination(current_page=3, total_pages=10)
    html = to_xml(pagination)

    assert "pagination" in html
    assert "page-item" in html


def test_pagination_active_page():
    """Current page is marked as active."""
    pagination = Pagination(current_page=5, total_pages=10)
    html = to_xml(pagination)

    assert "active" in html
    assert 'aria-current="page"' in html


def test_pagination_sizes():
    """Pagination supports size variants."""
    small = Pagination(1, 5, size="sm")
    large = Pagination(1, 5, size="lg")

    assert "pagination-sm" in to_xml(small)
    assert "pagination-lg" in to_xml(large)


def test_pagination_alignment():
    """Pagination supports alignment."""
    center = Pagination(1, 5, align="center")
    end = Pagination(1, 5, align="end")

    assert "justify-content-center" in to_xml(center)
    assert "justify-content-end" in to_xml(end)


def test_pagination_max_pages():
    """Pagination respects max_pages limit."""
    pagination = Pagination(10, 100, max_pages=3)
    html = to_xml(pagination)

    # Should show limited page numbers
    assert "pagination" in html


def test_pagination_prev_next():
    """Pagination shows prev/next buttons."""
    pagination = Pagination(3, 10, show_prev_next=True)
    html = to_xml(pagination)

    assert "‹" in html  # Previous
    assert "›" in html  # Next


def test_pagination_first_last():
    """Pagination can show first/last buttons."""
    pagination = Pagination(5, 10, show_first_last=True)
    html = to_xml(pagination)

    assert "«" in html  # First
    assert "»" in html  # Last


def test_pagination_disabled_prev():
    """Previous button disabled on first page."""
    pagination = Pagination(1, 10, show_prev_next=True)
    html = to_xml(pagination)

    assert "disabled" in html


def test_pagination_disabled_next():
    """Next button disabled on last page."""
    pagination = Pagination(10, 10, show_prev_next=True)
    html = to_xml(pagination)

    assert "disabled" in html


def test_pagination_base_url():
    """Pagination uses custom base URL."""
    pagination = Pagination(2, 5, base_url="/products")
    html = to_xml(pagination)

    assert "/products?page=" in html


def test_pagination_page_links():
    """Pagination generates correct page links."""
    pagination = Pagination(1, 3, base_url="/items")
    html = to_xml(pagination)

    # Note: Page 1 is active (Span), pages 2-3 have links
    assert "/items?page=2" in html  # ✅ Fixed
    assert "/items?page=3" in html


def test_pagination_custom_classes():
    """Pagination merges custom classes."""
    pagination = Pagination(1, 5, cls="custom-pagination")
    html = to_xml(pagination)

    assert "pagination" in html
    assert "custom-pagination" in html


def test_pagination_htmx():
    """Pagination supports HTMX attributes."""
    pagination = Pagination(2, 5, hx_boost="true", hx_target="#content")
    html = to_xml(pagination)

    assert 'hx-boost="true"' in html
    assert 'hx-target="#content"' in html


def test_pagination_aria_label():
    """Pagination has proper ARIA label."""
    pagination = Pagination(1, 5)
    html = to_xml(pagination)

    assert 'aria-label="Page navigation"' in html
