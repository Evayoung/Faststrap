"""FastStrap - Modern Bootstrap 5 components for FastHTML.

Build beautiful web UIs in pure Python with zero JavaScript knowledge.
"""

__version__ = "0.3.1"
__author__ = "FastStrap Contributors"
__license__ = "MIT"

# Core functionality
# Display
from .components.display import (
    Badge,
    Card,
    EmptyState,
    Figure,
    StatCard,
    Table,
    TBody,
    TCell,
    THead,
    TRow,
)

# Feedback
from .components.feedback import (
    Alert,
    ConfirmDialog,
    Modal,
    Popover,
    Progress,
    ProgressBar,
    SimpleToast,
    Spinner,
    Toast,
    ToastContainer,
    Tooltip,
)

# Forms
from .components.forms import (
    Button,
    ButtonGroup,
    ButtonToolbar,
    Checkbox,
    CloseButton,
    FileInput,
    FloatingLabel,
    Input,
    InputGroup,
    InputGroupText,
    Radio,
    Range,
    Select,
    Switch,
)

# Layout
from .components.layout import Col, Container, Hero, Row

# Navigation
from .components.navigation import (
    Accordion,
    AccordionItem,
    Breadcrumb,
    Collapse,
    Drawer,
    Dropdown,
    DropdownDivider,
    DropdownItem,
    ListGroup,
    ListGroupItem,
    Navbar,
    Pagination,
    TabPane,
    Tabs,
)
from .core.effects import Fx
from .core.assets import add_bootstrap, get_assets
from .core.base import merge_classes
from .core._stability import experimental, stable, beta
from .core.theme import (
    Theme,
    create_theme,
    get_builtin_theme,
    list_builtin_themes,
    reset_component_defaults,
    resolve_defaults,
    set_component_defaults,
)

# Utils
from .utils import cleanup_static_resources, get_faststrap_static_url
from .utils.icons import Icon

__all__ = [
    # Core
    "add_bootstrap",
    "get_assets",
    "merge_classes",
    # Theme
    "Theme",
    "create_theme",
    "get_builtin_theme",
    "list_builtin_themes",
    "set_component_defaults",
    "reset_component_defaults",
    "resolve_defaults",
    # Forms
    "Button",
    "CloseButton",
    "ButtonGroup",
    "ButtonToolbar",
    "Checkbox",
    "FileInput",
    "Radio",
    "Switch",
    "Range",
    "Input",
    "InputGroup",
    "InputGroupText",
    "FloatingLabel",
    "Select",
    # Display
    "Badge",
    "Card",
    "EmptyState",
    "Figure",
    "StatCard",
    "Table",
    "THead",
    "TBody",
    "TRow",
    "TCell",
    "Alert",
    "ConfirmDialog",
    "Toast",
    "SimpleToast",
    "ToastContainer",
    "Modal",
    "Popover",
    "Tooltip",
    "Progress",
    "ProgressBar",
    "Spinner",
    # Layout
    "Container",
    "Row",
    "Col",
    "Hero",
    # Navigation
    "Accordion",
    "AccordionItem",
    "Collapse",
    "Drawer",
    "ListGroup",
    "ListGroupItem",
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
    "Fx",
    # Stability
    "stable",
    "beta",
    "experimental",
]
