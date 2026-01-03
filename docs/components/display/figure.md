# Figure

The `Figure` component is used for displaying content—like images—with an optional caption. It provides consistent padding and styling for image-based content blocks.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Figures Documentation](https://getbootstrap.com/docs/5.3/content/figures/)

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <figure class="figure">
      <img src="https://placehold.co/600x400" class="figure-img img-fluid rounded" alt="...">
      <figcaption class="figure-caption text-center">A placeholder figure caption.</figcaption>
    </figure>
  </div>
  <div class="preview-code" markdown>
```python
Figure(
    src="https://placehold.co/600x400",
    caption="A placeholder figure caption.",
    align="center"
)
```
  </div>
</div>

---

## Visual Examples & Use Cases

### 1. Alignment
Captions can be aligned to the start (left), center, or end (right).

!!! note "Code & Output"
<div class="component-preview">
  <div class="preview-header">Live Preview (Alignment)</div>
  <div class="preview-render">
    <figure class="figure">
      <img src="https://placehold.co/300x200" class="figure-img img-fluid" alt="...">
      <figcaption class="figure-caption text-end">Right aligned caption</figcaption>
    </figure>
  </div>
  <div class="preview-code" markdown>
```python
Figure(
    src="...", 
    caption="Right aligned caption", 
    align="end"
)
```
  </div>
</div>

### 2. Styling (Thumbnail & Rounded)
Wrap the image in a thumbnail border or round the corners.

!!! note "Code & Output"
    ```python
    Figure(
        src="...", 
        thumbnail=True, 
        rounded=True
    )
    ```

---

## Parameter Reference

| FastStrap Param | Type | Bootstrap Class | Description |
| :--- | :--- | :--- | :--- |
| `src` | `str` | `src="..."` | Image URL. |
| `alt` | `str` | `alt="..."` | Alt text for accessibility. |
| `caption` | `str` | `.figure-caption` | Text to display below image. |
| `align` | `str` | `.text-{align}` | Caption alignment: `start`, `center`, `end`. |
| `fluid` | `bool` | `.img-fluid` | Makes image responsive (full width). |
| `rounded` | `bool` | `.rounded` | Rounds image corners. |
| `thumbnail` | `bool` | `.img-thumbnail` | Adds a 1px border with padding. |

::: faststrap.components.display.figure.Figure
    options:
        show_source: true
        heading_level: 4
