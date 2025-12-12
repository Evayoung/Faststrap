# FastStrap Roadmap – Updated December 2025

**Vision:** The most complete, Pythonic, zero-JS Bootstrap 5 component library for FastHTML — 100+ production-ready components built by the community, for the community.

---

## Current Status (v0.3.0 – Released Dec 12, 2025)

**20 components live** – Phase 1 through 3 complete  
**219 tests** – 80%+ coverage  
**Full HTMX + Bootstrap 5.3.3 support**  
**Zero custom JavaScript required**

### Completed Phases

| Phase | Components | Status       | Released     |
|------|------------|--------------|--------------|
| 1–2  | 12         | Complete     | Dec 2025     |
| 3    | +8 (Tabs, Dropdown, Input, Select, Breadcrumb, Pagination, Spinner, Progress) | Complete | **Dec 12, 2025** |

**Total: 20 production-ready components**

---

## Phase 4 – Now Open for Contributions (v0.4.0 – Target Q2 2026)

**Goal:** Reach **28–30 components** by end of 1st quarter-2026  
**Focus:** Most requested missing Bootstrap primitives

### High-Priority Components (Help Wanted!)

| Priority | Component        | Status       | Issue / Owner         | Notes |
|---------|------------------|--------------|-----------------------|-------|
| 1       | `Table`          | Open         | —                     | Responsive, striped, hover, dark variant |
| 2       | `Accordion`      | Open         | —                     | Flush, always-open, icons |
| 3       | `Checkbox` / `Radio` | Open     | —                     | Inline, switches, button groups |
| 4       | `Range` (slider) | Open         | —                     | With labels, steps |
| 5       | `FileInput`      | Open         | —                     | Multiple, drag & drop preview |
| 6       | `Tooltip`        | Open         | —                     | Requires Bootstrap JS init |
| 7       | `Popover`        | Open         | —                     | Rich content |
| 8       | `Carousel`       | Open         | —                     | Indicators + controls |
| 9       | `ListGroup`      | Open         | —                     | Actionable, badges |

Claim any of these → open an issue with “I’ll take X” → get assigned → PR reviewed in <48h.

---

## Future Phases (Community-Driven)

| Phase | Target     | Goal Components | Focus Area                   |
|------|------------|------------------|------------------------------|
| 5    | Q3–Q4 2025 | ~50 total        | SaaS & Dashboard Patterns    |
| 6    | 2026       | 80–100 total     | Advanced UI + Integrations   |
| 7    | 2026+      | 100+             | Full Bootstrap parity + extras |

### Planned Higher-Level Components (Phase 5+)
- `DataTable` (sortable, searchable, paginated)
- `Form` + `Field` helpers (auto-validation, layout)
- `Sidebar`, `DashboardLayout`, `StatCard`
- `ModalForm`, `ConfirmDialog`
- `ToastContainer` manager
- `DarkModeToggle` component
- `MultiSelect`, `TagInput`, `DatePicker` wrappers

All driven by community demand.

---

## Success Metrics (Updated Dec 2025)

| Metric                    | v0.3.0 (Now)    | v0.4.0 Goal     | v1.0.0 Goal     |
|---------------------------|-----------------|-----------------|-----------------|
| Components                | 20              | 30+             | 100+            |
| Tests                     | 219             | 300+            | 700+            |
| Coverage                  | 80%             | 90%+            | 95%+            |
| GitHub Stars              | Growing fast    | 2,000+          | 10,000+         |
| Monthly PyPI Downloads    | Rising          | 10k+            | 50k+            |
| Contributors              | 15+             | 50+             | 100+            |

---

## How to Contribute Right Now

1. **Pick a Phase 4 component** from the table above
2. Comment on GitHub Issues → “I’ll build Accordion” → get assigned
3. Use `src/faststrap/templates/component_template.py` as starting point
4. Follow [BUILDING_COMPONENTS.md](BUILDING_COMPONENTS.md) exactly
5. Write 10–15 tests using `to_xml()`
6. Submit PR → merged in ≤48 hours

Fastest way to get your name in the next release!

---

## Release Schedule (Revised & Realistic)

| Version | Target       | Components | Notes                              |
|--------|--------------|------------|------------------------------------|
| 0.3.0  | Dec 12, 2025 | 20         | Complete – Phase 3 shipped!         |
| 0.4.0  | Jan–Mar 2026 | 28–32      | Phase 4 (Table, Accordion, etc.)   |
| 0.5.0  | Apr–Jun 2026 | 45–50      | SaaS/dashboard patterns            |
| 1.0.0  | Aug 2026     | 100+       | Stable, full docs, playground      |

Timelines flex based on community velocity — the more PRs, the faster we ship.

---

## Community Feedback Wanted

Tell us what you need most:
- Reply in [Discussions](https://github.com/Evayoung/Faststrap/discussions)
- Vote on issues with thumbs up
- Join FastHTML Discord → #faststrap channel

Your vote directly influences what gets built next.

---

**Last Updated: December 12, 2025**  
**Current Version: 0.3.0 (20 components live)**

**Let’s build the definitive UI library for FastHTML — together.**

Claim a component today → become a core contributor tomorrow!