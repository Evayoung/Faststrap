"""Tests for Progress component."""

from fasthtml.common import to_xml

from faststrap.components.feedback import Progress


def test_progress_basic():
    """Progress renders with value."""
    progress = Progress(75)
    html = to_xml(progress)

    assert "progress" in html
    assert "progress-bar" in html
    assert "width: 75" in html


def test_progress_percentage_calculation():
    """Progress calculates percentage correctly."""
    progress = Progress(50, max_value=100)
    html = to_xml(progress)

    assert "width: 50.0%" in html


def test_progress_custom_max():
    """Progress works with custom max value."""
    progress = Progress(30, max_value=60)
    html = to_xml(progress)

    assert "width: 50.0%" in html  # 30/60 = 50%


def test_progress_variants():
    """Progress supports all color variants."""
    variants = ["primary", "secondary", "success", "danger", "warning", "info", "light", "dark"]

    for variant in variants:
        progress = Progress(50, variant=variant)
        html = to_xml(progress)
        assert f"bg-{variant}" in html


def test_progress_with_label():
    """Progress can have label text."""
    progress = Progress(75, label="75%")
    html = to_xml(progress)

    assert "75%" in html


def test_progress_striped():
    """Progress supports striped style."""
    progress = Progress(60, striped=True)
    html = to_xml(progress)

    assert "progress-bar-striped" in html


def test_progress_animated():
    """Progress supports animated stripes."""
    progress = Progress(60, striped=True, animated=True)  # ✅ Fixed
    html = to_xml(progress)

    assert "progress-bar-striped" in html
    assert "progress-bar-animated" in html
