"""Bootstrap [ComponentName] for [purpose].

This is a TEMPLATE file. Copy this to components/category/your_component.py
and customize it for your component.
"""

from typing import Any, Literal

from fasthtml.common import Div  # Or appropriate FT type

# NOTE: When copying this template, adjust the import path:
# from ...core.base import merge_classes
# from ...utils.attrs import convert_attrs

# For template validation only (remove when using):
try:
    from faststrap.core.base import merge_classes
    from faststrap.utils.attrs import convert_attrs
except ImportError:
    # Fallback for when template is used standalone
    def merge_classes(*args: str | None) -> str:  # type: ignore
        """Placeholder - use real implementation."""
        return " ".join(str(c) for c in args if c)

    def convert_attrs(kwargs: dict[str, Any]) -> dict[str, Any]:  # type: ignore
        """Placeholder - use real implementation."""
        return kwargs


# Type aliases
VariantType = Literal[
    "primary", "secondary", "success", "danger", "warning", "info", "light", "dark"
]


def ComponentName(
    *children: Any,
    variant: VariantType = "primary",
    **kwargs: Any,
) -> Div:
    """Bootstrap [ComponentName] component.

    Args:
        *children: Component content
        variant: Bootstrap color variant
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Div element

    Example:
        Basic:
        >>> ComponentName("Content", variant="success")

        With HTMX:
        >>> ComponentName("Load", hx_get="/api", hx_target="#result")

        Custom styling:
        >>> ComponentName("Custom", cls="mt-3 shadow")

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/[name]/
    """
    # Build classes
    classes = ["component-base", f"component-{variant}"]

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    return Div(*children, **attrs)
