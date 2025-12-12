"""FastStrap utilities."""

from .icons import Icon
from .static_management import (
    cleanup_static_resources,
    get_faststrap_static_url,
)

__all__ = [
    "Icon",
    "cleanup_static_resources",
    "get_faststrap_static_url",
]
