
"""Bootstrap Modal component for dialog boxes."""

from typing import Any, Literal

from fasthtml.common import Button, Div, H5, Span

from ...core.base import merge_classes

SizeType = Literal["sm", "lg", "xl"]


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


def Modal(
    *children: Any,
    modal_id: str,  # Using modal_id to avoid conflict
    title: str | None = None,
    footer: Any | None = None,
    size: SizeType | None = None,
    centered: bool = False,
    scrollable: bool = False,
    fullscreen: bool | Literal["sm-down", "md-down", "lg-down", "xl-down", "xxl-down"] = False,
    static_backdrop: bool = False,
    **kwargs: Any,
) -> Div:
    """Bootstrap Modal component for dialog boxes and overlays.

    Args:
        *children: Modal body content
        modal_id: Unique ID for the modal (required for Bootstrap JS)
        title: Modal header title
        footer: Modal footer content (buttons, text, etc.)
        size: Modal size (sm, lg, xl)
        centered: Vertically center modal
        scrollable: Make modal body scrollable
        fullscreen: Full-screen modal (True or breakpoint like "md-down")
        static_backdrop: Clicking backdrop doesn't close modal
        **kwargs: Additional HTML attributes (cls, hx-*, data-*, etc.)

    Returns:
        FastHTML Div element with modal structure

    Example:
        Basic modal:
        >>> Modal(
        ...     P("Are you sure you want to delete this?"),
        ...     modal_id="deleteModal",
        ...     title="Confirm Delete",
        ...     footer=Div(
        ...         Button("Cancel", variant="secondary", data_bs_dismiss="modal"),
        ...         Button("Delete", variant="danger")
        ...     )
        ... )

        Large centered modal:
        >>> Modal(
        ...     "Modal content here",
        ...     modal_id="largeModal",
        ...     title="Large Modal",
        ...     size="lg",
        ...     centered=True
        ... )

        Scrollable modal:
        >>> Modal(
        ...     "Very long content...",
        ...     modal_id="scrollModal",
        ...     title="Scrollable",
        ...     scrollable=True
        ... )

        Full-screen on mobile:
        >>> Modal(
        ...     "Content",
        ...     modal_id="fullModal",
        ...     title="Full Screen",
        ...     fullscreen="md-down"
        ... )

    Note:
        To trigger a modal, use Bootstrap's data attributes:
        >>> Button("Open Modal", data_bs_toggle="modal", data_bs_target="#deleteModal")
        
        Or use HTMX to load modal content dynamically:
        >>> Button("Load Modal", hx_get="/modal-content", hx_target="#modalContainer")

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/modal/
    """
    # Build modal dialog classes
    dialog_classes = ["modal-dialog"]

    if size:
        dialog_classes.append(f"modal-{size}")

    if centered:
        dialog_classes.append("modal-dialog-centered")

    if scrollable:
        dialog_classes.append("modal-dialog-scrollable")

    if fullscreen:
        if fullscreen is True:
            dialog_classes.append("modal-fullscreen")
        else:
            dialog_classes.append(f"modal-fullscreen-{fullscreen}")

    # Build modal attributes (WITHOUT id - we'll add it later)
    modal_classes = ["modal", "fade"]
    user_cls = kwargs.pop("cls", "")
    all_modal_classes = merge_classes(" ".join(modal_classes), user_cls)

    attrs: dict[str, Any] = {
        "cls": all_modal_classes,
        "tabindex": "-1",
        "aria_labelledby": f"{modal_id}Label",
        "aria_hidden": "true",
    }

    # Static backdrop
    if static_backdrop:
        attrs["data_bs_backdrop"] = "static"
        attrs["data_bs_keyboard"] = "false"

    # Convert remaining kwargs (excluding modal_id)
    converted_kwargs = _convert_attrs({k: v for k, v in kwargs.items() if k != 'modal_id'})
    attrs.update(converted_kwargs)

    # Build modal structure
    content_parts = []

    # Header
    if title:
        header = Div(
            H5(title, cls="modal-title", id=f"{modal_id}Label"),
            Button(
                type="button",
                cls="btn-close",
                data_bs_dismiss="modal",
                aria_label="Close",
            ),
            cls="modal-header",
        )
        content_parts.append(header)

    # Body
    body = Div(*children, cls="modal-body")
    content_parts.append(body)

    # Footer
    if footer:
        footer_div = Div(footer, cls="modal-footer")
        content_parts.append(footer_div)

    # Assemble modal
    modal_content = Div(*content_parts, cls="modal-content")
    modal_dialog = Div(modal_content, cls=" ".join(dialog_classes))

        # Assemble modal
    modal_content = Div(*content_parts, cls="modal-content")
    modal_dialog = Div(modal_content, cls=" ".join(dialog_classes))

    # # FINAL CORRECT WAY — id goes in attrs, not after
    # final_attrs = {"id": modal_id, **attrs}
    # # return Div(modal_dialog, **final_attrs)
    return Div(modal_dialog, id=modal_id, **attrs)