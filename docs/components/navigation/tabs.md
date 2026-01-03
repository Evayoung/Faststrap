# Tabs & Pills

Use tabs and pills to navigate between different views or panes of content within the same page.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Navs & Tabs](https://getbootstrap.com/docs/5.3/components/navs-tabs/)

---

## Quick Start

Tabs require a list of `NavItem` objects and a list of `TabPane` objects. FastStrap simplifies this with the `Tabs` component.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render flex-column">
    <ul class="nav nav-tabs w-100 mb-3" role="tablist">
      <li class="nav-item" role="presentation">
        <button class="nav-link active" id="tab1-tab" data-bs-toggle="tab" data-bs-target="#tab1" type="button" role="tab">Profile</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="tab2-tab" data-bs-toggle="tab" data-bs-target="#tab2" type="button" role="tab">Settings</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="tab3-tab" data-bs-toggle="tab" data-bs-target="#tab3" type="button" role="tab">Security</button>
      </li>
    </ul>
    <div class="tab-content w-100">
      <div class="tab-pane fade show active" id="tab1" role="tabpanel">This is Content A</div>
      <div class="tab-pane fade" id="tab2" role="tabpanel">This is Content B</div>
      <div class="tab-pane fade" id="tab3" role="tabpanel">This is Content C</div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Tabs(
    TabPane("This is Content A", label="Profile"),
    TabPane("This is Content B", label="Settings"),
    TabPane("This is Content C", label="Security")
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Pills Variant
Pills look like rounded buttons and are often used for filtering or sub-navigation.

!!! note "Code & Output"
<div class="component-preview">
  <div class="preview-header">Live Preview (Pills)</div>
  <div class="preview-render">
    <ul class="nav nav-pills w-100" role="tablist">
      <li class="nav-item"><button class="nav-link active">Profile</button></li>
      <li class="nav-item"><button class="nav-link">Settings</button></li>
      <li class="nav-item"><button class="nav-link">Security</button></li>
    </ul>
  </div>
  <div class="preview-code" markdown>
```python
Tabs(
    TabPane("...", label="Profile"),
    TabPane("...", label="Settings"),
    TabPane("...", label="Security"),
    pills=True
)
```
  </div>
</div>

### 2. Vertical Alignment
For sidebar-style navigation, you can stack the nav items vertically.

!!! note "Code & Output"
    ```python
    Tabs(..., vertical=True)
    ```

### 3. HTMX Content Loading
Load tab content only when it's clicked to save initial page load time.

```python
Tabs(
    TabPane(
        Div(hx_get="/api/user-stats", hx_trigger="load"), # Loads on click
        label="Analytics"
    )
)
```

---

## Components Map

| Component | Responsibility |
| :--- | :--- |
| `Tabs` | The main container that handles switching logic. |
| `TabPane` | A single container of content. Use the `label` argument to define the tab text. |

---

## Parameter Reference

| FastStrap Param | Type | Bootstrap Class | Description |
| :--- | :--- | :--- | :--- |
| `pills` | `bool` | `.nav-pills` | Switches from underlined tabs to rounded pills. |
| `vertical` | `bool` | `.flex-column` | Aligns items vertically. |
| `fade` | `bool` | `.fade` | Adds transition animation when switching. |
| `fill` | `bool` | `.nav-fill` | Proportionally fills the entire width. |
| `justified` | `bool` | `.nav-justified` | Every item has the exact same width. |

::: faststrap.components.navigation.tabs.Tabs
    options:
        show_source: false
        heading_level: 4
