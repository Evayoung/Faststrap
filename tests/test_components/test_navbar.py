"""Tests for Navbar component."""

from fasthtml.common import A
from fasthtml.common import to_xml
from faststrap.components.navigation import Navbar



def test_navbar_basic():
    """Navbar renders with basic content."""
    navbar = Navbar(A("Home", href="/", cls="nav-link"))
    html = to_xml(navbar)

    assert "navbar" in html
    assert "Home" in html


def test_navbar_with_brand():
    """Navbar can have a brand."""
    navbar = Navbar(A("Link", href="/"), brand="MyApp")
    html = to_xml(navbar)

    assert "MyApp" in html
    assert "navbar-brand" in html


def test_navbar_brand_href():
    """Navbar brand link is customizable."""
    navbar = Navbar(A("Link", href="/"), brand="Logo", brand_href="/home")
    html = to_xml(navbar)

    assert 'href="/home"' in html


def test_navbar_variants():
    """Navbar supports light and dark variants."""
    for variant in ["light", "dark"]:
        navbar = Navbar(A("Link", href="/"), variant=variant)
        html = to_xml(navbar)
        assert f"navbar-{variant}" in html


def test_navbar_background():
    """Navbar can have background color."""
    navbar = Navbar(A("Link", href="/"), bg="primary")
    html = to_xml(navbar)

    assert "bg-primary" in html


def test_navbar_expand_breakpoints():
    """Navbar supports all expand breakpoints."""
    breakpoints = ["sm", "md", "lg", "xl", "xxl"]

    for bp in breakpoints:
        navbar = Navbar(A("Link", href="/"), expand=bp)
        html = to_xml(navbar)
        assert f"navbar-expand-{bp}" in html


def test_navbar_sticky():
    """Navbar can be sticky."""
    for position in ["top", "bottom"]:
        navbar = Navbar(A("Link", href="/"), sticky=position)
        html = to_xml(navbar)
        assert f"sticky-{position}" in html


def test_navbar_fixed():
    """Navbar can be fixed."""
    for position in ["top", "bottom"]:
        navbar = Navbar(A("Link", href="/"), fixed=position)
        html = to_xml(navbar)
        assert f"fixed-{position}" in html


def test_navbar_container():
    """Navbar wraps content in container by default."""
    navbar = Navbar(A("Link", href="/"))
    html = to_xml(navbar)

    assert "container" in html


def test_navbar_no_container():
    """Navbar can disable container."""
    navbar = Navbar(A("Link", href="/"), container=False)
    html = to_xml(navbar)

    # Should have navbar but not wrapped in container
    assert "navbar" in html
    # Container should not be a direct wrapper (might be in children)
    assert '<div class="container"' not in html[:200]


def test_navbar_container_responsive():
    """Navbar supports responsive containers."""
    navbar = Navbar(A("Link", href="/"), container="lg")
    html = to_xml(navbar)

    assert "container-lg" in html


def test_navbar_toggler():
    """Navbar includes toggler for mobile."""
    navbar = Navbar(A("Link", href="/"), brand="App", expand="lg")
    html = to_xml(navbar)

    assert "navbar-toggler" in html
    assert "navbar-toggler-icon" in html
    assert 'data-bs-toggle="collapse"' in html


def test_navbar_collapse():
    """Navbar includes collapsible section."""
    navbar = Navbar(A("Link", href="/"), expand="lg")
    html = to_xml(navbar)

    assert "collapse navbar-collapse" in html


def test_navbar_custom_classes():
    """Navbar merges custom classes."""
    navbar = Navbar(A("Link", href="/"), cls="custom-navbar shadow")
    html = to_xml(navbar)

    assert "navbar" in html
    assert "custom-navbar" in html
    assert "shadow" in html


def test_navbar_full_configuration():
    """Navbar with all options works correctly."""
    navbar = Navbar(
        A("Home", href="/", cls="nav-link"),
        A("About", href="/about", cls="nav-link"),
        brand="MyApp",
        brand_href="/",
        variant="dark",
        bg="primary",
        expand="lg",
        sticky="top"
    )
    html = to_xml(navbar)

    assert "MyApp" in html
    assert "Home" in html
    assert "About" in html
    assert "navbar-dark" in html
    assert "bg-primary" in html
    assert "navbar-expand-lg" in html
    assert "sticky-top" in html
