"""
FastStrap - Modern Bootstrap 5 components for FastHTML.

Build beautiful web UIs in pure Python with zero JavaScript knowledge.
"""

__author__ = "FastStrap Contributors"
__license__ = "MIT"

# Core functionality
from .core.assets import add_bootstrap, get_assets
from .core.base import Component, BaseComponent, merge_classes

# Components
from .components.forms import Button

__all__ = [
    # Core
    "add_bootstrap",
    "get_assets",
    "Component",
    "BaseComponent",
    "merge_classes",
    # Components
    "Button",
    # Metadata
    "__version__",
]