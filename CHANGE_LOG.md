# Changelog

All notable changes to FastStrap will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [0.3.0] - 2025-12-12

### Major Release: 8 New Components Added!

**Phase 3 Complete** - FastStrap now includes 20 total components (12 from Phase 1+2, 8 new in Phase 3)

### Added - Navigation Components (4)
- **Tabs** - Navigation tabs and pills with content panes
  - Support for tabs/pills variants
  - Vertical tab layout option
  - HTMX mode for dynamic content loading
  - TabPane helper for content management
- **Dropdown** - Contextual menus with full customization
  - Split button support
  - Directional dropdowns (up, start, end)
  - String-based dividers ("---")
  - DropdownItem and DropdownDivider helpers
- **Breadcrumb** - Navigation trail with icon support
  - Auto-active last item
  - Custom href handling
  - Full accessibility (ARIA)
- **Pagination** - Page navigation with options
  - Customizable page range
  - First/last page buttons
  - Size variants (sm, lg)
  - Alignment options (start, center, end)

### Added - Form Components (2)
- **Input** - Text form controls with validation
  - All HTML5 input types (text, email, password, number, tel, url, search, date, time)
  - Label and help text support
  - Size variants (sm, lg)
  - Required field indicators
  - Full ARIA accessibility
- **Select** - Dropdown selections
  - Single and multiple selection modes
  - Default selection support
  - Label and help text
  - Size variants
  - Full accessibility

### Added - Feedback Components (2)
- **Spinner** - Loading indicators
  - Border and grow animation types
  - Color variants
  - Small size support
  - Screen reader labels
- **Progress** - Progress bars
  - Percentage-based progress
  - Color variants
  - Striped and animated styles
  - Custom height support
  - ProgressBar helper for stacked bars

### Added - Core Features
- **Centralized convert_attrs()** utility in `utils/attrs.py`
  - Consistent HTMX attribute handling across all components
  - Converts Python snake_case to HTML kebab-case (hx_get → hx-get)
- **Default Favicon** - FastStrap now includes a built-in favicon
  - Automatically injected with `add_bootstrap()`
  - Can be disabled with `include_favicon=False`
  - Can be customized with `favicon_url` parameter
  - Supports SVG, PNG, ICO, JPG, and WebP formats

### Improved
- All components now use consistent attribute conversion
- Better type hints throughout (Python 3.10+ syntax)
- Enhanced documentation with 5-10 examples per component
- Improved error messages and validation
- Better ARIA accessibility support

### Fixed
- Dropdown divider detection (now uses string "---" instead of Hr object)
- ARIA attribute handling in form components
- ID linkage between labels and inputs

### Technical
- 219 tests passing (80% coverage)
- Full mypy type checking compliance
- All components support HTMX attributes
- Bootstrap 5.3.3 compliant

### Documentation
- Complete examples for all 8 new components
- Updated BUILDING_COMPONENTS.md guide
- Updated ROADMAP.md to reflect Phase 3 completion

[0.3.0]: https://github.com/Evayoung/Faststrap/compare/v0.2.2...v0.3.0

## [0.2.3] - 2025-12-09

### Fixed
- **Critical**: Local Bootstrap assets (`bootstrap.min.css`, `bootstrap.bundle.min.js`, icons, etc.) are now correctly included in the PyPI wheel when `use_cdn=False`. Previously, offline/local mode resulted in missing styles and broken JavaScript (modals, drawers, toasts).  
  → All local assets now work out of the box with no extra setup.
- Fixed a `mypy` type error when mounting static files by properly handling `importlib.resources.files(...).as_posix()` and casting `Traversable` objects for `StaticFiles`.

### Added
- **Developer Templates** — New `src/faststrap/templates/` directory with:
  - `component_template.py` → Boilerplate for rapid, consistent component development
  - `test_file_template.py` → Standardized pytest template with `to_xml()` assertions and HTMX/data-attribute tests
- These templates enforce FastStrap’s coding standards and dramatically speed up contribution.

