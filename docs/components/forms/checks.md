# Checkbox, Radio & Switch

These components allow users to select one or more options from a list. FastStrap provides `Checkbox` for multiple select, `Radio` for single select, and `Switch` for toggles.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Checks & Radios](https://getbootstrap.com/docs/5.3/forms/checks-radios/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render flex-column align-items-start">
    <div class="form-check">
      <input class="form-check-input" type="checkbox" id="check1">
      <label class="form-check-label" for="check1">Subscribe to newsletter</label>
    </div>
    <div class="form-check">
      <input class="form-check-input" type="radio" name="plan" id="radio1" value="monthly">
      <label class="form-check-label" for="radio1">Monthly Plan</label>
    </div>
    <div class="form-check form-switch">
      <input class="form-check-input" type="checkbox" id="switch1">
      <label class="form-check-label" for="switch1">Enable Notifications</label>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Checkbox("subscribe", label="Subscribe to newsletter")
Radio("plan", value="monthly", label="Monthly Plan")
Switch("notifications", label="Enable Notifications")
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Grouping Radios
Radios share a `name` attribute to ensure only one can be selected at a time.

!!! note "Code & Output"
<div class="component-preview">
  <div class="preview-header">Live Preview (Radio Group)</div>
  <div class="preview-render flex-column align-items-start">
    <div class="form-check">
      <input class="form-check-input" type="radio" name="shipping" id="ship1" value="standard" checked>
      <label class="form-check-label" for="ship1">Standard Shipping (Free)</label>
    </div>
    <div class="form-check">
      <input class="form-check-input" type="radio" name="shipping" id="ship2" value="express">
      <label class="form-check-label" for="ship2">Express Shipping ($10)</label>
    </div>
    <div class="form-check">
      <input class="form-check-input" type="radio" name="shipping" id="ship3" value="overnight">
      <label class="form-check-label" for="ship3">Overnight ($25)</label>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Div(
    Radio("shipping", value="standard", label="Standard Shipping (Free)", checked=True),
    Radio("shipping", value="express", label="Express Shipping ($10)"),
    Radio("shipping", value="overnight", label="Overnight ($25)")
)
```
  </div>
</div>

### 2. Inline Layout
By default, checks stack vertically. Use `inline=True` to place them side-by-side.

!!! note "Code & Output"
<div class="component-preview">
  <div class="preview-header">Live Preview (Inline)</div>
  <div class="preview-render">
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="checkbox" id="inline1" value="python">
      <label class="form-check-label" for="inline1">Python</label>
    </div>
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="checkbox" id="inline2" value="javascript">
      <label class="form-check-label" for="inline2">JavaScript</label>
    </div>
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="checkbox" id="inline3" value="rust">
      <label class="form-check-label" for="inline3">Rust</label>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Div(
    Checkbox("tag", value="python", label="Python", inline=True),
    Checkbox("tag", value="javascript", label="JavaScript", inline=True),
    Checkbox("tag", value="rust", label="Rust", inline=True)
)
```
  </div>
</div>

### 3. Switches 
A `Switch` is simply a checkbox with a toggle slider appearance. It has the same API as `Checkbox`.

!!! note "Code & Output"
<div class="component-preview">
  <div class="preview-header">Live Preview (Switches)</div>
  <div class="preview-render flex-column align-items-start">
    <div class="form-check form-switch">
      <input class="form-check-input" type="checkbox" id="sw1" checked>
      <label class="form-check-label" for="sw1">Wi-Fi</label>
    </div>
    <div class="form-check form-switch">
      <input class="form-check-input" type="checkbox" id="sw2">
      <label class="form-check-label" for="sw2">Bluetooth</label>
    </div>
    <div class="form-check form-switch">
      <input class="form-check-input" type="checkbox" id="sw3" disabled>
      <label class="form-check-label" for="sw3">Airplane Mode</label>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Switch("wifi", label="Wi-Fi", checked=True)
Switch("bluetooth", label="Bluetooth")
Switch("airplane", label="Airplane Mode", disabled=True)
```
  </div>
</div>

### 4. Button Style (Toggle Buttons) 
You can make checkboxes and radios look like push buttons using `btn_style=True`.

!!! note "Code & Output"
<div class="component-preview">
  <div class="preview-header">Live Preview (Toggle Buttons)</div>
  <div class="preview-render">
    <div class="btn-group" role="group">
      <input type="radio" class="btn-check" name="view" id="v1" value="list" checked>
      <label class="btn btn-outline-primary" for="v1">List View</label>
      <input type="radio" class="btn-check" name="view" id="v2" value="grid">
      <label class="btn btn-outline-primary" for="v2">Grid View</label>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Div(
    Radio("view", value="list", label="List View", btn_style=True, variant="outline-primary", checked=True),
    Radio("view", value="grid", label="Grid View", btn_style=True, variant="outline-primary"),
    cls="btn-group"
)
```
  </div>
</div>

---

## Parameter Reference (Common)

| FastStrap Param | Type | Bootstrap Class | Description |
| :--- | :--- | :--- | :--- |
| `name` | `str` | `name="..."` | Name for form submission. Radios with same name act as a group. |
| `value` | `str` | `value="..."` | Value submitted when checked. |
| `label` | `str` | `<label>` | Text displayed next to the control. |
| `checked` | `bool` | `checked` | Detailed initial state. |
| `inline` | `bool` | `.form-check-inline` | Displays control inline. |
| `reverse` | `bool` | `.form-check-reverse` | Puts label on left, input on right. |
| `switch` | `bool` | `.form-switch` | (Checkbox only) Renders as toggle switch. |
| `btn_style` | `bool` | `.btn-check` | Renders as a button instead of a native input. |

::: faststrap.components.forms.checks.Checkbox
    options:
        show_source: false
        heading_level: 4

::: faststrap.components.forms.checks.Radio
    options:
        show_source: false
        heading_level: 4
