"""Tests for Drawer (Offcanvas) component."""

from faststrap.components.navigation import Drawer
from fasthtml.common import to_xml


def test_drawer_basic():
    """Drawer renders with basic content."""
    drawer = Drawer("Content", drawer_id="testDrawer")
    html = to_xml(drawer)

    assert "Content" in html
    assert "offcanvas" in html
    assert "offcanvas-body" in html
    assert 'id="testDrawer"' in html


def test_drawer_with_title():
    """Drawer can have a title."""
    drawer = Drawer("Body", drawer_id="drawer1", title="Menu")
    html = to_xml(drawer)

    assert "Menu" in html
    assert "offcanvas-title" in html
    assert "offcanvas-header" in html
    assert "btn-close" in html


def test_drawer_placements():
    """Drawer supports all placement positions."""
    placements = ["start", "end", "top", "bottom"]

    for placement in placements:
        drawer = Drawer("Content", drawer_id=f"drawer_{placement}", placement=placement)
        html = to_xml(drawer)
        assert f"offcanvas-{placement}" in html


def test_drawer_default_placement():
    """Drawer uses 'start' placement by default."""
    drawer = Drawer("Content", drawer_id="defaultDrawer")
    html = to_xml(drawer)

    assert "offcanvas-start" in html


def test_drawer_backdrop_default():
    """Drawer has backdrop by default."""
    drawer = Drawer("Content", drawer_id="backdropDrawer")
    html = to_xml(drawer)

    # Backdrop is default, so data-bs-backdrop should NOT be present
    assert 'data-bs-backdrop="false"' not in html


def test_drawer_no_backdrop():
    """Drawer can disable backdrop."""
    drawer = Drawer("Content", drawer_id="noBackdrop", backdrop=False)
    html = to_xml(drawer)

    assert 'data-bs-backdrop="false"' in html


def test_drawer_scroll():
    """Drawer can enable body scroll."""
    drawer = Drawer("Content", drawer_id="scrollDrawer", scroll=True)
    html = to_xml(drawer)

    assert 'data-bs-scroll="true"' in html


def test_drawer_aria_attributes():
    """Drawer has proper ARIA attributes."""
    drawer = Drawer("Content", drawer_id="ariaDrawer", title="Accessible")
    html = to_xml(drawer)

    assert 'aria-labelledby="ariaDrawerLabel"' in html
    assert 'tabindex="-1"' in html


def test_drawer_custom_classes():
    """Drawer merges custom classes."""
    drawer = Drawer("Content", drawer_id="customDrawer", cls="custom-drawer")
    html = to_xml(drawer)

    assert "offcanvas" in html
    assert "custom-drawer" in html


def test_drawer_data_attributes():
    """Drawer handles data attributes correctly."""
    drawer = Drawer("Content", drawer_id="dataDrawer", data_test="value")
    html = to_xml(drawer)

    assert 'data-test="value"' in html


def test_drawer_full_configuration():
    """Drawer with all options works correctly."""
    drawer = Drawer(
        "Body content",
        drawer_id="fullDrawer",
        title="Full Drawer",
        placement="end",
        backdrop=False,
        scroll=True
    )
    html = to_xml(drawer)

    assert "Full Drawer" in html
    assert "Body content" in html
    assert "offcanvas-end" in html
    assert 'data-bs-backdrop="false"' in html
    assert 'data-bs-scroll="true"' in html


def test_drawer_multiple_children():
    """Drawer body can contain multiple elements."""
    drawer = Drawer("First. ", "Second. ", "Third.", drawer_id="multiDrawer")
    html = to_xml(drawer)

    assert "First." in html
    assert "Second." in html
    assert "Third." in html
