# Building FastStrap Components - Complete Guide

**For contributors, LLMs, and developers building new components.**

---

## 🎯 Quick Start (30 seconds)

1. Copy an existing component from `src/faststrap/components/` as template
2. Follow the patterns below
3. Add tests to `tests/test_components/`
4. Submit PR

**Best templates to copy:**
- Simple component: `badge.py` or `spinner.py`
- Form component: `input.py` or `select.py`
- Complex component: `card.py` or `tabs.py`
- Interactive (Bootstrap JS): `modal.py` or `dropdown.py`

---

## 📋 Component Checklist

Before submitting, ensure:

- [ ] File in correct directory (`forms/`, `display/`, `feedback/`, `navigation/`, `layout/`)
- [ ] Function uses Python 3.10+ type hints (`str | None` not `Optional[str]`)
- [ ] Uses `convert_attrs()` from `utils.attrs` for HTMX support
- [ ] Uses `merge_classes()` from `core.base` for CSS
- [ ] Comprehensive docstring with 5+ examples
- [ ] Test file with 8-15 tests
- [ ] Exported in all `__init__.py` files
- [ ] Works with `to_xml()` (not just `str()`)

---

## 🏗️ Component Structure Template

```python
"""Bootstrap [ComponentName] for [purpose]."""

from typing import Any, Literal

from fasthtml.common import Div  # Or appropriate FT type

from ...core.base import merge_classes
from ...utils.attrs import convert_attrs

# Type aliases
VariantType = Literal["primary", "secondary", "success", "danger", "warning", "info", "light", "dark"]


def ComponentName(
    *children: Any,
    variant: VariantType = "primary",
    **kwargs: Any,
) -> Div:
    """Bootstrap [ComponentName] component.

    Args:
        *children: Component content
        variant: Bootstrap color variant
        **kwargs: Additional HTML attributes (cls, id, hx-*, data-*, etc.)

    Returns:
        FastHTML Div element

    Example:
        Basic:
        >>> ComponentName("Content", variant="success")

        With HTMX:
        >>> ComponentName("Load", hx_get="/api", hx_target="#result")

        Custom styling:
        >>> ComponentName("Custom", cls="mt-3 shadow")

        With icons:
        >>> ComponentName(Icon("check"), "Complete", variant="success")

        Multiple children:
        >>> ComponentName("First", "Second", "Third")

    See Also:
        Bootstrap docs: https://getbootstrap.com/docs/5.3/components/[name]/
    """
    # Build classes
    classes = ["component-base", f"component-{variant}"]

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    return Div(*children, **attrs)
```

---

## 🔧 Critical Patterns

### 1. **Type Hints (Python 3.10+)**

```python
# ✅ CORRECT
from typing import Any, Literal

def Component(
    *children: Any,
    size: Literal["sm", "lg"] | None = None,
    **kwargs: Any
) -> Div:
    ...

# ❌ WRONG (old style)
from typing import Optional, Union

def Component(
    size: Optional[Union[str, None]] = None
) -> Div:
    ...
```

### 2. **Class Merging**

```python
from ...core.base import merge_classes

# Always merge user classes
user_cls = kwargs.pop("cls", "")
all_classes = merge_classes("btn btn-primary", user_cls)
```

### 3. **Attribute Conversion (CRITICAL)**

```python
from ...utils.attrs import convert_attrs

# Always use convert_attrs() for consistent HTMX/data/ARIA handling
attrs.update(convert_attrs(kwargs))

# This allows:
Button("Save", hx_post="/save", data_id="123", aria_label="Save button")
# To become: <button hx-post="/save" data-id="123" aria-label="Save button">
```

### 4. **Bootstrap Variants**

```python
# Standard variants
VariantType = Literal[
    "primary", "secondary", "success", "danger",
    "warning", "info", "light", "dark"
]

# Apply as:
classes.append(f"btn-{variant}")  # Buttons
classes.append(f"text-bg-{variant}")  # Badges
classes.append(f"alert-{variant}")  # Alerts
classes.append(f"bg-{variant}")  # Progress bars
```

### 5. **Component IDs (Special Handling)**

If your component requires an `id` (like Modal, Drawer, Tabs):

```python
def Modal(
    *children: Any,
    modal_id: str,  # ← Use custom param name, NOT "id"
    **kwargs: Any
) -> Div:
    # Build attributes WITHOUT id
    attrs: dict[str, Any] = {"cls": classes, "role": "dialog"}
    attrs.update(convert_attrs(kwargs))
    
    # Return with id as named parameter
    return Div(*parts, id=modal_id, **attrs)
```

**Why:** Use descriptive parameter names like `modal_id`, `drawer_id`, `tab_id` for clarity.

---

## 🧪 Test File Template

