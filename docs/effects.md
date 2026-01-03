# Zero-JS Visual Effects

Faststrap includes a lightweight, zero-dependency effects module (`faststrap-fx.css`) that provides smooth animations and interactions without writing any CSS or usage of JavaScript.

Because Faststrap is built on the philosophy of "Zero Custom JS", all effects are implemented using pure CSS transitions and animations, with full support for accessibility (prefers-reduced-motion).

## Usage

Import the `Fx` helper and add effect classes to your component's `cls` argument.

```python
from faststrap import Card, Fx, Button

# Clean & Readable
Card(
    "Content", 
    cls=[Fx.base, Fx.fade_in_up, Fx.hover_lift]
)
```

> [!IMPORTANT]
> Always include `Fx.base` when using hover interactions or modifiers. It sets up the CSS variables for transitions.

## Entrance Animations

Animations that play when the element enters the DOM (e.g., on page load or HTMX swap).

| Class | Python Helper | Effect |
|-------|---------------|--------|
| `fx-fade-in` | `Fx.fade_in` | Simple opacity fade |
| `fx-fade-in-up` | `Fx.fade_in_up` | Fades in while moving up |
| `fx-fade-in-down` | `Fx.fade_in_down` | Fades in while moving down |
| `fx-zoom-in` | `Fx.zoom_in` | Scales up from 95% to 100% |
| `fx-slide-in-right` | `Fx.slide_in_right` | Slides in from right |
| `fx-slide-in-left` | `Fx.slide_in_left` | Slides in from left |

## Hover Interactions

Micro-interactions that trigger when the user hovers over an element.

| Class | Python Helper | Effect |
|-------|---------------|--------|
| `fx-hover-lift` | `Fx.hover_lift` | Moves up 4px and adds shadow |
| `fx-hover-scale` | `Fx.hover_scale` | Scales up to 103% |
| `fx-hover-glow` | `Fx.hover_glow` | Adds a subtle primary-colored glow |
| `fx-hover-colorize` | `Fx.hover_colorize` | Starts grayscale, becomes colored on hover |

Example:
```python
Button(
    "Hover Me",
    cls=[Fx.base, Fx.hover_scale, Fx.hover_glow]
)
```

## Loading States

Perfect for `hx-indicator` or loading screens.

| Class | Python Helper | Effect |
|-------|---------------|--------|
| `fx-spin` | `Fx.spin` | Infinite rotation (good for icons) |
| `fx-pulse` | `Fx.pulse` | Opacity pulsing |
| `fx-shimmer` | `Fx.shimmer` | Skeleton loading shimmer effect |

Example:
```python
# Loading spinner icon
Icon("arrow-repeat", cls=[Fx.spin])

# Skeleton card
Card(
    cls=[Fx.shimmer],
    style={"height": "200px"}
)
```

## Modifiers

Customize the speed and delay of animations using token classes.

### Speed
| Class | Python Helper | Time |
|-------|---------------|------|
| `fx-fast` | `Fx.fast` | 150ms |
| `fx-slow` | `Fx.slow` | 500ms |
| `fx-slower` | `Fx.slower` | 1000ms |

### Delay
| Class | Python Helper | Time |
|-------|---------------|------|
| `fx-delay-xs` | `Fx.delay_xs` | 100ms |
| `fx-delay-sm` | `Fx.delay_sm` | 200ms |
| `fx-delay-md` | `Fx.delay_md` | 300ms |
| `fx-delay-lg` | `Fx.delay_lg` | 500ms |
| `fx-delay-xl` | `Fx.delay_xl` | 1000ms |

### Staggered Animations Example

```python
for i, item in enumerate(items):
    # Dynamically select delay
    delay = getattr(Fx, f"delay_{['xs','sm','md','lg'][i%4]}")
    
    Card(item.title, cls=[Fx.base, Fx.fade_in_up, delay])
```

## Accessibility

Faststrap respects `prefers-reduced-motion: reduce`. If a user has disabled OS animations, all transitions and animations are automatically disabled. This is built into the `faststrap-fx.css` core.
