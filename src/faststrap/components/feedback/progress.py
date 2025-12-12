"""Bootstrap Progress component for progress bars."""

from typing import Any, Literal

from fasthtml.common import Div

from ...core.base import merge_classes
from ...utils.attrs import convert_attrs

VariantType = Literal[
    "primary", "secondary", "success", "danger", "warning", "info", "light", "dark"
]


def Progress(
    value: int,
    max_value: int = 100,
    variant: VariantType | None = None,
    striped: bool = False,
    animated: bool = False,
    label: str | None = None,
    height: str | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Progress component for progress bars.

    Args:
        value: Current progress value
        max_value: Maximum value (default 100)
        variant: Bootstrap color variant
        striped: Use striped style
        animated: Animate stripes (requires striped=True)
        label: Label text to display (e.g., "75%")
        height: Custom height (e.g., "20px", "1rem")
        **kwargs: Additional HTML attributes (cls, id, hx-*, etc.)

    Returns:
        Div element with progress bar

    Example:
        Simple progress:
        >>> Progress(75)

        Colored with label:
        >>> Progress(60, variant="success", label="60%")

        Striped:
        >>> Progress(45, variant="info", striped=True)

        Animated stripes:
        >>> Progress(80, variant="warning", striped=True, animated=True)

        Custom height:
        >>> Progress(90, height="30px", variant="primary", label="90%")

        Different variants:
        >>> Progress(25, variant="danger")
        >>> Progress(50, variant="warning")
        >>> Progress(75, variant="success")

        With HTMX updates:
        >>> Progress(
        ...     30,
        ...     variant="info",
        ...     id="upload-progress",
        ...     hx_get="/progress",
        ...     hx_trigger="every 1s",
        ...     hx_swap="outerHTML"
        ... )

        Zero to full:
        >>> Progress(0, variant="secondary")
        >>> Progress(100, variant="success", label="Complete!")

        Custom max value:
        >>> Progress(45, max_value=60, variant="primary", label="45/60")

    Note:
        - Value is clamped between 0 and max_value
        - Percentage calculated automatically
        - Animated requires striped=True to work

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/progress/
    """
    # Calculate percentage
    pct = min(100, max(0, (value / max_value) * 100))

    # Build bar classes
    bar_classes = ["progress-bar"]

    if variant:
        bar_classes.append(f"bg-{variant}")

    if striped:
        bar_classes.append("progress-bar-striped")

    if animated:
        bar_classes.append("progress-bar-animated")

    # Create progress bar
    bar = Div(
        label or "",
        cls=" ".join(bar_classes),
        role="progressbar",
        aria_valuenow=value,
        aria_valuemin=0,
        aria_valuemax=max_value,
        style=f"width: {pct}%",
    )

    # Build wrapper
    user_cls = kwargs.pop("cls", "")
    wrapper_cls = merge_classes("progress", user_cls)

    wrapper_attrs: dict[str, Any] = {"cls": wrapper_cls}

    if height:
        wrapper_attrs["style"] = f"height: {height}"

    # Convert remaining kwargs (HTMX, data-*, etc.)
    wrapper_attrs.update(convert_attrs(kwargs))

    return Div(bar, **wrapper_attrs)


def ProgressBar(
    value: int,
    max_value: int = 100,
    variant: VariantType | None = None,
    striped: bool = False,
    animated: bool = False,
    label: str | None = None,
    **kwargs: Any,
) -> Div:
    """Individual progress bar for stacked progress bars.

    Args:
        value: Current progress value
        max_value: Maximum value
        variant: Bootstrap color variant
        striped: Use striped style
        animated: Animate stripes
        label: Label text
        **kwargs: Additional HTML attributes

    Returns:
        Div element with progress-bar class (without wrapper)

    Example:
        Single bar (use in custom container):
        >>> ProgressBar(25, variant="success")

        Stacked progress bars:
        >>> Div(
        ...     ProgressBar(15, variant="success"),
        ...     ProgressBar(30, variant="info"),
        ...     ProgressBar(20, variant="warning"),
        ...     cls="progress"
        ... )

        Multi-colored with labels:
        >>> Div(
        ...     ProgressBar(30, variant="success", label="30%"),
        ...     ProgressBar(20, variant="warning", label="20%"),
        ...     ProgressBar(45, variant="danger", label="45%"),
        ...     cls="progress",
        ...     style="height: 30px;"
        ... )

        Animated stack:
        >>> Div(
        ...     ProgressBar(25, variant="primary", striped=True, animated=True),
        ...     ProgressBar(35, variant="success", striped=True, animated=True),
        ...     ProgressBar(15, variant="info", striped=True, animated=True),
        ...     cls="progress"
        ... )

        Storage usage example:
        >>> Div(
        ...     ProgressBar(40, variant="success", label="Documents"),
        ...     ProgressBar(25, variant="info", label="Photos"),
        ...     ProgressBar(20, variant="warning", label="Videos"),
        ...     ProgressBar(15, variant="danger", label="Other"),
        ...     cls="progress",
        ...     style="height: 25px;"
        ... )

    Note:
        - Must be wrapped in .progress container
        - Use Progress() for single bars (includes wrapper)
        - Percentages should sum to ≤100 for visual accuracy

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/progress/#multiple-bars
    """
    # Calculate percentage
    pct = min(100, max(0, (value / max_value) * 100))

    # Build classes
    classes = ["progress-bar"]

    if variant:
        classes.append(f"bg-{variant}")

    if striped:
        classes.append("progress-bar-striped")

    if animated:
        classes.append("progress-bar-animated")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    cls = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {
        "cls": cls,
        "role": "progressbar",
        "aria_valuenow": value,
        "aria_valuemin": 0,
        "aria_valuemax": max_value,
        "style": f"width: {pct}%",
    }

    # Convert remaining kwargs (HTMX, data-*, etc.)
    attrs.update(convert_attrs(kwargs))

    return Div(label or "", **attrs)