```python
"""Tests for ComponentName."""

from fasthtml.common import to_xml  # ← IMPORTANT: Use to_xml(), not str()

from faststrap.components.category import ComponentName


def test_component_basic():
    """Component renders correctly."""
    comp = ComponentName("Test")
    html = to_xml(comp)  # ← Use to_xml()
    
    assert "Test" in html
    assert "component-base" in html


def test_component_variants():
    """Component supports all variants."""
    variants = ["primary", "secondary", "success", "danger"]
    
    for variant in variants:
        comp = ComponentName("Test", variant=variant)
        html = to_xml(comp)
        assert f"component-{variant}" in html


def test_component_custom_classes():
    """Component merges custom classes."""
    comp = ComponentName("Test", cls="custom-class mt-3")
    html = to_xml(comp)
    
    assert "component-base" in html
    assert "custom-class" in html
    assert "mt-3" in html


def test_component_htmx():
    """Component supports HTMX."""
    comp = ComponentName("Load", hx_get="/api", hx_target="#result")
    html = to_xml(comp)
    
    assert 'hx-get="/api"' in html
    assert 'hx-target="#result"' in html


def test_component_data_attributes():
    """Component handles data attributes."""
    comp = ComponentName("Test", data_id="123", data_type="info")
    html = to_xml(comp)
    
    assert 'data-id="123"' in html
    assert 'data-type="info"' in html


def test_component_aria_attributes():
    """Component handles ARIA attributes."""
    comp = ComponentName("Test", aria_label="Test button")
    html = to_xml(comp)
    
    assert 'aria-label="Test button"' in html
```

**CRITICAL:** Always use `to_xml(component)`, **never** `str(component)` due to FastHTML bug.

---

## 📁 File Structure

```
src/faststrap/components/
├── display/          # Visual elements (Badge, Card, Avatar)
│   ├── __init__.py
│   └── component.py
├── feedback/         # User feedback (Alert, Toast, Modal, Spinner, Progress)
├── forms/            # Form inputs (Button, Input, Select)
├── layout/           # Layout helpers (Container, Row, Col)
└── navigation/       # Navigation (Navbar, Tabs, Drawer, Dropdown, Breadcrumb, Pagination)

tests/test_components/
└── test_component.py
```

---

## 🎨 Bootstrap Component Reference

When building a component, reference Bootstrap docs:

**Base URL:** `https://getbootstrap.com/docs/5.3/components/[name]/`

**Key classes to know:**
- Variants: `btn-primary`, `alert-success`, `text-bg-danger`
- Sizes: `btn-sm`, `btn-lg`, `form-control-lg`
- States: `disabled`, `active`, `show`, `fade`
- Utilities: `d-flex`, `gap-2`, `mt-3`, `shadow`

---

## 🚀 Component Priority List

### **✅ Phase 3 Complete (v0.3.0)**
1. ✅ Tabs & TabPane
2. ✅ Dropdown (with DropdownItem, DropdownDivider)
3. ✅ Input (all HTML5 types)
4. ✅ Select (single/multiple)
5. ✅ Breadcrumb
6. ✅ Pagination
7. ✅ Spinner
8. ✅ Progress & ProgressBar

### **🎯 Phase 4 Next (v0.4.0 - Q2 2025):**
9. Table (responsive, striped, hoverable)
10. Accordion (collapsible panels)
11. Carousel (image sliders)
12. ListGroup (versatile lists)
13. Tooltip (contextual hints)
14. Popover (rich overlays)
15. Checkbox (standard, switch, inline)
16. Radio (standard, button style)
17. Range (sliders)
18. FileInput (file uploads)

See [ROADMAP.md](ROADMAP.md) for complete timeline.

---

## 💡 Tips for LLMs

When asking an LLM to build a component:

**Good prompt:**
> "Build the Accordion component for FastStrap following BUILDING_COMPONENTS.md. Use Tabs.py as template for multi-part structure. Include collapsible panels with flush variant. Add 12 tests using to_xml(). Reference: https://getbootstrap.com/docs/5.3/components/accordion/"

**Include:**
- This guide
- An existing similar component as reference
- Bootstrap docs link
- Specific test count (8-15 tests)

**Phase 3 Reference Components:**
- For simple components: `Spinner`, `Badge`
- For form components: `Input`, `Select`
- For multi-part components: `Tabs`, `Dropdown`
- For navigation: `Breadcrumb`, `Pagination`

---

## 🤝 Getting Help

- **Questions:** [GitHub Discussions](https://github.com/Evayoung/Faststrap/discussions)
- **Bugs:** [GitHub Issues](https://github.com/Evayoung/Faststrap/issues)
- **PRs:** We review within 48 hours
- **Discord:** [FastHTML Community](https://discord.gg/qcXvcxMhdP)

---

## ✅ Submission Checklist

Before submitting PR:

```bash
# 1. Run tests
pytest tests/test_components/test_yourcomponent.py -v

# 2. Check coverage
pytest --cov=faststrap.components.category.yourcomponent

# 3. Type check
mypy src/faststrap

# 4. Format
black src/faststrap tests
ruff check src/faststrap tests

# 5. Test demo
python examples/demo_yourcomponent.py
```

All checks pass? Submit PR! 🎉

---

## 📊 Current Stats (v0.3.0)

- ✅ **20 components** (12 from Phase 1+2, 8 new in Phase 3)
- ✅ **219 tests** passing (80% coverage)
- ✅ **Centralized convert_attrs()** for consistency
- ✅ **Full HTMX integration** across all components
- ✅ **Bootstrap 5.3.3** compliant

---

**Ready to build? Pick a component from Phase 4 and start coding!**