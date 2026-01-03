# Empty State

The `EmptyState` component provides a visual placeholder for when data is missing or a user hasn't completed an action yet. It usually contains an icon, a title, a description, and a call-to-action button.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="text-center p-5 bg-body-tertiary rounded w-100">
      <i class="bi bi-search display-1 text-muted mb-3 d-block"></i>
      <h3 class="fw-bold">No items found</h3>
      <p class="text-muted mb-4">You haven't added any items to your collection yet.</p>
      <button class="btn btn-primary">Add First Item</button>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
EmptyState(
    title="No items found",
    description="You haven't added any items to your collection yet.",
    icon="search",
    action=Button("Add First Item", variant="primary")
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Dashboard Placeholders
Use inside cards or grids to signify empty data sets.

!!! note "Code & Output"
    ```python
    from faststrap import Card

<div class="component-preview">
  <div class="preview-header">Live Preview (Card Placeholder)</div>
  <div class="preview-render">
    <div class="card shadow-sm w-100">
      <div class="card-body">
        <div class="text-center p-4">
          <i class="bi bi-activity h1 text-muted mb-2 d-block"></i>
          <h5 class="fw-semibold">No Activity</h5>
          <p class="text-muted small mb-0">Log some activity to see it here.</p>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Card(
    EmptyState(
        title="No Activity",
        description="Log some activity to see it here.",
        icon="activity"
    )
)
```
  </div>
</div>
    ```

---

## Parameter Reference

| FastStrap Param | Type | Description |
| :--- | :--- | :--- |
| `title` | `str` | Main bold heading. |
| `description` | `str` | Explanatory message. |
| `icon` | `str` | Bootstrap icon name. |
| `action` | `Any` | Call to action (usually a Button or Link). |
| `variant` | `str` | Color variant for the icon and title. |

::: faststrap.components.display.empty_state.EmptyState
    options:
        show_source: true
        heading_level: 4
