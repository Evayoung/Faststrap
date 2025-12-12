"""Tests for Tabs component."""

from fasthtml.common import to_xml

from faststrap.components.navigation import TabPane, Tabs


def test_tabs_basic():
    """Tabs render with basic items."""
    tabs = Tabs(("home", "Home"), ("profile", "Profile"), ("contact", "Contact"))
    html = to_xml(tabs)

    assert "Home" in html
    assert "Profile" in html
    assert "Contact" in html
    assert "nav-tabs" in html


def test_tabs_first_active():
    """First tab is active by default."""
    tabs = Tabs(("tab1", "Tab 1"), ("tab2", "Tab 2"))
    html = to_xml(tabs)

    assert "active" in html
    assert 'id="tab1-tab"' in html


def test_tabs_explicit_active():
    """Can explicitly set active tab."""
    tabs = Tabs(("tab1", "Tab 1"), ("tab2", "Tab 2", True), ("tab3", "Tab 3"))
    html = to_xml(tabs)

    assert 'aria-selected="true"' in html
    assert 'id="tab2-tab"' in html


def test_tabs_pills():
    """Tabs support pills variant."""
    tabs = Tabs(("a", "A"), ("b", "B"), variant="pills")
    html = to_xml(tabs)

    assert "nav-pills" in html
    assert "nav-tabs" not in html


def test_tabs_justified():
    """Tabs can be justified."""
    tabs = Tabs(("a", "A"), ("b", "B"), justified=True)
    html = to_xml(tabs)

    assert "nav-justified" in html


def test_tabs_fill():
    """Tabs can fill width."""
    tabs = Tabs(("a", "A"), ("b", "B"), fill=True)
    html = to_xml(tabs)

    assert "nav-fill" in html


def test_tabs_vertical():
    """Tabs support vertical layout."""
    tabs = Tabs(("a", "A"), ("b", "B"), vertical=True)
    html = to_xml(tabs)

    assert "flex-column" in html
    assert "row" in html  # Vertical uses grid layout


def test_tabs_htmx_mode():
    """Tabs support HTMX mode."""
    tabs = Tabs(("a", "A"), ("b", "B"), htmx=True)
    html = to_xml(tabs)

    assert "data-bs-toggle" not in html  # Bootstrap JS disabled
    assert "data-bs-target" not in html


def test_tabs_aria_attributes():
    """Tabs have proper ARIA attributes."""
    tabs = Tabs(("home", "Home"), ("profile", "Profile"))
    html = to_xml(tabs)

    assert 'role="tab"' in html
    assert 'role="tablist"' in html
    assert 'aria-controls="home"' in html


def test_tabs_custom_classes():
    """Tabs merge custom classes."""
    tabs = Tabs(("a", "A"), cls="custom-tabs")
    html = to_xml(tabs)

    assert "nav-tabs" in html
    assert "custom-tabs" in html


def test_tabpane_basic():
    """TabPane renders correctly."""
    pane = TabPane("Content", tab_id="home")
    html = to_xml(pane)

    assert "Content" in html
    assert "tab-pane" in html
    assert 'id="home"' in html


def test_tabpane_active():
    """TabPane can be active."""
    pane = TabPane("Content", tab_id="home", active=True)
    html = to_xml(pane)

    assert "show" in html
    assert "active" in html


def test_tabpane_aria():
    """TabPane has proper ARIA attributes."""
    pane = TabPane("Content", tab_id="home")
    html = to_xml(pane)

    assert 'role="tabpanel"' in html
    assert 'aria-labelledby="home-tab"' in html
