# FastStrap

**Modern Bootstrap 5 components for FastHTML - Build beautiful web UIs in pure Python with zero JavaScript knowledge.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastHTML](https://img.shields.io/badge/FastHTML-0.6+-green.svg)](https://fastht.ml/)
[![PyPI version](https://img.shields.io/pypi/v/faststrap.svg)](https://pypi.org/project/faststrap/)
[![Tests](https://github.com/Evayoung/Faststrap/workflows/Tests/badge.svg)](https://github.com/Evayoung/Faststrap/actions)

---

## Why FastStrap?

FastHTML is amazing for building web apps in pure Python, but it lacks pre-built UI components. FastStrap fills that gap by providing:

✅ **20 Bootstrap components** - Buttons, Cards, Modals, Forms, Navigation, and more  
✅ **Zero JavaScript knowledge required** - Components just work  
✅ **No build steps** - Pure Python, no npm/webpack/vite  
✅ **Full HTMX integration** - Dynamic updates without page reloads  
✅ **Dark mode built-in** - Automatic theme switching  
✅ **Type-safe** - Full type hints for better IDE support  
✅ **Pythonic API** - Intuitive kwargs style

---

## Quick Start

### Installation

```bash
pip install faststrap
```

### Hello World

```python
from fasthtml.common import FastHTML, serve
from faststrap import add_bootstrap, Card, Button

app = FastHTML()
add_bootstrap(app, theme="dark")

@app.route("/")
def home():
    return Card(
        "Welcome to FastStrap! Build beautiful UIs in pure Python.",
        header="Hello World 👋",
        footer=Button("Get Started", variant="primary")
    )

serve()
```

That's it! You now have a modern, responsive web app with zero JavaScript.

---

## Available Components (20 Total)

### ✅ Phase 1+2 (v0.1.0 - v0.2.2) - 12 Components

| Component | Description | Status |
|-----------|-------------|--------|
| **Button** | Buttons with variants, sizes, loading states | ✅ |
| **ButtonGroup** | Grouped buttons and toolbars | ✅ |
| **Badge** | Status indicators and labels | ✅ |
| **Card** | Content containers with headers/footers | ✅ |
| **Alert** | Dismissible alerts with variants | ✅ |
| **Modal** | Dialog boxes and confirmations | ✅ |
| **Drawer** | Offcanvas side panels | ✅ |
| **Toast** | Auto-dismiss notifications | ✅ |
| **Navbar** | Responsive navigation bars | ✅ |
| **Container/Row/Col** | Bootstrap grid system | ✅ |
| **Icon** | Bootstrap Icons helper | ✅ |

### ✅ Phase 3 (v0.3.0 - Released!) - 8 New Components

| Component | Description | Status |
|-----------|-------------|--------|
| **Tabs** | Navigation tabs and pills | ✅ NEW |
| **Dropdown** | Contextual menus with split buttons | ✅ NEW |
| **Input** | Text form controls with validation | ✅ NEW |
| **Select** | Dropdown selections (single/multiple) | ✅ NEW |
| **Breadcrumb** | Navigation trail with icons | ✅ NEW |
| **Pagination** | Page navigation with customization | ✅ NEW |
| **Spinner** | Loading indicators (border/grow) | ✅ NEW |
| **Progress** | Progress bars with animations | ✅ NEW |

### 🚧 Phase 4 (v0.4.0 - Planned Q2 2026)

- **Table** - Responsive data tables
- **Accordion** - Collapsible panels
- **Carousel** - Image sliders
- **ListGroup** - Versatile lists
- **Tooltip** - Contextual hints
- **Popover** - Rich overlays
- **Checkbox/Radio/Range** - Form controls
- **FileInput** - File uploads

See [ROADMAP.md](ROADMAP.md) for complete timeline.

---

## Core Concepts

### 1. Adding Bootstrap to Your App

```python
from fasthtml.common import FastHTML
from faststrap import add_bootstrap

app = FastHTML()

# Basic setup (includes default FastStrap favicon)
add_bootstrap(app)

# With dark theme
add_bootstrap(app, theme="dark")

# Custom favicon
add_bootstrap(app, theme="dark", favicon_url="/static/logo.svg")

# Using CDN
add_bootstrap(app, use_cdn=True)
```

### 2. Using Components

All components follow Bootstrap's conventions with Pythonic names:

```python
from faststrap import Button, Badge, Alert, Input, Select, Tabs

# Button with HTMX
Button("Save", variant="primary", hx_post="/save", hx_target="#result")

# Form inputs
Input("email", input_type="email", label="Email Address", required=True)
Select("country", ("us", "USA"), ("uk", "UK"), label="Country")

# Navigation tabs
Tabs(
    ("home", "Home", True),
    ("profile", "Profile"),
    ("settings", "Settings")
)
```

### 3. HTMX Integration

All components support HTMX attributes:

```python
# Dynamic button
Button("Load More", hx_get="/api/items", hx_swap="beforeend")

# Live search input
Input("search", placeholder="Search...", hx_get="/search", hx_trigger="keyup changed delay:500ms")

# Dynamic dropdown
Select("category", ("a", "A"), ("b", "B"), hx_get="/filter", hx_trigger="change")
```

### 4. Responsive Grid System

```python
from faststrap import Container, Row, Col

Container(
    Row(
        Col("Left column", cols=12, md=6, lg=4),
        Col("Middle column", cols=12, md=6, lg=4),
        Col("Right column", cols=12, md=12, lg=4)
    )
)
```

---

## Examples

### Form with Validation

```python
from faststrap import Input, Select, Button, Card

Card(
    Input(
        "email",
        input_type="email",
        label="Email Address",
        placeholder="you@example.com",
        required=True,
        help_text="We'll never share your email"
    ),
    Input(
        "password",
        input_type="password",
        label="Password",
        required=True,
        size="lg"
    ),
    Select(
        "country",
        ("us", "United States"),
        ("uk", "United Kingdom"),
        ("ca", "Canada"),
        label="Country",
        required=True
    ),
    Button("Sign Up", variant="primary", type="submit", cls="w-100"),
    header="Create Account"
)
```

### Navigation with Tabs

```python
from faststrap import Tabs, TabPane, Card

Card(
    Tabs(
        ("profile", "Profile", True),
        ("settings", "Settings"),
        ("billing", "Billing")
    ),
    Div(
        TabPane("Profile content here", tab_id="profile", active=True),
        TabPane("Settings content here", tab_id="settings"),
        TabPane("Billing content here", tab_id="billing"),
        cls="tab-content p-3"
    )
)
```

### Loading States

```python
from faststrap import Spinner, Progress, Button

# Spinner in button
Button(
    Spinner(size="sm", label="Loading..."),
    " Processing...",
    variant="primary",
    disabled=True
)

# Progress bar
Progress(75, variant="success", striped=True, animated=True, label="75%")

# Stacked progress
Div(
    ProgressBar(30, variant="success"),
    ProgressBar(20, variant="warning"),
    ProgressBar(10, variant="danger"),
    cls="progress"
)
```

### Pagination

```python
from faststrap import Pagination, Breadcrumb

# Breadcrumb
Breadcrumb(
    (Icon("house"), "/"),
    ("Products", "/products"),
    ("Laptops", None)
)

# Page navigation
Pagination(
    current_page=5,
    total_pages=20,
    size="lg",
    align="center",
    show_first_last=True
)
```

---

## Project Structure

```
faststrap/
├── src/faststrap/
│   ├── __init__.py              # Public API
│   ├── core/
│   │   ├── assets.py            # Bootstrap injection + favicon
│   │   ├── base.py              # Component base classes
│   │   └── registry.py          # Component registry
│   ├── components/
│   │   ├── forms/               # Button, Input, Select
│   │   ├── display/             # Card, Badge
│   │   ├── feedback/            # Alert, Toast, Modal, Spinner, Progress
│   │   ├── navigation/          # Navbar, Drawer, Tabs, Dropdown, Breadcrumb, Pagination
│   │   └── layout/              # Container, Row, Col
│   ├── static/                  # Bootstrap assets + favicon
│   │   ├── css/
│   │   │   ├── bootstrap.min.css
│   │   │   └── bootstrap-icons.min.css
│   │   ├── js/
│   │   │   └── bootstrap.bundle.min.js
│   │   └── favicon.svg          # Default FastStrap favicon
│   ├── templates/               # Component templates
│   └── utils/
│       ├── icons.py             # Bootstrap Icons
│       ├── static_management.py # Assets extended helper functions
│       └── attrs.py             # Centralized attribute conversion
├── tests/                       # 219 tests (80% coverage)
├── examples/                    # Demo applications
└── docs/                        # Documentation
```

---

## Development

### Prerequisites

- Python 3.10+
- FastHTML 0.6+
- Git

### Setup

```bash
# Clone repository
git clone https://github.com/Evayoung/Faststrap.git
cd Faststrap

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=faststrap

# Type checking
mypy src/faststrap

# Format code
black src/faststrap tests
ruff check src/faststrap tests
```

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribution Guide

1. **Pick a component** from [ROADMAP.md](ROADMAP.md) Phase 4
2. **Follow patterns** in [BUILDING_COMPONENTS.md](BUILDING_COMPONENTS.md)
3. **Write tests** - Aim for 100% coverage (8-15 tests per component)
4. **Submit PR** - We review within 48 hours

---

## Documentation

- 📖 **Component Spec**: [COMPONENT_SPEC.md](COMPONENT_SPEC.md)
- 🏗️ **Building Guide**: [BUILDING_COMPONENTS.md](BUILDING_COMPONENTS.md)
- 🗺️ **Roadmap**: [ROADMAP.md](ROADMAP.md)
- 🤝 **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)
- 📝 **Changelog**: [CHANGELOG.md](CHANGELOG.md)

---

## Roadmap

### v0.3.0 (Current - Released Dec 2024)
- ✅ 20 components (12 + 8 new)
- ✅ 219 tests, 80% coverage
- ✅ Centralized convert_attrs() utility
- ✅ Default FastStrap favicon
- ✅ Full HTMX integration

### v0.4.0 (Q2 2025)
- Table, Accordion, Carousel, ListGroup
- Tooltip, Popover
- Checkbox, Radio, Range, FileInput
- 28+ components total

### v1.0.0 (Q4 2025)
- 50+ components
- Component playground
- Video tutorials
- Production ready

See [ROADMAP.md](ROADMAP.md) for complete timeline.

---

## Support

- 📖 **Documentation**: [GitHub README](https://github.com/Evayoung/Faststrap#readme)
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/Evayoung/Faststrap/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Evayoung/Faststrap/discussions)
- 🎮 **Discord**: [FastHTML Community](https://discord.gg/qcXvcxMhdP)

---

## Stats

- **20 components** across 5 categories
- **219 passing tests** (80% coverage)
- **Bootstrap 5.3.3** compliant
- **Python 3.10+** with modern type hints
- **Zero custom JavaScript** required
- **Full HTMX integration**

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **FastHTML** - The amazing pure-Python web framework
- **Bootstrap** - Battle-tested UI components
- **HTMX** - Dynamic interactions without complexity
- **Contributors** - Thank you! 🙏

---

**Built with ❤️ for the FastHTML community**