# Static Files Guide

Complete guide to handling static files in Faststrap applications.

## Overview

Faststrap uses two separate directories for static files:
- `/static/` - Faststrap's Bootstrap CSS, JS, and icons (managed automatically)
- `/assets/` (or custom) - Your application's images, fonts, uploads (you manage)

## Quick Start

```python
from fasthtml.common import FastHTML
from faststrap import add_bootstrap, mount_assets

app = FastHTML()
add_bootstrap(app)           # Mounts Faststrap files at /static/
mount_assets(app, "assets")  # Mounts your files at /assets/

@app.route("/")
def home():
    return Div(
        Img(src="/assets/logo.png"),
        style="background-image: url('/assets/hero.jpg');"
    )
```

## Methods Comparison

### Method 1: `mount_assets()` (Recommended)

**Pros**: Explicit, flexible, no conflicts  
**Cons**: Requires one extra line

```python
from faststrap import mount_assets

mount_assets(app, "assets", url_path="/assets")

# Files: assets/hero.jpg → /assets/hero.jpg
```

### Method 2: FastHTML's `static_dir`

**Pros**: Built-in, simple  
**Cons**: Files at root, potential conflicts

```python
app = FastHTML(static_dir="assets")

# Files: assets/hero.jpg → /hero.jpg (NOT /assets/hero.jpg!)
```

### Method 3: Manual Mount (Advanced)

**Pros**: Full control  
**Cons**: More verbose

```python
from starlette.staticfiles import StaticFiles
from starlette.routing import Mount
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
app.routes.insert(0, Mount("/assets", StaticFiles(directory=path), name="assets"))
```

## Best Practices

1. **Use `mount_assets()`** for clarity and flexibility
2. **Separate directories**: Keep your assets separate from Faststrap's
3. **Consistent naming**: Use `/assets/` for all custom files
4. **Absolute paths in HTML**: Always use `/assets/file.jpg`, not `assets/file.jpg`

## Common Issues

### 404 Not Found

**Cause**: Path mismatch between mount and HTML reference

**Fix**:
```python
# If you mounted at /assets/
mount_assets(app, "assets", url_path="/assets")

# Use /assets/ in HTML
Img(src="/assets/logo.png")  # ✅
Img(src="/logo.png")         # ❌
```

### Files at Wrong Path

**Cause**: Using `static_dir` but referencing `/assets/`

**Fix**: Either use `mount_assets()` OR change HTML paths to match root

## Advanced Usage

### Multiple Directories

```python
mount_assets(app, "images", url_path="/img")
mount_assets(app, "uploads", url_path="/uploads")
mount_assets(app, "fonts", url_path="/fonts")
```

### Absolute Paths

```python
mount_assets(app, "/var/www/static", url_path="/files")
```

### Custom Priority

```python
# Add to end of routes instead of beginning
mount_assets(app, "assets", priority=False)
```
