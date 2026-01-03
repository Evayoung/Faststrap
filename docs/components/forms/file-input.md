# File Input

The `FileInput` component is an enhanced wrapper for `<input type="file">`. It supports single/multiple uploads, size options, and includes a built-in **automatic preview** feature (Phase 4B).

!!! tip "Bootstrap Reference"
    [Bootstrap 5 File Input](https://getbootstrap.com/docs/5.3/forms/form-control/#file-input)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="w-100">
      <label class="form-label">Upload Resume</label>
      <input class="form-control" type="file" id="f1">
    </div>
  </div>
  <div class="preview-code" markdown>
```python
FileInput("resume", label="Upload Resume")
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Multiple Files & Sizing
Allow uploading multiple files at once.

!!! note "Code & Output"
<div class="component-preview">
  <div class="preview-header">Live Preview (Multiple & Large)</div>
  <div class="preview-render">
    <div class="w-100">
      <label class="form-label">Gallery Photos</label>
      <input class="form-control form-control-lg" type="file" multiple id="f2">
    </div>
  </div>
  <div class="preview-code" markdown>
```python
FileInput("photos", label="Gallery Photos", multiple=True, size="lg")
```
  </div>
</div>

### 2. Automatic Image Preview (✨ New in Phase 4B)
FastStrap includes a lightweight JavaScript snippet that can automatically show a preview of selected images *before* upload.

Set `preview_id="auto"` to have FastStrap handle everything for you.

!!! note "Code & Output"
<div class="component-preview">
  <div class="preview-header">Live Preview (Automatic Preview)</div>
  <div class="preview-render flex-column align-items-center">
    <div class="w-100 mb-3">
      <label class="form-label">Profile Picture</label>
      <input class="form-control" type="file" accept="image/*" id="f3">
    </div>
    <div id="file-avatar-preview" class="border rounded d-flex align-items-center justify-content-center bg-light" style="width: 150px; height: 150px;">
      <span class="text-muted small">Preview</span>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Automatically generates a preview container with ID 'file-avatar-preview'
FileInput(
    "avatar", 
    label="Profile Picture", 
    accept="image/*", 
    preview_id="auto" 
)
```
  </div>
</div>

---

## Parameter Reference

| Param | Type | HTML Attribute | Description |
| :--- | :--- | :--- | :--- |
| `name` | `str` | `name="..."` | Form field name. |
| `label` | `str` | `<label>` | Input label. |
| `multiple` | `bool` | `multiple` | Allow selecting multiple files. |
| `accept` | `str` | `accept="..."` | File type filter (e.g. `image/*`, `.pdf`). |
| `preview_id` | `str` | - | ID of element to display preview in. Use `"auto"` for automatic generation. |

::: faststrap.components.forms.file.FileInput
    options:
        show_source: true
        heading_level: 4
