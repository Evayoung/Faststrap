"""Tests for faststrap.core.effects module."""

from faststrap.core.effects import Fx


def test_fx_base_constant():
    """Test that Fx.base returns correct class name."""
    assert Fx.base == "fx"


def test_fx_entrance_animations():
    """Test that entrance animation constants return correct class names."""
    assert Fx.fade_in == "fx-fade-in"
    assert Fx.fade_in_up == "fx-slide-up"
    assert Fx.fade_in_down == "fx-slide-down"
    assert Fx.zoom_in == "fx-zoom-in"
    assert Fx.slide_right == "fx-slide-right"
    assert Fx.slide_left == "fx-slide-left"


def test_fx_hover_interactions():
    """Test that hover interaction constants return correct class names."""
    assert Fx.hover_lift == "fx-hover-lift"
    assert Fx.hover_scale == "fx-hover-scale"
    assert Fx.hover_glow == "fx-hover-glow"
    assert Fx.hover_colorize == "fx-hover-colorize"


def test_fx_loading_states():
    """Test that loading state constants return correct class names."""
    assert Fx.spin == "fx-spin"
    assert Fx.pulse == "fx-pulse"
    assert Fx.shimmer == "fx-shimmer"


def test_fx_speed_modifiers():
    """Test that speed modifier constants return correct class names."""
    assert Fx.fast == "fx-fast"
    assert Fx.slow == "fx-slow"
    assert Fx.slower == "fx-slower"


def test_fx_delay_modifiers():
    """Test that delay modifier constants return correct class names."""
    assert Fx.delay_xs == "fx-delay-xs"
    assert Fx.delay_sm == "fx-delay-sm"
    assert Fx.delay_md == "fx-delay-md"
    assert Fx.delay_lg == "fx-delay-lg"
    assert Fx.delay_xl == "fx-delay-xl"


def test_fx_usage_with_components():
    """Test that Fx classes can be used with components."""
    from faststrap import Card

    card = Card("Content", cls=[Fx.base, Fx.fade_in, Fx.hover_lift])
    html = str(card)

    assert "fx" in html
    assert "fx-fade-in" in html
    assert "fx-hover-lift" in html


def test_fx_multiple_effects_combination():
    """Test combining multiple effects on a single component."""
    from faststrap import Button

    button = Button(
        "Animated Button",
        cls=[Fx.base, Fx.fade_in_up, Fx.hover_scale, Fx.fast, Fx.delay_sm],
    )
    html = str(button)

    assert "fx" in html
    assert "fx-slide-up" in html
    assert "fx-hover-scale" in html
    assert "fx-fast" in html
    assert "fx-delay-sm" in html
