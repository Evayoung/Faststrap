"""Bootstrap Toast component for temporary notifications."""

from typing import Any, Literal

from fasthtml.common import Button, Div, Strong

from ...core.base import merge_classes

VariantType = Literal[
    "primary",
    "secondary",
    "success",
    "danger",
    "warning",
    "info",
    "light",
    "dark",
]


def _convert_attrs(kwargs: dict[str, Any]) -> dict[str, Any]:
    """Convert Python kwargs to HTML attributes (hx_get → hx-get)."""
    converted = {}
    for k, v in kwargs.items():
        if k.startswith("hx_") or k.startswith("data_") or k.startswith("aria_"):
            converted[k.replace("_", "-")] = v
        elif k == "cls":
            converted[k] = v
        else:
            converted[k.replace("_", "-")] = v
    return converted


def Toast(
    *children: Any,
    title: str | None = None,
    variant: VariantType | None = None,
    autohide: bool = True,
    delay: int = 5000,
    animation: bool = True,
    **kwargs: Any,
) -> Div:
    """Bootstrap Toast component for temporary notifications.

    Args:
        *children: Toast body content
        title: Toast header title
        variant: Bootstrap color variant (applies background color)
        autohide: Automatically hide toast after delay
        delay: Auto-hide delay in milliseconds (default: 5000ms / 5s)
        animation: Enable fade animation
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Div element with toast structure

    Example:
        Basic toast:
        >>> Toast("Operation successful!", title="Success")

        With variant color:
        >>> Toast(
        ...     "Your changes were saved.",
        ...     title="Saved",
        ...     variant="success"
        ... )

        No auto-hide:
        >>> Toast(
        ...     "Important message - stays visible",
        ...     title="Notice",
        ...     autohide=False
        ... )

        Custom delay:
        >>> Toast(
        ...     "Quick notification",
        ...     title="Alert",
        ...     delay=2000  # 2 seconds
        ... )

    Note:
        Toasts require Bootstrap's JavaScript to work.
        
        To show a toast programmatically:
        - Add it to the page (hidden by default)
        - Use Bootstrap's Toast API: `toast.show()` via JavaScript
        
        Or use HTMX to dynamically add toasts:
        >>> Button("Show Toast", hx_get="/toast", hx_target="#toast-container")

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/toasts/
    """
    # Build base classes
    classes = ["toast"]

    # Add variant background if specified
    if variant:
        classes.append(f"text-bg-{variant}")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build data attributes for Bootstrap JS
    attrs: dict[str, Any] = {
        "cls": all_classes,
        "role": "alert",
        "aria-live": "assertive",
        "aria-atomic": "true",
    }

    # Bootstrap toast data attributes
    if autohide:
        attrs["data-bs-autohide"] = "true"
        attrs["data-bs-delay"] = str(delay)
    else:
        attrs["data-bs-autohide"] = "false"

    if animation:
        attrs["data-bs-animation"] = "true"

    # Convert remaining kwargs
    attrs.update(_convert_attrs(kwargs))

    # Build toast structure
    parts = []

    # Add header if title provided
    if title:
        header = Div(
            Strong(title, cls="me-auto"),
            Button(
                type="button",
                cls="btn-close",
                data_bs_dismiss="toast",
                aria_label="Close",
            ),
            cls="toast-header",
        )
        parts.append(header)

    # Add body
    body = Div(*children, cls="toast-body")
    parts.append(body)

    return Div(*parts, **attrs)


def ToastContainer(
    *toasts: Any,
    position: Literal[
        "top-start",
        "top-center",
        "top-end",
        "middle-start",
        "middle-center",
        "middle-end",
        "bottom-start",
        "bottom-center",
        "bottom-end",
    ] = "top-end",
    **kwargs: Any,
) -> Div:
    """Container for positioning toasts on the page.

    Args:
        *toasts: Toast components to display
        position: Toast position on screen
        **kwargs: Additional HTML attributes

    Returns:
        FastHTML Div element positioned for toasts

    Example:
        >>> ToastContainer(
        ...     Toast("Message 1", title="Alert 1"),
        ...     Toast("Message 2", title="Alert 2"),
        ...     position="top-end"
        ... )

    Note:
        Position the container fixed on the page:
        - top-start: Top left
        - top-center: Top center
        - top-end: Top right (default)
        - middle-*: Vertically centered
        - bottom-*: Bottom aligned
    """
    # Build position classes
    classes = ["toast-container", "position-fixed", "p-3"]

    # Map position to CSS classes
    position_map = {
        "top-start": "top-0 start-0",
        "top-center": "top-0 start-50 translate-middle-x",
        "top-end": "top-0 end-0",
        "middle-start": "top-50 start-0 translate-middle-y",
        "middle-center": "top-50 start-50 translate-middle",
        "middle-end": "top-50 end-0 translate-middle-y",
        "bottom-start": "bottom-0 start-0",
        "bottom-center": "bottom-0 start-50 translate-middle-x",
        "bottom-end": "bottom-0 end-0",
    }

    classes.append(position_map[position])

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(_convert_attrs(kwargs))

    return Div(*toasts, **attrs)