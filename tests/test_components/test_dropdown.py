"""Tests for Dropdown component."""

from fasthtml.common import A, to_xml

from faststrap.components.navigation import Dropdown, DropdownDivider, DropdownItem


def test_dropdown_basic():
    """Dropdown renders with items."""
    dropdown = Dropdown("Action", "Another action", label="Actions")
    html = to_xml(dropdown)

    assert "Actions" in html
    assert "Action" in html
    assert "dropdown" in html
    assert "dropdown-menu" in html


def test_dropdown_variants():
    """Dropdown supports all variants."""
    variants = ["primary", "secondary", "success", "danger", "warning", "info", "light", "dark"]

    for variant in variants:
        dropdown = Dropdown("Item", label="Test", variant=variant)
        html = to_xml(dropdown)
        assert f"btn-{variant}" in html


def test_dropdown_sizes():
    """Dropdown supports size variants."""
    small = Dropdown("Item", label="Small", size="sm")
    large = Dropdown("Item", label="Large", size="lg")

    assert "btn-sm" in to_xml(small)
    assert "btn-lg" in to_xml(large)


def test_dropdown_split():
    """Dropdown supports split button."""
    dropdown = Dropdown("Edit", "Delete", label="Options", split=True)
    html = to_xml(dropdown)

    assert "btn-group" in html
    assert "dropdown-toggle-split" in html


def test_dropdown_directions():
    """Dropdown supports all directions."""
    dropup = Dropdown("Item", label="Up", direction="up")
    dropstart = Dropdown("Item", label="Start", direction="start")
    dropend = Dropdown("Item", label="End", direction="end")

    assert "dropup" in to_xml(dropup)
    assert "dropstart" in to_xml(dropstart)
    assert "dropend" in to_xml(dropend)


def test_dropdown_with_divider():
    """Dropdown supports dividers with string."""
    dropdown = Dropdown("Action", "---", "Separated link", label="Menu")  # String divider
    html = to_xml(dropdown)

    assert "dropdown-divider" in html


def test_dropdown_with_links():
    """Dropdown works with A elements."""
    link = A("Custom Link", href="/custom")
    dropdown = Dropdown(link, label="Menu")
    html = to_xml(dropdown)

    assert "Custom Link" in html
    assert "dropdown-item" in html


def test_dropdown_toggle_attributes():
    """Dropdown has proper toggle attributes."""
    dropdown = Dropdown("Item", label="Menu")
    html = to_xml(dropdown)

    assert 'data-bs-toggle="dropdown"' in html
    assert 'aria-expanded="false"' in html


def test_dropdown_custom_classes():
    """Dropdown merges custom classes."""
    dropdown = Dropdown("Item", label="Menu", cls="custom-dropdown")
    html = to_xml(dropdown)

    assert "dropdown" in html
    assert "custom-dropdown" in html


def test_dropdown_item():
    """DropdownItem renders correctly."""
    item = DropdownItem("Action")
    html = to_xml(item)

    assert "Action" in html
    assert "dropdown-item" in html
    assert 'role="menuitem"' in html


def test_dropdown_item_active():
    """DropdownItem can be active."""
    item = DropdownItem("Active", active=True)
    html = to_xml(item)

    assert "active" in html


def test_dropdown_item_disabled():
    """DropdownItem can be disabled."""
    item = DropdownItem("Disabled", disabled=True)
    html = to_xml(item)

    assert "disabled" in html
    assert 'aria-disabled="true"' in html


def test_dropdown_divider():
    """DropdownDivider renders correctly."""
    divider = DropdownDivider()
    html = to_xml(divider)

    assert "dropdown-divider" in html
