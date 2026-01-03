"""
Faststrap Effects Module (Zero-JS)

This module provides the `Fx` helper class, which exposes standard CSS classes
for animations, transitions, and micro-interactions defined in `faststrap-fx.css`.

Usage:
    from faststrap import Card, Fx

    Card(..., cls=[Fx.base, Fx.fade_in, Fx.hover_lift])
"""


class Fx:
    """
    Zero-JS Effects Helper.
    Combines with `cls` argument in FastHTML components.
    """

    # --------------------------------------------------------------------------
    # 1. Base Class (Required for transitions to work properly)
    # --------------------------------------------------------------------------
    base = "fx"

    # --------------------------------------------------------------------------
    # 2. Entrance Animations (Appear on load/swap)
    # --------------------------------------------------------------------------
    fade_in = "fx-fade-in"
    slide_up = "fx-slide-up"  # Roadmap compliant
    slide_down = "fx-slide-down"  # Roadmap compliant
    slide_left = "fx-slide-left"  # Roadmap compliant
    slide_right = "fx-slide-right"  # Roadmap compliant
    zoom_in = "fx-zoom-in"
    bounce_in = "fx-bounce-in"  # New

    # Contextual aliases for backward compatibility or clearer intent
    fade_in_up = slide_up
    fade_in_down = slide_down

    # --------------------------------------------------------------------------
    # 3. Hover Interactions (Trigger on mouseover)
    # --------------------------------------------------------------------------
    hover_lift = "fx-hover-lift"
    hover_scale = "fx-hover-scale"
    hover_glow = "fx-hover-glow"
    hover_tilt = "fx-hover-tilt"  # New
    hover_colorize = "fx-hover-colorize"

    # --------------------------------------------------------------------------
    # 4. Loading States (For hx-indicator)
    # --------------------------------------------------------------------------
    spin = "fx-spin"
    pulse = "fx-pulse"
    shimmer = "fx-shimmer"

    # --------------------------------------------------------------------------
    # 5. Visual Effects (Glass, Shadows)
    # --------------------------------------------------------------------------
    glass = "fx-glass"
    shadow_soft = "fx-shadow-soft"
    shadow_sharp = "fx-shadow-sharp"
    gradient_shift = "fx-gradient-shift"

    # --------------------------------------------------------------------------
    # 6. Modifiers (Tokens)
    # --------------------------------------------------------------------------
    # Speed
    fast = "fx-fast"  # 150ms
    slow = "fx-slow"  # 500ms
    slower = "fx-slower"  # 1000ms

    # Delay
    delay_xs = "fx-delay-xs"  # 100ms
    delay_sm = "fx-delay-sm"  # 200ms
    delay_md = "fx-delay-md"  # 300ms
    delay_lg = "fx-delay-lg"  # 500ms
    delay_xl = "fx-delay-xl"  # 1000ms
