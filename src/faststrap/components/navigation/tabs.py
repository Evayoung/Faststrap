"""Bootstrap Tabs component for Faststrap.

Implements:
- Tabs navigation (tabs / pills)
- Vertical tabs (uses Bootstrap Grid for side-by-side layout)
- Optional HTMX integration (disables conflicting Bootstrap JS)
- Compatible with TabPane for content management
"""

from typing import Any, Literal

from fasthtml.common import Button, Div, Li, Ul

# Assuming these are the correct relative imports based on your structure
from ...core.base import merge_classes
from ...utils.attrs import convert_attrs

TabType = Literal["tabs", "pills"]


def Tabs(
    *items: tuple[str, Any, bool] | tuple[str, Any],
    variant: TabType = "tabs",
    justified: bool = False,
    fill: bool = False,
    vertical: bool = False,
    htmx: bool = False,
    **kwargs: Any,
) -> Div:
    """
    Bootstrap Tabs navigation component.

    Args:
        *items: Tuples of (id, label) or (id, label, active)
        variant: 'tabs' or 'pills'
        justified: Make tabs full width
        fill: Proportionally fill width
        vertical: Stack tabs vertically and wrap in a grid layout (nav side-by-side with content).
        htmx: Enable HTMX-safe behavior (disables Bootstrap JS toggling: data-bs-toggle/target).
        **kwargs: Extra HTML attributes for the main <ul> element (cls, id, hx-*, data-*, etc.).

    Returns:
        Div containing the navigation list. Returns a Div(row, [col(nav), col(placeholder)])
        when `vertical=True`.
    Example:
        Basic tabs:
        >>> Tabs(
        ...     ("home", "Home", True),
        ...     ("profile", "Profile"),
        ...     ("contact", "Contact")
        ... )

        Pills style:
        >>> Tabs(
        ...     ("tab1", "Tab 1", True),
        ...     ("tab2", "Tab 2"),
        ...     variant="pills"
        ... )

        Vertical tabs:
        >>> Tabs(
        ...     ("v1", "Vertical 1", True),
        ...     ("v2", "Vertical 2"),
        ...     vertical=True
        ... )

        With HTMX content loading:
        >>> Tabs(
        ...     ("dynamic", A("Dynamic", hx_get="/content", hx_target="#tab-content")),
        ...     ("static", "Static")
        ... )

    Note:
        - First tab is active by default if no tab is marked active
        - Use data-bs-toggle="tab" for standard Bootstrap behavior
        - Content panes should have matching IDs

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/navs-tabs/
    """

    # ---- Nav CSS classes -------------------------------------------------- #
    nav_classes = ["nav"]
    nav_classes.append("nav-tabs" if variant == "tabs" else "nav-pills")

    if justified:
        nav_classes.append("nav-justified")
    if fill:
        nav_classes.append("nav-fill")
    if vertical:
        nav_classes.append("flex-column")

    # ---- Build nav items -------------------------------------------------- #
    nav_items = []
    has_active = False

    for idx, item in enumerate(items):
        if len(item) == 3:
            tab_id, label, is_active = item
        elif len(item) == 2:
            tab_id, label = item
            is_active = False
        else:
            raise ValueError("Tab item must be (id, label) or (id, label, active)")

        # First tab active fallback
        if idx == 0 and not has_active and not is_active:
            is_active = True

        if is_active:
            has_active = True

        # CRITICAL ARIA FIX: The button/link needs an ID for the pane's aria-labelledby
        btn_id = f"{tab_id}-tab"

        link_classes = merge_classes("nav-link", "active" if is_active else "")

        btn_attrs = {
            "cls": link_classes,
            "id": btn_id,  # ARIA linkage ID
            "type": "button",
            "role": "tab",
            "aria_controls": tab_id,
            "aria_selected": "true" if is_active else "false",
        }

        # HTMX Safety: Omit data-bs-* attributes if HTMX mode is enabled
        if not htmx:
            btn_attrs["data_bs_toggle"] = "tab"
            btn_attrs["data_bs_target"] = f"#{tab_id}"

        # Note: This implementation assumes the label is a simple string.
        # For complex labels (like an A tag with hx-get), the user must pass
        # an A tag with all required attrs (id, role, aria-*) manually applied.
        nav_link = Button(label, **btn_attrs)

        nav_items.append(Li(nav_link, cls="nav-item", role="presentation"))

    # ---- Build nav element ------------------------------------------------ #
    user_cls = kwargs.pop("cls", "")
    nav_cls = merge_classes(" ".join(nav_classes), user_cls)

    nav_attrs = {
        "cls": nav_cls,
        "role": "tablist",
    }
    nav_attrs.update(convert_attrs(kwargs))

    nav = Ul(*nav_items, **nav_attrs)

    # ---- Final Layout ------------------------------------------------------ #
    if vertical:
        # Returns the full Bootstrap row/col structure for vertical tabs.
        # It includes a Div(col) placeholder where the user must place the TabPane components.
        return Div(
            Div(nav, cls="col-auto"),
            # Placeholder column for the tab content panes (TabPane components)
            Div(cls="col"),
            cls="row g-0",  # 'g-0' removes gutter between nav and content
        )
    else:
        # Horizontal tabs only return the nav list wrapped in a Div.
        return Div(nav)


def TabPane(
    *children: Any,
    tab_id: str,
    active: bool = False,
    **kwargs: Any,
) -> Div:
    """
    Bootstrap tab content pane.

    Args:
        *children: Pane content
        tab_id: Unique ID matching the corresponding tab button's target ID
        active: Whether this pane is visible initially
        **kwargs: Additional HTML attributes
    Returns:
        Div with tab-pane classes
    Example:
        >>> TabPane("Home content", tab_id="home", active=True)
        >>> TabPane("Profile content", tab_id="profile")
    """

    classes = ["tab-pane", "fade"]
    if active:
        classes.extend(["show", "active"])

    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    attrs = {
        "cls": all_classes,
        "role": "tabpanel",
        "id": tab_id,
        # CRITICAL ARIA FIX: Link to the tab button's ID
        "aria-labelledby": f"{tab_id}-tab",
        "tabindex": "0",
    }

    attrs.update(convert_attrs(kwargs))

    return Div(*children, **attrs)
