"""Tests for Toast component."""

from fasthtml.common import to_xml
from faststrap.components.feedback import Toast, ToastContainer


def test_toast_basic():
    """Toast renders with basic content."""
    toast = Toast("Test message")
    html = to_xml(toast)

    assert "Test message" in html
    assert "toast" in html
    assert "toast-body" in html
    assert 'role="alert"' in html


def test_toast_with_title():
    """Toast can have a title header."""
    toast = Toast("Message", title="Notification")
    html = to_xml(toast)

    assert "Notification" in html
    assert "Message" in html
    assert "toast-header" in html
    assert "btn-close" in html


def test_toast_variants():
    """Toast supports color variants."""
    variants = ["primary", "success", "danger", "warning", "info"]

    for variant in variants:
        toast = Toast("Test", variant=variant)
        html = to_xml(toast)
        assert f"text-bg-{variant}" in html


def test_toast_autohide_default():
    """Toast autohides by default."""
    toast = Toast("Message")
    html = to_xml(toast)

    assert 'data-bs-autohide="true"' in html
    assert 'data-bs-delay="5000"' in html


def test_toast_no_autohide():
    """Toast can disable autohide."""
    toast = Toast("Persistent", autohide=False)
    html = to_xml(toast)

    assert 'data-bs-autohide="false"' in html


def test_toast_custom_delay():
    """Toast accepts custom delay."""
    toast = Toast("Quick", delay=2000)
    html = to_xml(toast)

    assert 'data-bs-delay="2000"' in html


def test_toast_animation():
    """Toast has animation enabled by default."""
    toast = Toast("Animated")
    html = to_xml(toast)

    assert 'data-bs-animation="true"' in html


def test_toast_aria_attributes():
    """Toast has proper ARIA attributes."""
    toast = Toast("Accessible")
    html = to_xml(toast)

    assert 'aria-live="assertive"' in html
    assert 'aria-atomic="true"' in html


def test_toast_custom_classes():
    """Toast merges custom classes."""
    toast = Toast("Custom", cls="mb-3 shadow-lg")
    html = to_xml(toast)

    assert "toast" in html
    assert "mb-3" in html
    assert "shadow-lg" in html


def test_toast_container_basic():
    """ToastContainer renders correctly."""
    container = ToastContainer(
        Toast("Toast 1"),
        Toast("Toast 2")
    )
    html = to_xml(container)

    assert "toast-container" in html
    assert "position-fixed" in html
    assert "Toast 1" in html
    assert "Toast 2" in html


def test_toast_container_positions():
    """ToastContainer supports all positions."""
    positions = [
        "top-start",
        "top-center",
        "top-end",
        "middle-start",
        "middle-center",
        "middle-end",
        "bottom-start",
        "bottom-center",
        "bottom-end",
    ]

    for position in positions:
        container = ToastContainer(Toast("Test"), position=position)
        html = to_xml(container)
        assert "toast-container" in html
        # Should have position classes like "top-0", "start-0", etc.
        assert ("top-0" in html or "bottom-0" in html or "start-0" in html or
                "end-0" in html or "start-50" in html)


def test_toast_data_attributes():
    """Toast handles data attributes correctly."""
    toast = Toast("Data", data_id="123", data_type="notification")
    html = to_xml(toast)

    assert 'data-id="123"' in html
    assert 'data-type="notification"' in html
