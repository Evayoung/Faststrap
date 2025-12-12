"""Tests for Select component."""

from fasthtml.common import to_xml

from faststrap.components.forms import Select


def test_select_basic():
    """Select renders with options."""
    select = Select("country", ("us", "United States"), ("uk", "United Kingdom"), ("ca", "Canada"))
    html = to_xml(select)

    assert 'name="country"' in html
    assert "United States" in html
    assert "United Kingdom" in html
    assert "form-select" in html


def test_select_with_label():
    """Select with label wraps in div."""
    select = Select("size", ("s", "Small"), ("m", "Medium"), label="Select Size")
    html = to_xml(select)

    assert "Select Size" in html
    assert "form-label" in html
    assert "mb-3" in html


def test_select_selected_option():
    """Select can have default selection."""
    select = Select("size", ("s", "Small"), ("m", "Medium", True), ("l", "Large"))
    html = to_xml(select)

    assert "selected" in html
    assert "Medium" in html


def test_select_sizes():
    """Select supports size variants."""
    small = Select("field", ("a", "A"), size="sm")
    large = Select("field", ("a", "A"), size="lg")

    assert "form-select-sm" in to_xml(small)
    assert "form-select-lg" in to_xml(large)


def test_select_disabled():
    """Select can be disabled."""
    select = Select("field", ("a", "A"), disabled=True)
    html = to_xml(select)

    assert "disabled" in html


def test_select_required():
    """Select can be required."""
    select = Select("field", ("a", "A"), label="Field", required=True)
    html = to_xml(select)

    assert "required" in html
    assert "*" in html  # Required indicator


def test_select_multiple():
    """Select supports multiple mode."""
    select = Select("tags", ("py", "Python"), ("js", "JavaScript"), multiple=True)
    html = to_xml(select)

    assert "multiple" in html


def test_select_with_help_text():
    """Select supports help text."""
    select = Select("country", ("us", "US"), help_text="Choose your country")
    html = to_xml(select)

    assert "Choose your country" in html
    assert "form-text" in html


def test_select_id_label_linkage():
    """Select ID links to label correctly."""
    select = Select("country", ("us", "US"), label="Country")
    html = to_xml(select)

    assert 'id="country"' in html
    assert 'for="country"' in html


def test_select_custom_id():
    """Select accepts custom ID."""
    select = Select("field", ("a", "A"), label="Field", id="custom_select")
    html = to_xml(select)

    assert 'id="custom_select"' in html
    assert 'for="custom_select"' in html


def test_select_htmx():
    """Select supports HTMX attributes."""
    select = Select("category", ("a", "A"), ("b", "B"), hx_get="/filter", hx_trigger="change")
    html = to_xml(select)

    assert 'hx-get="/filter"' in html
    assert 'hx-trigger="change"' in html


def test_select_custom_classes():
    """Select merges custom classes."""
    select = Select("field", ("a", "A"), cls="custom-select")
    html = to_xml(select)

    assert "form-select" in html
    assert "custom-select" in html


def test_select_data_attributes():
    """Select handles data attributes."""
    select = Select("field", ("a", "A"), data_validation="required")
    html = to_xml(select)

    assert 'data-validation="required"' in html


def test_select_without_wrapper():
    """Select without label/help returns just select."""
    select = Select("field", ("a", "A"))
    html = to_xml(select)

    assert "mb-3" not in html  # No wrapper div
    assert "form-select" in html


def test_select_option_values():
    """Select options have correct values."""
    select = Select("size", ("small", "Small"), ("large", "Large"))
    html = to_xml(select)

    assert 'value="small"' in html
    assert 'value="large"' in html