### Changed
- **Packaging Improvement**: Moved the `static/` directory into `src/faststrap/static/`  
  → Ensures assets are reliably included in built wheels/sdists (modern Python packaging best practice).
- **Component Organization**: Reorganized components into clearly defined categories:
  - `forms/` → Buttons, inputs, groups
  - `display/` → Badges, cards
  - `feedback/` → Alerts, toasts, modals
  - `navigation/` → Navbar, drawer/offcanvas
  - `layout/` → Container, Row, Col  
  → Much easier for contributors to navigate and extend.

This release significantly improves reliability in offline/air-gapped environments and sets a strong foundation for community contributions and long-term maintainability.

---

## [0.2.2] - 2025-12-09

### Added
- Interactive demo with HTMX theme toggle (no custom JavaScript)
- HTMX-powered toast trigger button
- Complete showcase of all 12 components with real interactions

### Improved
- Demo now proves components work without custom JavaScript
- Theme switching via HTMX POST request
- Toast notifications via HTMX GET request
- Better documentation of HTMX integration

### Technical
- Added `/toggle-theme` route for theme switching
- Added `/show-toast` route for toast notifications
- Minimal Bootstrap JS usage (only built-in features)

---

## [0.2.0] - 2025-12-08

### 🎉 Phase 1 + Phase 2 Complete - Production Ready!

This is the first production-ready release of FastStrap, featuring 12 fully-tested Bootstrap 5 components for FastHTML.

### Added

#### **Components (12 total)**

**Forms (2):**
- `Button` - Fully-featured button with variants, sizes, icons, loading states, and outline styles
- `ButtonGroup` - Group buttons together with vertical/horizontal orientation and toolbar support
- `ButtonToolbar` - Organize multiple button groups

**Display (2):**
- `Badge` - Status indicators and labels with pill style option
- `Card` - Flexible content container with header, footer, image support, and overlay mode

**Feedback (3):**
- `Alert` - Contextual feedback messages with dismissible option and custom headings
- `Toast` - Auto-dismissing notifications with positioning via ToastContainer
- `Modal` - Dialog boxes with multiple sizes, centering, scrollable content, and fullscreen modes

**Layout (3):**
- `Container` - Fixed-width or fluid responsive containers
- `Row` - Grid rows with responsive column counts
- `Col` - Grid columns with responsive sizing and offsets

**Navigation (2):**
- `Navbar` - Responsive navigation bar with brand, collapse, and theming
- `Drawer` (Offcanvas) - Sliding side panels with multiple placements and backdrop control

**Utils (1):**
- `Icon` - Bootstrap Icons helper for easy icon integration

#### **Core Features**
- Asset management system with CDN and local file support
- Theme system supporting light, dark, and auto modes
- Base component classes and protocols for consistent API
- HTMX attribute conversion (`hx_get` → `hx-get`)
- Class merging utility for combining Bootstrap and custom classes
- Python 3.10+ type hints throughout

#### **Infrastructure**
- Complete test suite with 121 tests
- 84% code coverage
- Type checking with MyPy
- Code formatting with Black and Ruff
- GitHub Actions CI/CD pipeline
- Automatic PyPI publishing on release

#### **Documentation**
- Comprehensive README with quick start guide
- Component specification guide (COMPONENT_SPEC.md)
- Contributor guide (BUILDING_COMPONENTS.md)
- Development roadmap (ROADMAP.md)
- Example applications demonstrating all components
- Inline documentation with usage examples

### Fixed
- FastHTML `id` parameter handling using `modal_id`/`drawer_id` workaround
- Test suite updated to use `to_xml()` instead of `str()` (FastHTML 0.12.33 bug workaround)
- HTMX attribute conversion for proper HTML rendering
- Class merging to prevent duplicate Bootstrap classes
- Theme application via `htmlkw` for proper Bootstrap theming

### Technical Details
- **Python Version:** 3.10+
- **FastHTML Version:** 0.6.0+
- **Bootstrap Version:** 5.3.3
- **Bootstrap Icons Version:** 1.11.3
- **Type Checking:** MyPy strict mode
- **Linting:** Ruff + Black
- **Testing:** pytest with coverage reporting

