"""Tests for Spinner component."""

from fasthtml.common import to_xml

from faststrap.components.feedback import Spinner


def test_spinner_basic():
    """Spinner renders with default settings."""
    spinner = Spinner()
    html = to_xml(spinner)

    assert "spinner-border" in html
    assert 'role="status"' in html


def test_spinner_types():
    """Spinner supports border and grow types."""
    border = Spinner(spinner_type="border")
    grow = Spinner(spinner_type="grow")

    assert "spinner-border" in to_xml(border)
    assert "spinner-grow" in to_xml(grow)


def test_spinner_variants():
    """Spinner supports all color variants."""
    variants = ["primary", "secondary", "success", "danger", "warning", "info", "light", "dark"]

    for variant in variants:
        spinner = Spinner(variant=variant)
        html = to_xml(spinner)
        assert f"text-{variant}" in html


def test_spinner_small_size():
    """Spinner supports small size."""
    spinner = Spinner(size="sm")
    html = to_xml(spinner)

    assert "spinner-border-sm" in html


def test_spinner_custom_label():
    """Spinner can have custom label."""
    spinner = Spinner(label="Processing...")
    html = to_xml(spinner)

    assert "Processing..." in html
    assert "visually-hidden" in html


def test_spinner_screen_reader_text():
    """Spinner has screen reader text."""
    spinner = Spinner()
    html = to_xml(spinner)

    assert "Loading..." in html
    assert "visually-hidden" in html


def test_spinner_custom_classes():
    """Spinner merges custom classes."""
    spinner = Spinner(cls="custom-spinner")
    html = to_xml(spinner)

    assert "spinner-border" in html
    assert "custom-spinner" in html


def test_spinner_data_attributes():
    """Spinner handles data attributes."""
    spinner = Spinner(data_testid="loading-spinner")
    html = to_xml(spinner)

    assert 'data-testid="loading-spinner"' in html


def test_spinner_in_button():
    """Spinner works inside buttons."""
    from faststrap import Button

    button = Button(Spinner(size="sm", variant="light"), " Loading...", disabled=True)
    html = to_xml(button)

    assert "spinner-border-sm" in html
    assert "Loading..." in html


def test_spinner_grow_small():
    """Growing spinner can be small."""
    spinner = Spinner(spinner_type="grow", size="sm")
    html = to_xml(spinner)

    assert "spinner-grow-sm" in html
