# Badge

Small, circular or pill-shaped indicators for status, counts, or labels. Badges scale to match the size of the immediate parent element by using relative font sizing and `em` units.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Badges](https://getbootstrap.com/docs/5.3/components/badge/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <span class="badge text-bg-primary">New</span>
  </div>
  <div class="preview-code" markdown>
```python
Badge("New", variant="primary")
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Variants
Like buttons, badges use semantic variants for meaning.

!!! note "Code & Output"
<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="d-flex gap-2">
      <span class="badge text-bg-success">Success</span>
      <span class="badge text-bg-danger">Danger</span>
      <span class="badge rounded-pill text-bg-warning">Warning</span>
      <span class="badge text-bg-light text-dark">Light</span>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Badge("Success", variant="success")
Badge("Danger", variant="danger")
Badge("Warning", variant="warning", pill=True)
Badge("Light", variant="light", cls="text-dark")
```
  </div>
</div>

### 2. Contextual Badges
Badges are often placed inside other components like Buttons or Headings.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render flex-column gap-3">
    <!-- Notification count in a button -->
    <button class="btn btn-primary d-flex align-items-center">
      Notifications <span class="badge rounded-pill text-bg-light text-dark ms-2">99+</span>
    </button>
    <!-- Status in a heading -->
    <h1 class="mb-0">Documentation <span class="badge text-bg-info">Beta</span></h1>
  </div>
  <div class="preview-code" markdown>
```python
# Notification count in a button
Button(
    "Notifications ", 
    Badge("99+", variant="light", pill=True), 
    variant="primary"
)

# Status in a heading
H1("Documentation ", Badge("Beta", variant="info"))
```
  </div>
</div>

---

## Practical Functionality

### 1. Indicators (Dot Style)
You can create "status dots" by using a Badge with no text and specific width/height.

```python
# A small 'Online' green dot
Badge(variant="success", rounded=True, style={"width": "10px", "height": "10px", "padding": "0"})
```

---

## Advanced Customization

### 1. CSS Variables
Customize standard badge colors.

| CSS Variable | Description | Default |
| :--- | :--- | :--- |
| `--bs-badge-padding-x` | Horizontal padding. | `.65em` |
| `--bs-badge-padding-y` | Vertical padding. | `.35em` |
| `--bs-badge-font-size` | Text size. | `.75em` |
| `--bs-badge-font-weight` | Boldness. | `700` |
| `--bs-badge-border-radius` | Corner roundness. | `var(--bs-border-radius)` |

---

## Parameter Reference

| FastStrap Param | Type | Bootstrap Class | Description |
| :--- | :--- | :--- | :--- |
| `variant` | `str` | `.text-bg-{variant}` | Color theme. |
| `pill` | `bool` | `.rounded-pill` | Fully rounded edges. |
| `rounded` | `bool` | `.rounded-circle` | Perfect circle (if width=height). |

::: faststrap.components.display.badge.Badge
    options:
        show_source: true
        heading_level: 4
