"""Bootstrap Select component for dropdown selections."""

from typing import Any, Literal

from fasthtml.common import Div, Label, Option, Small
from fasthtml.common import Select as FTSelect

from ...core.base import merge_classes
from ...utils.attrs import convert_attrs

SizeType = Literal["sm", "lg"]


def Select(
    name: str,
    *options: tuple[str, str] | tuple[str, str, bool],
    label: str | None = None,
    help_text: str | None = None,
    size: SizeType | None = None,
    disabled: bool = False,
    required: bool = False,
    multiple: bool = False,
    **kwargs: Any,
) -> Div:  # Div | FTSelect
    """Bootstrap Select component for dropdown selections.

    Args:
        name: Select name attribute
        *options: Options as (value, label) or (value, label, selected)
        label: Label text (if provided, wraps select in div)
        help_text: Helper text below select
        size: Select size (sm, lg)
        disabled: Whether select is disabled
        required: Whether select is required
        multiple: Allow multiple selections
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        Div with label/select/help or just Select element

    Example:
        Simple select:
        >>> Select(
        ...     "country",
        ...     ("us", "United States"),
        ...     ("uk", "United Kingdom"),
        ...     ("ca", "Canada")
        ... )

        With default selection:
        >>> Select(
        ...     "size",
        ...     ("s", "Small"),
        ...     ("m", "Medium", True),
        ...     ("l", "Large"),
        ...     label="Select Size",
        ...     required=True
        ... )

        Multiple select:
        >>> Select(
        ...     "tags",
        ...     ("python", "Python"),
        ...     ("js", "JavaScript"),
        ...     ("go", "Go"),
        ...     ("rust", "Rust"),
        ...     multiple=True,
        ...     label="Choose Technologies",
        ...     help_text="Hold Ctrl/Cmd to select multiple"
        ... )

        With HTMX:
        >>> Select(
        ...     "category",
        ...     ("tech", "Technology"),
        ...     ("health", "Health"),
        ...     ("finance", "Finance"),
        ...     label="Category",
        ...     hx_get="/filter",
        ...     hx_trigger="change",
        ...     hx_target="#results"
        ... )

        Large size:
        >>> Select(
        ...     "priority",
        ...     ("low", "Low"),
        ...     ("medium", "Medium"),
        ...     ("high", "High"),
        ...     size="lg",
        ...     label="Priority Level"
        ... )

    Note:
        - Selected option marked with True in tuple
        - Multiple mode allows Ctrl/Cmd+click selection
        - Proper accessibility with label linkage

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/forms/select/
    """
    # Ensure ID for label linkage
    select_id = kwargs.pop("id", name)

    # Build select classes
    classes = ["form-select"]
    if size:
        classes.append(f"form-select-{size}")

    user_cls = kwargs.pop("cls", "")
    cls = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {
        "cls": cls,
        "name": name,
        "id": select_id,
    }

    if disabled:
        attrs["disabled"] = True

    if required:
        attrs["required"] = True

    if multiple:
        attrs["multiple"] = True

    # ARIA for help text
    if help_text:
        attrs["aria_describedby"] = f"{select_id}-help"

    # Convert remaining kwargs (HTMX, data-*, etc.)
    attrs.update(convert_attrs(kwargs))

    # Process options
    option_nodes: list[Any] = []
    for item in options:
        is_selected = False

        if len(item) == 3:
            value, label_text, is_selected = item
        elif len(item) == 2:
            value, label_text = item
        else:
            raise ValueError(
                f"Option must be (value, label) or (value, label, selected), got {item}"
            )

        opt_attrs: dict[str, Any] = {"value": value}
        if is_selected:
            opt_attrs["selected"] = True

        option_nodes.append(Option(label_text, **opt_attrs))

    # Create select element
    select_el = FTSelect(*option_nodes, **attrs)

    # If just select (no label/help), return select only
    if not label and not help_text:
        return select_el

    # Wrap in div with label and help text
    nodes: list[Any] = []

    if label:
        nodes.append(
            Label(
                label,
                " ",
                Small("*", cls="text-danger") if required else "",
                **{"for": select_id},
                cls="form-label",
            )
        )

    nodes.append(select_el)

    if help_text:
        help_id = f"{select_id}-help"
        nodes.append(Small(help_text, cls="form-text text-muted", id=help_id))

    return Div(*nodes, cls="mb-3")
