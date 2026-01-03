# Hero Section

The `Hero` component (often called a Jumbotron) is a large, prominent section typically found at the top of landing pages to showcase the primary value proposition of a site.

!!! tip "Bootstrap Reference"
    Hero sections are usually custom implementations of Containers and Spacing. FastStrap provides a dedicated component to standardize this common pattern.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="px-4 py-5 my-5 text-center bg-light rounded w-100">
      <h1 class="display-5 fw-bold">Build Faster with FastStrap</h1>
      <div class="col-lg-6 mx-auto">
        <p class="lead mb-4">The definitive Bootstrap component library for FastHTML.</p>
        <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
          <button type="button" class="btn btn-primary btn-lg px-4 gap-3">Get Started</button>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Hero(
    title="Build Faster with FastStrap",
    subtitle="The definitive Bootstrap component library for FastHTML.",
    action=Button("Get Started", size="lg", variant="primary"),
    variant="light",
    align="center"
)
```
  </div>
</div>

<div class="result" markdown>
![Screenshot: Large centered hero section with title and button](../../assets/images/hero-basic.png)
</div>

---

## Visual Examples & Use Cases

### 1. Dark Mode Hero
Use `variant="dark"` and `bg_variant="dark"` for a premium, high-contrast look.

!!! note "Code & Output"
    ```python
<div class="component-preview">
  <div class="preview-header">Live Preview (Dark)</div>
  <div class="preview-render p-0 overflow-hidden">
    <div class="px-4 py-5 text-start bg-dark text-white w-100">
      <h1 class="display-5 fw-bold">Modern Python Development</h1>
      <p class="lead mb-0">Zero JS, Infinite Possibilities.</p>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Hero(
    title="Modern Python Development",
    subtitle="Zero JS, Infinite Possibilities.",
    variant="dark",
    bg_variant="dark",
    align="start"
)
```
  </div>
</div>
    ```

### 2. Image Backgrounds
You can pass an image URL to `bg_image` to create a more visual experience.

```python
Hero(
    title="Adventure Awaits",
    bg_image="https://example.com/mountain.jpg",
    fixed_bg=True, # Parallax effect
    variant="dark"
)
```

---

## Practical Functionality

### 1. Customizing Children
The `action` argument can accept any FastHTML element or component.

```python
Hero(
    ...,
    action=Div(
        Button("Download", variant="primary"),
        Button("View Source", variant="link"),
        cls="d-flex gap-2 justify-content-center"
    )
)
```

---

## Parameter Reference

| FastStrap Param | Type | Description |
| :--- | :--- | :--- |
| `title` | `str` | Main large heading (H1). |
| `subtitle` | `str` | Secondary text or description. |
| `action` | `Any` | Call to action (usually a button). |
| `align` | `str` | Alignment: `start`, `center`, `end`. |
| `variant` | `str` | Text theme: `light` or `dark`. |
| `bg_variant` | `str` | Background color utility (e.g. `primary`, `dark`). |
| `bg_image` | `str` | URL for background image. |
| `container` | `bool` | If `True`, wraps content in a `.container`. Default `True`. |
| `fixed_bg` | `bool` | Enables parallax background attachment. |

::: faststrap.components.layout.hero.Hero
    options:
        show_source: true
        heading_level: 4
