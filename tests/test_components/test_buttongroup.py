"""Tests for ButtonGroup component."""

from fasthtml.common import to_xml
from faststrap import Button
from faststrap.components.forms import ButtonGroup, ButtonToolbar


def test_buttongroup_basic():
    """ButtonGroup renders with buttons."""
    group = ButtonGroup(
        Button("One"),
        Button("Two"),
        Button("Three")
    )
    html = to_xml(group)

    assert "btn-group" in html
    assert 'role="group"' in html
    assert "One" in html
    assert "Two" in html
    assert "Three" in html


def test_buttongroup_sizes():
    """ButtonGroup supports sizes."""
    for size in ["sm", "lg"]:
        group = ButtonGroup(Button("Test"), size=size)
        html = to_xml(group)
        assert f"btn-group-{size}" in html


def test_buttongroup_vertical():
    """ButtonGroup can be vertical."""
    group = ButtonGroup(
        Button("Top"),
        Button("Middle"),
        Button("Bottom"),
        vertical=True
    )
    html = to_xml(group)

    assert "btn-group-vertical" in html
    assert "Top" in html
    assert "Bottom" in html


def test_buttongroup_horizontal_default():
    """ButtonGroup is horizontal by default."""
    group = ButtonGroup(Button("Test"))
    html = to_xml(group)

    assert "btn-group" in html
    assert "btn-group-vertical" not in html


def test_buttongroup_custom_classes():
    """ButtonGroup merges custom classes."""
    group = ButtonGroup(Button("Test"), cls="custom-group shadow")
    html = to_xml(group)

    assert "btn-group" in html
    assert "custom-group" in html
    assert "shadow" in html


def test_buttongroup_data_attributes():
    """ButtonGroup handles data attributes."""
    group = ButtonGroup(Button("Test"), data_id="123")
    html = to_xml(group)

    assert 'data-id="123"' in html


def test_buttontoolbar_basic():
    """ButtonToolbar renders with groups."""
    toolbar = ButtonToolbar(
        ButtonGroup(Button("1"), Button("2")),
        ButtonGroup(Button("3"), Button("4"))
    )
    html = to_xml(toolbar)

    assert "btn-toolbar" in html
    assert 'role="toolbar"' in html
    assert "btn-group" in html


def test_buttontoolbar_custom_classes():
    """ButtonToolbar merges custom classes."""
    toolbar = ButtonToolbar(
        ButtonGroup(Button("Test")),
        cls="custom-toolbar"
    )
    html = to_xml(toolbar)

    assert "btn-toolbar" in html
    assert "custom-toolbar" in html


def test_buttongroup_with_variants():
    """ButtonGroup works with different button variants."""
    group = ButtonGroup(
        Button("Primary", variant="primary"),
        Button("Success", variant="success"),
        Button("Danger", variant="danger")
    )
    html = to_xml(group)

    assert "btn-primary" in html
    assert "btn-success" in html
    assert "btn-danger" in html