---

## [0.1.0] - 2025-12-05

### 🌟 Initial Development Release

First internal release establishing the foundation of FastStrap.

### Added

#### **Phase 1 Components (5):**
- `Button` - Basic button implementation with variants and sizes
- `Badge` - Simple badge component with color variants
- `Alert` - Alert component with dismissible functionality
- `Card` - Card container with header and footer
- Grid system (`Container`, `Row`, `Col`) - Responsive layout system

#### **Core Infrastructure**
- Project structure and build configuration
- Asset management for Bootstrap CSS/JS
- Base component classes and utilities
- Initial test framework setup
- GitHub repository initialization

### Development Notes
- Established component development patterns
- Created test templates and examples
- Set up CI/CD pipeline
- Documented contribution guidelines

---

## [Unreleased]

### 🚀 Coming in v0.3.0 (Phase 2 - Q1 2025)

#### **Planned Components (8):**
- `Tabs` - Navigation tabs and pills
- `Dropdown` - Contextual dropdown menus
- `Input` - Text input controls with validation
- `Select` - Dropdown selection controls
- `Breadcrumb` - Navigation breadcrumbs
- `Pagination` - Page navigation controls
- `Spinner` - Loading indicators
- `Progress` - Progress bars with labels and animations

#### **Planned Features:**
- Enhanced form validation helpers
- Additional theme customization options
- Component playground documentation site
- Video tutorials and examples
- Performance optimizations

See [ROADMAP.md](ROADMAP.md) for complete future plans.

---

## Release Statistics

### v0.2.0 Metrics
- **Components:** 12
- **Tests:** 121
- **Coverage:** 84%
- **Lines of Code:** ~1,500
- **Contributors:** 2
- **Development Time:** 2 weeks

---

## Migration Guides

### Migrating from 0.1.0 to 0.2.0

**Breaking Changes:**
- None - First public release

**New Features:**
- 7 new components added (Toast, Modal, Drawer, Navbar, ButtonGroup)
- HTMX integration now fully supported
- Theme system implemented
- All components now production-ready

**Deprecations:**
- None

---

## Version History Summary

| Version | Release Date | Components | Tests | Coverage | Status |
|---------|--------------|------------|-------|----------|--------|
| 0.2.0   | 2025-12-08   | 12         | 121   | 84%      | ✅ Stable |
| 0.1.0   | 2025-12-06   | 5          | 56    | 75%      | 🔒 Internal |

---

## Contributing

We welcome contributions! See:
- [BUILDING_COMPONENTS.md](BUILDING_COMPONENTS.md) - How to build components
- [ROADMAP.md](ROADMAP.md) - What needs to be built
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines

### Reporting Issues
Found a bug? [Open an issue](https://github.com/Evayoung/Faststrap/issues/new)

### Requesting Features
Want a new component? [Start a discussion](https://github.com/Evayoung/Faststrap/discussions/new)

---

## Acknowledgments

### v0.2.0 Contributors
- **Olorundare Micheal** (@Evayoung) - Lead Developer
- **Claude (Anthropic)** - AI Development Assistant
- FastHTML Community - Testing and feedback

### Special Thanks
- **Jeremy Howard** - Creator of FastHTML
- **Answer.AI Team** - FastHTML development
- **Bootstrap Team** - Amazing CSS framework
- All early testers and contributors

---

## License

FastStrap is released under the [MIT License](LICENSE).

Copyright (c) 2024 FastStrap Contributors

---

## Links

- **Homepage:** https://github.com/Evayoung/Faststrap
- **Documentation:** [BUILDING_COMPONENTS.md](BUILDING_COMPONENTS.md)
- **PyPI:** https://pypi.org/project/faststrap/
- **Issues:** https://github.com/Evayoung/Faststrap/issues
- **Discussions:** https://github.com/Evayoung/Faststrap/discussions

---

*For older releases and detailed commit history, see [GitHub Releases](https://github.com/Evayoung/Faststrap/releases).*

**Last Updated:** December 8, 2025