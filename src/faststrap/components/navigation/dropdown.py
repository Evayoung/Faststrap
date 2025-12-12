"""Bootstrap Dropdown component for Faststrap."""

from typing import Any, Literal

from fasthtml.common import A, Button, Div, Li, Ul

from ...core.base import merge_classes
from ...utils.attrs import convert_attrs

VariantType = Literal[
    "primary", "secondary", "success", "danger", "warning", "info", "light", "dark"
]

DirectionType = Literal["down", "up", "start", "end"]


def Dropdown(
    *items: Any,
    label: str = "Dropdown",
    variant: VariantType = "primary",
    size: Literal["sm", "lg"] | None = None,
    split: bool = False,
    direction: DirectionType = "down",
    **kwargs: Any,
) -> Div:
    """Bootstrap Dropdown component for contextual menus.

    Args:
        *items: Dropdown menu items (strings, A elements, or "---" for dividers)
        label: Button label text
        variant: Bootstrap button variant
        size: Button size
        split: Use split button style
        direction: Dropdown direction (down, up, start=left, end=right)
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        Div containing dropdown button and menu

    Example:
        Basic dropdown:
        >>> Dropdown(
        ...     "Action",
        ...     "Another action",
        ...     "---",  # Divider
        ...     "Separated link",
        ...     label="Actions"
        ... )

        Split button:
        >>> Dropdown(
        ...     "Edit",
        ...     "Delete",
        ...     label="Options",
        ...     split=True,
        ...     variant="success"
        ... )

        Dropup:
        >>> Dropdown(
        ...     "Item 1",
        ...     "Item 2",
        ...     label="Dropup",
        ...     direction="up"
        ... )

        With HTMX:
        >>> Dropdown(
        ...     A("Load More", hx_get="/items", hx_target="#content"),
        ...     "Settings",
        ...     label="Menu"
        ... )

    Note:
        - Items can be strings (converted to links) or A/Button elements
        - Use "---" string for dividers between items
        - Supports all Bootstrap dropdown features

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/dropdowns/
    """
    # ---- Container classes ------------------------------------------------ #
    container_classes = []

    container_classes.append(
        {
            "up": "dropup",
            "start": "dropstart",
            "end": "dropend",
            "down": "dropdown",
        }[direction]
    )

    if split:
        container_classes.append("btn-group")

    # ---- Button classes --------------------------------------------------- #
    btn_classes = ["btn", f"btn-{variant}"]
    if size:
        btn_classes.append(f"btn-{size}")

    btn_class_str = " ".join(btn_classes)

    toggle_id = kwargs.pop("id", "dropdownMenuButton")

    # ---- Build buttons ---------------------------------------------------- #
    buttons: list[Any] = []

    if split:
        # Action button (left)
        buttons.append(Button(label, cls=btn_class_str, type="button"))

        # Toggle (right)
        buttons.append(
            Button(
                "",  # Empty for split
                cls=merge_classes(btn_class_str, "dropdown-toggle dropdown-toggle-split"),
                type="button",
                id=toggle_id,
                data_bs_toggle="dropdown",
                aria_expanded="false",
            )
        )
    else:
        buttons.append(
            Button(
                label,
                cls=merge_classes(btn_class_str, "dropdown-toggle"),
                type="button",
                id=toggle_id,
                data_bs_toggle="dropdown",
                aria_expanded="false",
            )
        )

    # ---- Build dropdown items -------------------------------------------- #
    menu_items: list[Any] = []

    for item in items:
        # Check for divider string
        if isinstance(item, str) and item == "---":
            menu_items.append(Li(cls="dropdown-divider"))
            continue

        # Check for hr element by name attribute
        if hasattr(item, "name") and item.name == "hr":
            menu_items.append(Li(cls="dropdown-divider"))
            continue

        # String -> <a>
        if isinstance(item, str):
            menu_items.append(
                Li(
                    A(
                        item,
                        cls="dropdown-item",
                        href="#",
                        role="menuitem",
                    )
                )
            )
            continue

        # A / Button elements
        if hasattr(item, "name") and item.name in {"a", "button"}:
            cls = merge_classes("dropdown-item", item.attrs.get("cls", ""))
            # Clone the element with updated class
            cloned_attrs = {**item.attrs, "cls": cls}
            cloned = item.__class__(*item.children, **cloned_attrs)
            menu_items.append(Li(cloned))
            continue

        # Fallback wrapper
        menu_items.append(Li(item, cls="dropdown-item"))

    # ---- Build menu -------------------------------------------------------- #
    menu = Ul(
        *menu_items,
        cls="dropdown-menu",
        role="menu",
        aria_labelledby=toggle_id,
    )

    # ---- Final container --------------------------------------------------- #
    user_cls = kwargs.pop("cls", "")
    container_cls = merge_classes(" ".join(container_classes), user_cls)

    attrs: dict[str, Any] = {"cls": container_cls}
    attrs.update(convert_attrs(kwargs))

    return Div(*buttons, menu, **attrs)


def DropdownItem(
    *children: Any,
    active: bool = False,
    disabled: bool = False,
    **kwargs: Any,
) -> A:
    """Dropdown item helper.

    Args:
        *children: Item content
        active: Whether item is active
        disabled: Whether item is disabled
        **kwargs: Additional HTML attributes

    Returns:
        A element with dropdown-item class

    Example:
        >>> DropdownItem("Action")
        >>> DropdownItem("Active Item", active=True)
        >>> DropdownItem("Disabled", disabled=True)
    """
    classes = ["dropdown-item"]
    if active:
        classes.append("active")
    if disabled:
        classes.append("disabled")

    cls_str = merge_classes(" ".join(classes), kwargs.pop("cls", ""))

    attrs: dict[str, Any] = {
        "cls": cls_str,
        "role": "menuitem",
    }

    if disabled:
        attrs["aria_disabled"] = "true"
        attrs["tabindex"] = "-1"

    if "href" not in kwargs:
        attrs["href"] = "#"

    attrs.update(convert_attrs(kwargs))

    return A(*children, **attrs)


def DropdownDivider() -> Li:
    """Divider helper.

    Returns:
        Li element with dropdown-divider class

    Example:
        >>> DropdownDivider()
    """
    return Li(cls="dropdown-divider")
