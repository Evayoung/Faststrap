"""Bootstrap Spinner component for loading indicators."""

from typing import Any, Literal

from fasthtml.common import Div, Span

from ...core.base import merge_classes
from ...utils.attrs import convert_attrs

SpinnerType = Literal["border", "grow"]
VariantType = Literal[
    "primary", "secondary", "success", "danger", "warning", "info", "light", "dark"
]


def Spinner(
    spinner_type: SpinnerType = "border",
    variant: VariantType | None = None,
    size: Literal["sm"] | None = None,
    label: str = "Loading...",
    **kwargs: Any,
) -> Div:
    """Bootstrap Spinner component for loading indicators.

    Args:
        spinner_type: Spinner animation type ("border" or "grow")
        variant: Bootstrap color variant
        size: Spinner size (only "sm" supported)
        label: Screen reader label text
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        Div element with spinner animation

    Example:
        Basic spinner:
        >>> Spinner()

        Colored spinners:
        >>> Spinner(variant="primary")
        >>> Spinner(variant="success")
        >>> Spinner(variant="danger")

        Growing spinner:
        >>> Spinner(spinner_type="grow", variant="info")

        Small spinner:
        >>> Spinner(size="sm", variant="secondary")

        In button:
        >>> Button(
        ...     Spinner(size="sm", label="Saving..."),
        ...     " Saving...",
        ...     variant="primary",
        ...     disabled=True
        ... )

        With custom label:
        >>> Spinner(
        ...     variant="warning",
        ...     label="Processing your request..."
        ... )

        Multiple spinners:
        >>> Div(
        ...     Spinner(variant="primary", cls="me-2"),
        ...     Spinner(spinner_type="grow", variant="success", cls="me-2"),
        ...     Spinner(variant="danger", size="sm")
        ... )

        Loading state with HTMX:
        >>> Div(
        ...     Button("Load Data", hx_get="/data", hx_target="#content"),
        ...     Div(
        ...         Spinner(variant="primary"),
        ...         cls="htmx-indicator"
        ...     )
        ... )

        Custom styling:
        >>> Spinner(
        ...     variant="primary",
        ...     cls="position-absolute top-50 start-50"
        ... )

    Note:
        - Spinners are inline-block by default
        - Use size="sm" for smaller spinners in buttons
        - Label text is visually hidden but read by screen readers
        - Growing spinners use scaling animation instead of border

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/spinners/
    """
    # Build spinner classes
    classes = [f"spinner-{spinner_type}"]

    if variant:
        classes.append(f"text-{variant}")

    if size == "sm":
        classes.append(f"spinner-{spinner_type}-sm")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    cls = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {
        "cls": cls,
        "role": "status",
    }

    # Convert remaining kwargs (HTMX, data-*, etc.)
    attrs.update(convert_attrs(kwargs))

    # Screen reader text
    sr_text = Span(label, cls="visually-hidden")

    return Div(sr_text, **attrs)
