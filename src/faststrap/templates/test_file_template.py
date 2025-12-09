"""Tests for ComponentName.

This is a TEMPLATE file. Copy this to tests/test_components/test_your_component.py
and customize it for your component.
"""

from typing import TYPE_CHECKING

from fasthtml.common import to_xml  # ← IMPORTANT: Use to_xml(), not str()

# NOTE: When copying this template, adjust the import:
# from faststrap.components.category import ComponentName

# For template validation only (remove when using):
if TYPE_CHECKING:
    from fasthtml.common import FT

    def ComponentName(*children: object, **kwargs: object) -> FT:  # type: ignore
        """Placeholder for type checking."""
        ...


def test_component_basic() -> None:
    """Component renders correctly."""
    comp = ComponentName("Test")  # type: ignore
    html = to_xml(comp)

    assert "Test" in html
    assert "component-base" in html


def test_component_variants() -> None:
    """Component supports all variants."""
    variants = ["primary", "secondary", "success", "danger"]

    for variant in variants:
        comp = ComponentName("Test", variant=variant)  # type: ignore
        html = to_xml(comp)
        assert f"component-{variant}" in html


def test_component_custom_classes() -> None:
    """Component merges custom classes."""
    comp = ComponentName("Test", cls="custom-class mt-3")  # type: ignore
    html = to_xml(comp)

    assert "component-base" in html
    assert "custom-class" in html
    assert "mt-3" in html


def test_component_htmx() -> None:
    """Component supports HTMX."""
    comp = ComponentName("Load", hx_get="/api", hx_target="#result")  # type: ignore
    html = to_xml(comp)

    assert 'hx-get="/api"' in html
    assert 'hx-target="#result"' in html


def test_component_data_attributes() -> None:
    """Component handles data attributes."""
    comp = ComponentName("Test", data_id="123", data_type="info")  # type: ignore
    html = to_xml(comp)

    assert 'data-id="123"' in html
    assert 'data-type="info"' in html
