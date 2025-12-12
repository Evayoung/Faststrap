"""FastStrap - Modern Bootstrap 5 components for FastHTML.

Build beautiful web UIs in pure Python with zero JavaScript knowledge.
"""

__version__ = "0.2.4"  # Update version!
__author__ = "FastStrap Contributors"
__license__ = "MIT"

# Core functionality
# Display
from .components.display import Badge, Card

# Feedback
from .components.feedback import Alert, Modal, Progress, ProgressBar, Spinner, Toast, ToastContainer
from .components.forms import Button, ButtonGroup, ButtonToolbar, Input, Select

# Layout
from .components.layout import Col, Container, Row

# Navigation
from .components.navigation import (
    Breadcrumb,
    Drawer,
    Dropdown,
    DropdownDivider,
    DropdownItem,
    Navbar,
    Pagination,
    TabPane,
    Tabs,
)
from .core.assets import add_bootstrap, get_assets
from .core.base import merge_classes
from .utils import cleanup_static_resources, get_faststrap_static_url

# Utils
from .utils.icons import Icon

__all__ = [
    # Core
    "add_bootstrap",
    "get_assets",
    "merge_classes",
    # Forms
    "Button",
    "ButtonGroup",
    "ButtonToolbar",
    "Input",
    "Select",
    # Display
    "Badge",
    "Card",
    # Feedback
    "Alert",
    "Toast",
    "ToastContainer",
    "Modal",
    "Progress",
    "ProgressBar",
    "Spinner",
    # Layout
    "Container",
    "Row",
    "Col",
    # Navigation
    "Drawer",
    "Navbar",
    "Pagination",
    "Breadcrumb",
    "Dropdown",
    "DropdownItem",
    "DropdownDivider",
    "Tabs",
    "TabPane",
    # Utils
    "Icon",
    "get_faststrap_static_url",
    "cleanup_static_resources",
    # Metadata
    "__version__",
    "__author__",
    "__license__",
]
