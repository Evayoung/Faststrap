
"""Bootstrap Offcanvas (Drawer) component for side panels."""

from typing import Any, Literal

from fasthtml.common import Button, Div, H5

from ...core.base import merge_classes

PlacementType = Literal["start", "end", "top", "bottom"]


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


def Drawer(
    *children: Any,
    drawer_id: str,  # Using drawer_id to avoid conflict
    title: str | None = None,
    placement: PlacementType = "start",
    backdrop: bool = True,
    scroll: bool = False,
    **kwargs: Any,
) -> Div:
    """Bootstrap Offcanvas (Drawer) component for side panels and menus.

    Args:
        *children: Drawer body content
        drawer_id: Unique ID for the drawer (required for Bootstrap JS)
        title: Drawer header title
        placement: Drawer position (start=left, end=right, top, bottom)
        backdrop: Show backdrop overlay (default: True)
        scroll: Allow body scroll when drawer is open (default: False)
        **kwargs: Additional HTML attributes (cls, hx-*, data-*, etc.)

    Returns:
        FastHTML Div element with offcanvas structure

    Example:
        Left sidebar drawer:
        >>> Drawer(
        ...     Nav(
        ...         A("Home", href="/"),
        ...         A("About", href="/about"),
        ...         A("Contact", href="/contact")
        ...     ),
        ...     drawer_id="sidebar",
        ...     title="Menu",
        ...     placement="start"
        ... )

        Right drawer:
        >>> Drawer(
        ...     "Notifications here",
        ...     drawer_id="notifications",
        ...     title="Alerts",
        ...     placement="end"
        ... )

        No backdrop (allows interaction with page):
        >>> Drawer(
        ...     "Settings",
        ...     drawer_id="settings",
        ...     title="Settings",
        ...     backdrop=False,
        ...     scroll=True
        ... )

        Top drawer (full-width):
        >>> Drawer(
        ...     "Search results",
        ...     drawer_id="search",
        ...     title="Search",
        ...     placement="top"
        ... )

    Note:
        To trigger a drawer, use Bootstrap's data attributes:
        >>> Button("Open Menu", data_bs_toggle="offcanvas", data_bs_target="#sidebar")
        
        Or use HTMX to load drawer content dynamically:
        >>> Button("Load Drawer", hx_get="/drawer-content", hx_target="#drawerContainer")

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/offcanvas/
    """
    # Build offcanvas classes
    classes = ["offcanvas", f"offcanvas-{placement}"]

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes (WITHOUT id - we'll add it later)
    attrs: dict[str, Any] = {
        "cls": all_classes,
        "tabindex": "-1",
        "aria_labelledby": f"{drawer_id}Label",
    }

    # Configure backdrop and scroll
    if not backdrop:
        attrs["data_bs_backdrop"] = "false"

    if scroll:
        attrs["data_bs_scroll"] = "true"

    # Convert remaining kwargs (excluding drawer_id)
    converted_kwargs = _convert_attrs({k: v for k, v in kwargs.items() if k != 'drawer_id'})
    attrs.update(converted_kwargs)

    # Build drawer structure
    parts = []

    # Header
    if title:
        header = Div(
            H5(title, cls="offcanvas-title", id=f"{drawer_id}Label"),
            Button(
                type="button",
                cls="btn-close",
                data_bs_dismiss="offcanvas",
                aria_label="Close",
            ),
            cls="offcanvas-header",
        )
        parts.append(header)

    # Body
    body = Div(*children, cls="offcanvas-body")
    parts.append(body)

    # # Create the drawer with correct attrs including id
    # final_attrs = {"id": drawer_id, **attrs}
    # # return Div(*parts, **final_attrs)
    return Div(*parts, id=drawer_id, **attrs)
