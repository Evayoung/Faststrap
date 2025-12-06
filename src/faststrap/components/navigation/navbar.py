"""Bootstrap Navbar component for site navigation."""

from typing import Any, Literal

from fasthtml.common import A, Button, Div, Nav, Span

from ...core.base import merge_classes

VariantType = Literal["light", "dark"]
ExpandType = Literal["sm", "md", "lg", "xl", "xxl"]


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


def Navbar(
    *children: Any,
    brand: Any | None = None,
    brand_href: str = "/",
    variant: VariantType | None = None,
    bg: str | None = None,
    expand: ExpandType | None = "lg",
    sticky: Literal["top", "bottom"] | None = None,
    fixed: Literal["top", "bottom"] | None = None,
    container: bool | Literal["sm", "md", "lg", "xl", "xxl"] = True,
    **kwargs: Any,
) -> Nav:
    """Bootstrap Navbar component for responsive site navigation.

    Args:
        *children: Navbar content (nav items, forms, text, etc.)
        brand: Brand text or logo (appears on left)
        brand_href: Brand link URL (default: "/")
        variant: Color scheme (light or dark text)
        bg: Background color class (e.g., "primary", "dark", "light")
        expand: Breakpoint where navbar expands (default: "lg")
        sticky: Stick to top or bottom on scroll
        fixed: Fix to top or bottom
        container: Wrap in container (True, False, or breakpoint like "lg")
        **kwargs: Additional HTML attributes (cls, hx-*, data-*, etc.)

    Returns:
        FastHTML Nav element with navbar structure

    Example:
        Basic navbar:
        >>> Navbar(
        ...     A("Home", href="/", cls="nav-link"),
        ...     A("About", href="/about", cls="nav-link"),
        ...     brand="MyApp"
        ... )

        Dark navbar with background:
        >>> Navbar(
        ...     A("Products", href="/products", cls="nav-link"),
        ...     A("Contact", href="/contact", cls="nav-link"),
        ...     brand="Store",
        ...     variant="dark",
        ...     bg="primary"
        ... )

        Sticky navbar:
        >>> Navbar(
        ...     NavItems(...),
        ...     brand="Site",
        ...     sticky="top"
        ... )

        Custom expand breakpoint:
        >>> Navbar(
        ...     Menu items,
        ...     brand="Mobile App",
        ...     expand="md"  # Expands on tablets+
        ... )

    Note:
        For complex navbars with dropdowns, forms, or buttons,
        wrap items in appropriate containers:
        
        >>> Navbar(
        ...     Div(  # Nav items
        ...         A("Link 1", href="/", cls="nav-link"),
        ...         A("Link 2", href="/about", cls="nav-link"),
        ...         cls="navbar-nav"
        ...     ),
        ...     Div(  # Right-aligned form
        ...         Input(type="search", cls="form-control", placeholder="Search"),
        ...         cls="d-flex"
        ...     ),
        ...     brand="App"
        ... )

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/navbar/
    """
    # Build navbar classes
    classes = ["navbar"]

    # Add expand class
    if expand:
        classes.append(f"navbar-expand-{expand}")

    # Add variant
    if variant:
        classes.append(f"navbar-{variant}")

    # Add background
    if bg:
        classes.append(f"bg-{bg}")

    # Add sticky/fixed positioning
    if sticky:
        classes.append(f"sticky-{sticky}")
    elif fixed:
        classes.append(f"fixed-{fixed}")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(_convert_attrs(kwargs))

    # Build navbar content
    parts = []

    # Wrap in container if requested
    if container:
        container_cls = "container" if container is True else f"container-{container}"
        
        # Build container content
        container_parts = []

        # Brand
        if brand:
            brand_elem = A(brand, cls="navbar-brand", href=brand_href)
            container_parts.append(brand_elem)

        # Toggler for mobile (collapse button)
        if expand:
            toggler_id = kwargs.get("id", "navbarContent")
            if "id" not in kwargs:
                # Generate a unique ID for the collapse target
                import random
                toggler_id = f"navbar{random.randint(1000, 9999)}"
            
            toggler = Button(
                Span(cls="navbar-toggler-icon"),
                cls="navbar-toggler",
                type="button",
                data_bs_toggle="collapse",
                data_bs_target=f"#{toggler_id}",
                aria_controls=toggler_id,
                aria_expanded="false",
                aria_label="Toggle navigation",
            )
            container_parts.append(toggler)

            # Collapsible content
            collapse = Div(*children, cls="collapse navbar-collapse", id=toggler_id)
            container_parts.append(collapse)
        else:
            # No collapse, just add children directly
            container_parts.extend(children)

        parts.append(Div(*container_parts, cls=container_cls))
    else:
        # No container wrapper
        if brand:
            parts.append(A(brand, cls="navbar-brand", href=brand_href))
        
        if expand:
            # Still need collapse for mobile
            toggler_id = kwargs.get("id", "navbarContent")
            if "id" not in kwargs:
                import random
                toggler_id = f"navbar{random.randint(1000, 9999)}"
            
            toggler = Button(
                Span(cls="navbar-toggler-icon"),
                cls="navbar-toggler",
                type="button",
                data_bs_toggle="collapse",
                data_bs_target=f"#{toggler_id}",
                aria_controls=toggler_id,
                aria_expanded="false",
                aria_label="Toggle navigation",
            )
            parts.append(toggler)
            
            collapse = Div(*children, cls="collapse navbar-collapse", id=toggler_id)
            parts.append(collapse)
        else:
            parts.extend(children)

    return Nav(*parts, **attrs)