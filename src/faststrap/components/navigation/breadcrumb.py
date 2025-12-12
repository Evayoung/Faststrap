"""Bootstrap Breadcrumb component for navigation trail."""

from typing import Any

from fasthtml.common import A, Li, Nav, Ol

from ...core.base import merge_classes
from ...utils.attrs import convert_attrs


def Breadcrumb(
    *items: tuple[Any, str | None] | tuple[Any, str | None, bool],
    **kwargs: Any,
) -> Nav:
    """Bootstrap Breadcrumb component for navigation trail.

    Args:
        *items: Breadcrumb items as (label, href) or (label, href, active)
        **kwargs: Additional HTML attributes (cls, id, hx-*, etc.)

    Returns:
        Nav element with breadcrumb

    Example:
        Simple breadcrumb:
        >>> Breadcrumb(
        ...     ("Home", "/"),
        ...     ("Library", "/library"),
        ...     ("Data", None)
        ... )

        With icons:
        >>> from faststrap import Icon
        >>> Breadcrumb(
        ...     (Icon("house-fill"), "/"),
        ...     ("Products", "/products"),
        ...     ("Electronics", "/products/electronics"),
        ...     ("Laptops", None)
        ... )

        Custom styling:
        >>> Breadcrumb(
        ...     ("Dashboard", "/dashboard"),
        ...     ("Settings", "/settings"),
        ...     ("Profile", None),
        ...     cls="bg-light p-3 rounded"
        ... )

        With HTMX:
        >>> Breadcrumb(
        ...     ("Home", "/", False),
        ...     ("Products", None, True),
        ...     hx_boost="true",
        ...     hx_target="#content"
        ... )

        Explicit active item:
        >>> Breadcrumb(
        ...     ("Level 1", "/level1"),
        ...     ("Level 2", "/level2"),
        ...     ("Level 3", None, True)
        ... )

    Note:
        - Last item is automatically active if not specified
        - Active items have no href (None)
        - Supports any element as label (text, Icon, Div, etc.)

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/breadcrumb/
    """
    crumbs: list[Any] = []
    last_idx = len(items) - 1

    for idx, item in enumerate(items):
        # Parse item tuple
        if len(item) == 3:
            label, href, active = item
        elif len(item) == 2:
            label, href = item
            active = idx == last_idx  # Last item active by default
        else:
            raise ValueError(
                f"Breadcrumb item must be (label, href) or (label, href, active), got {item}"
            )

        # Build item classes
        item_cls = "breadcrumb-item" + (" active" if active else "")

        # Create crumb
        if active or href is None:
            # Active item (no link)
            crumbs.append(Li(label, cls=item_cls, aria_current="page"))
        else:
            # Linked item
            crumbs.append(Li(A(label, href=href), cls=item_cls))

    # Build breadcrumb
    user_cls = kwargs.pop("cls", "")
    ol_cls = merge_classes("breadcrumb", user_cls)

    # Convert remaining kwargs (HTMX, data-*, etc.)
    nav_attrs: dict[str, Any] = {"aria_label": "breadcrumb"}
    nav_attrs.update(convert_attrs(kwargs))

    return Nav(Ol(*crumbs, cls=ol_cls), **nav_attrs)
