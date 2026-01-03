# Table

The `Table` component enables you to display tabular data efficiently. FastStrap's implementation decomposes the table into semantic sub-components (`THead`, `TBody`, `TRow`, `TCell`) for maximum flexibility, while providing high-level arguments for common styles like striping and hover effects.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Tables](https://getbootstrap.com/docs/5.3/content/tables/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <table class="table table-striped table-hover w-100">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Role</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>Alice</td>
          <td>Admin</td>
        </tr>
        <tr>
          <td>2</td>
          <td>Bob</td>
          <td>User</td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class="preview-code" markdown>
```python
Table(
    THead(TRow(TCell("ID"), TCell("Name"), TCell("Role"))),
    TBody(
        TRow(TCell("1"), TCell("Alice"), TCell("Admin")),
        TRow(TCell("2"), TCell("Bob"), TCell("User")),
    ),
    striped=True, hover=True
)
```
  </div>
</div>

---

## Styling Options

FastStrap exposes Bootstrap's powerful table modifiers as simple boolean arguments.

### 1. Variants & Themes
Use `variant` to color the entire table, or set `striped` / `hover` for readability.

<div class="component-preview">
  <div class="preview-header">Live Preview (Variants)</div>
  <div class="preview-render flex-column gap-3">
    <!-- Dark Table -->
    <table class="table table-dark table-striped w-100 mb-0">
      <thead><tr><th>Header</th></tr></thead>
      <tbody><tr><td>Dark Striped Content</td></tr></tbody>
    </table>
    <!-- Borderless -->
    <table class="table table-borderless w-100 mb-0">
      <thead><tr><th>Header</th></tr></thead>
      <tbody><tr><td>Borderless Content</td></tr></tbody>
    </table>
  </div>
  <div class="preview-code" markdown>
```python
# Dark Mode Table
Table(..., variant="dark", striped=True)

# Borderless
Table(..., borderless=True)
```
  </div>
</div>

### 2. Responsiveness
Tables can overflow on small screens. Wrap them in a responsive container automatically using the `responsive` argument.

```python
# Enables horizontal scrolling on small devices
Table(..., responsive=True) # or responsive="sm", "md", "lg"
```

---

## API Reference

::: faststrap.components.display.table.Table
    options:
        show_source: true
        heading_level: 4
