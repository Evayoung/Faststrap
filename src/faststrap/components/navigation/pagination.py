"""Bootstrap Pagination component for page navigation."""

from typing import Any, Literal

from fasthtml.common import A, Li, Nav, Span, Ul

from ...core.base import merge_classes
from ...utils.attrs import convert_attrs

SizeType = Literal["sm", "lg"]
AlignType = Literal["start", "center", "end"]


def Pagination(
    current_page: int,
    total_pages: int,
    size: SizeType | None = None,
    align: AlignType = "start",
    max_pages: int = 5,
    base_url: str = "#",
    show_first_last: bool = False,
    show_prev_next: bool = True,
    **kwargs: Any,
) -> Nav:
    """Bootstrap Pagination component for page navigation.

    Args:
        current_page: Current active page (1-indexed)
        total_pages: Total number of pages
        size: Pagination size (sm, lg)
        align: Alignment (start, center, end)
        max_pages: Maximum page numbers to show
        base_url: Base URL for page links (uses ?page=N)
        show_first_last: Show first/last page buttons
        show_prev_next: Show previous/next buttons
        **kwargs: Additional HTML attributes (cls, id, hx-*, etc.)

    Returns:
        Nav element with pagination

    Example:
        Simple pagination:
        >>> Pagination(current_page=3, total_pages=10)

        Large centered:
        >>> Pagination(
        ...     current_page=5,
        ...     total_pages=20,
        ...     size="lg",
        ...     align="center"
        ... )

        With HTMX:
        >>> Pagination(
        ...     current_page=3,
        ...     total_pages=10,
        ...     base_url="/products",
        ...     hx_boost="true",
        ...     hx_target="#product-list"
        ... )

        Custom URL pattern:
        >>> Pagination(
        ...     current_page=2,
        ...     total_pages=5,
        ...     base_url="/blog/posts",
        ...     show_first_last=True
        ... )

        Small with limited pages:
        >>> Pagination(
        ...     current_page=7,
        ...     total_pages=20,
        ...     size="sm",
        ...     max_pages=3
        ... )

    Note:
        - Pages are 1-indexed (first page is 1, not 0)
        - Page links use ?page=N query parameter
        - Active page shown as Span (not clickable)

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/pagination/
    """
    # Build pagination classes
    classes = ["pagination"]
    if size:
        classes.append(f"pagination-{size}")

    # Alignment
    justify_class = {
        "center": "justify-content-center",
        "end": "justify-content-end",
    }.get(align)

    user_cls = kwargs.pop("cls", "")
    ul_cls = merge_classes(" ".join(classes), user_cls)

    # Calculate page range
    half = max_pages // 2
    start = max(1, current_page - half)
    end = min(total_pages, start + max_pages - 1)

    # Adjust if at end
    if end == total_pages:
        start = max(1, end - max_pages + 1)

    # Build page links
    links: list[Any] = []

    # First page
    if show_first_last and current_page > 1:
        links.append(Li(A("«", href=f"{base_url}?page=1", aria_label="First"), cls="page-item"))

    # Previous page
    if show_prev_next:
        prev_disabled = current_page == 1
        prev_page = max(1, current_page - 1)
        links.append(
            Li(
                (
                    A("‹", href=f"{base_url}?page={prev_page}", aria_label="Previous")
                    if not prev_disabled
                    else Span("‹", aria_hidden="true")
                ),
                cls="page-item" + (" disabled" if prev_disabled else ""),
            )
        )

    # Page numbers
    for page in range(start, end + 1):
        active = page == current_page
        href = f"{base_url}?page={page}"
        links.append(
            Li(
                Span(str(page)) if active else A(str(page), href=href, cls="page-link"),
                cls="page-item" + (" active" if active else ""),
                aria_current="page" if active else None,
            )
        )

    # Next page
    if show_prev_next:
        next_disabled = current_page == total_pages
        next_page = min(total_pages, current_page + 1)
        links.append(
            Li(
                (
                    A("›", href=f"{base_url}?page={next_page}", aria_label="Next")
                    if not next_disabled
                    else Span("›", aria_hidden="true")
                ),
                cls="page-item" + (" disabled" if next_disabled else ""),
            )
        )

    # Last page
    if show_first_last and current_page < total_pages:
        links.append(
            Li(A("»", href=f"{base_url}?page={total_pages}", aria_label="Last"), cls="page-item")
        )

    # Build pagination
    ul = Ul(*links, cls=ul_cls)

    # Convert remaining kwargs (HTMX, data-*, etc.)
    nav_attrs: dict[str, Any] = {"aria_label": "Page navigation"}
    nav_attrs.update(convert_attrs(kwargs))

    return Nav(ul, cls=justify_class, **nav_attrs)
