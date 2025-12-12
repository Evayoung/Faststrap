"""Bootstrap Input component for text form controls."""

from typing import Any, Literal

from fasthtml.common import Div, Label, Small
from fasthtml.common import Input as FTInput

from ...core.base import merge_classes
from ...utils.attrs import convert_attrs

InputType = Literal["text", "email", "password", "number", "tel", "url", "search", "date", "time"]
SizeType = Literal["sm", "lg"]


def Input(
    name: str,
    input_type: InputType = "text",
    placeholder: str | None = None,
    value: str | None = None,
    label: str | None = None,
    help_text: str | None = None,
    size: SizeType | None = None,
    disabled: bool = False,
    readonly: bool = False,
    required: bool = False,
    **kwargs: Any,
) -> Div:  # Div | FTInput
    """Bootstrap Input component for text form controls.

    Args:
        name: Input name attribute
        input_type: HTML input type
        placeholder: Placeholder text
        value: Initial value
        label: Label text (if provided, wraps input in div)
        help_text: Helper text below input
        size: Input size (sm, lg)
        disabled: Whether input is disabled
        readonly: Whether input is readonly
        required: Whether input is required
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        Div with label/input/help or just Input element

    Example:
        Simple input:
        >>> Input("email", input_type="email", placeholder="Enter email")

        With label and validation:
        >>> Input(
        ...     "username",
        ...     label="Username",
        ...     help_text="Choose a unique username",
        ...     required=True,
        ...     placeholder="johndoe"
        ... )

        With HTMX validation:
        >>> Input(
        ...     "email",
        ...     input_type="email",
        ...     label="Email Address",
        ...     hx_post="/validate/email",
        ...     hx_trigger="blur",
        ...     hx_target="#email-feedback"
        ... )

        Password with size:
        >>> Input(
        ...     "password",
        ...     input_type="password",
        ...     label="Password",
        ...     size="lg",
        ...     required=True
        ... )

        Disabled readonly input:
        >>> Input(
        ...     "readonly_field",
        ...     value="Cannot edit",
        ...     readonly=True,
        ...     disabled=True
        ... )

    Note:
        - If label is provided, input is wrapped in Div with proper accessibility
        - Help text automatically links via aria-describedby
        - Required fields show asterisk (*) in label

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/forms/form-control/
    """
    # Ensure ID is present for label linkage (defaults to name)
    input_id = kwargs.pop("id", name)

    # Build input classes
    input_classes = ["form-control"]
    if size:
        input_classes.append(f"form-control-{size}")

    user_cls = kwargs.pop("cls", "")
    input_cls = merge_classes(" ".join(input_classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {
        "cls": input_cls,
        "type": input_type,
        "name": name,
        "id": input_id,
    }

    if placeholder:
        attrs["placeholder"] = placeholder

    if value:
        attrs["value"] = value

    if disabled:
        attrs["disabled"] = True

    if readonly:
        attrs["readonly"] = True

    if required:
        attrs["required"] = True

    # ARIA for help text (must be applied BEFORE convert_attrs)
    if help_text:
        attrs["aria_describedby"] = f"{name}-help"

    # Convert remaining kwargs (HTMX, data-*, etc.)
    attrs.update(convert_attrs(kwargs))

    # Create input element
    input_elem = FTInput(**attrs)

    # If just input (no label/help), return input only
    if not label and not help_text:
        return input_elem

    # Wrap in div with label and help text
    elements = []

    if label:
        label_elem = Label(
            label,
            " ",
            Small("*", cls="text-danger") if required else "",
            **{"for": input_id},
            cls="form-label",
        )
        elements.append(label_elem)

    elements.append(input_elem)

    if help_text:
        help_elem = Small(help_text, cls="form-text text-muted", id=f"{name}-help")
        elements.append(help_elem)

    return Div(*elements, cls="mb-3")
