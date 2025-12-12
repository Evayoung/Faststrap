"""
FastStrap - Production Bootstrap Asset Manager
Safe for multi-worker servers, thread-safe, with graceful fallbacks.
"""

import warnings
from os import environ
from typing import Any

from fasthtml.common import Link, Script, Style
from starlette.staticfiles import StaticFiles

from ..utils.static_management import (
    create_favicon_links,
    get_default_favicon_url,
    get_static_path,
    is_mounted,
    resolve_static_url,
)

# Bootstrap versions
BOOTSTRAP_VERSION = "5.3.3"
BOOTSTRAP_ICONS_VERSION = "1.11.3"


# CDN assets with SRI hashes
CDN_ASSETS = (
    Link(
        rel="stylesheet",
        href=f"https://cdn.jsdelivr.net/npm/bootstrap@{BOOTSTRAP_VERSION}/dist/css/bootstrap.min.css",
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH",
        crossorigin="anonymous",
    ),
    Link(
        rel="stylesheet",
        href=f"https://cdn.jsdelivr.net/npm/bootstrap-icons@{BOOTSTRAP_ICONS_VERSION}/font/bootstrap-icons.min.css",
    ),
    Script(
        src=f"https://cdn.jsdelivr.net/npm/bootstrap@{BOOTSTRAP_VERSION}/dist/js/bootstrap.bundle.min.js",
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz",
        crossorigin="anonymous",
        defer=True,
    ),
)


def local_assets(static_url: str) -> tuple[Any, ...]:
    """Generate local asset links for the given static URL."""
    base = static_url.rstrip("/")
    return (
        Link(rel="stylesheet", href=f"{base}/css/bootstrap.min.css"),
        Link(rel="stylesheet", href=f"{base}/css/bootstrap-icons.min.css"),
        Script(src=f"{base}/js/bootstrap.bundle.min.js"),
    )


# Custom FastStrap enhancements
CUSTOM_STYLES = Style(
    """
:root {
  --fs-shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --fs-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1);
  --fs-shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
  --fs-transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.shadow-sm { box-shadow: var(--fs-shadow-sm) !important; }
.shadow { box-shadow: var(--fs-shadow) !important; }
.shadow-lg { box-shadow: var(--fs-shadow-lg) !important; }

.btn { transition: var(--fs-transition); }
.btn:hover:not(:disabled) { transform: translateY(-1px); box-shadow: var(--fs-shadow); }
.btn:active:not(:disabled) { transform: translateY(0); }

[data-bs-theme="dark"] { transition: background-color 0.3s, color 0.3s; }
"""
)


def get_assets(
    use_cdn: bool | None = None, include_custom: bool = True, static_url: str | None = None
) -> tuple[Any, ...]:
    """
    Get Bootstrap assets for injection.

    Args:
        use_cdn: Use CDN (True) or local files (False)
        include_custom: Include FastStrap custom styles
        static_url: Custom static URL (if using local assets)

    Returns:
        Tuple of FastHTML elements for app.hdrs
    """
    if use_cdn is None:
        use_cdn = environ.get("FASTSTRAP_USE_CDN", "false").lower() == "true"

    if use_cdn:
        assets = CDN_ASSETS
    else:
        actual_static_url = static_url if static_url is not None else "/static"
        assets = local_assets(actual_static_url)

    if include_custom:
        return assets + (CUSTOM_STYLES,)
    return assets


def add_bootstrap(
    app: Any,
    theme: str | None = None,
    use_cdn: bool | None = None,
    mount_static: bool = True,
    static_url: str = "/static",
    force_static_url: bool = False,
    include_favicon: bool = True,
    favicon_url: str | None = None,
) -> Any:
    """
    Enhance FastHTML app with Bootstrap (production-safe).

    Args:
        app: FastHTML application instance
        theme: Bootstrap theme ('light', 'dark', or None for auto)
        use_cdn: Use CDN instead of local assets
        mount_static: Auto-mount static directory
        static_url: Preferred URL prefix for static files
        force_static_url: Force use of this URL even if already mounted (not recommended)
        include_favicon: Include default FastStrap favicon (ignored if favicon_url is provided)
        favicon_url: Custom favicon URL (overrides default)
                    Examples:
                    - "/static/my-icon.svg"
                    - "https://example.com/icon.png"

    Returns:
        Modified app instance

    Example:
        # Use default FastStrap favicon
        add_bootstrap(app, theme="dark")

        # Use custom favicon
        add_bootstrap(app, theme="dark", favicon_url="/static/my-logo.svg")

        # Disable favicon injection
        add_bootstrap(app, theme="dark", include_favicon=False)
    """
    # Clean up any previous FastStrap state on this app
    if hasattr(app, "_faststrap_static_url"):
        delattr(app, "_faststrap_static_url")

    if use_cdn is None:
        use_cdn = environ.get("FASTSTRAP_USE_CDN", "false").lower() == "true"

    # 1. Determine where to mount static files
    actual_static_url = static_url
    if not use_cdn and mount_static:
        if force_static_url:
            # User wants to force this URL (they handle conflicts)
            actual_static_url = static_url
        else:
            # Auto-resolve conflicts
            actual_static_url = resolve_static_url(app, static_url)

    # 2. Collect favicon links FIRST (before Bootstrap assets)
    favicon_links = []
    if favicon_url:
        # User provided custom favicon
        favicon_links = create_favicon_links(favicon_url)
    elif include_favicon:
        # Use default FastStrap favicon
        default_favicon = get_default_favicon_url(use_cdn, actual_static_url)
        favicon_links = create_favicon_links(default_favicon)

    # 3. Get Bootstrap assets
    bootstrap_assets = get_assets(
        use_cdn=use_cdn, include_custom=True, static_url=actual_static_url if not use_cdn else None
    )

    # 4. Normalize app.hdrs to list and inject in correct order
    # Favicon FIRST, then Bootstrap assets
    hdrs = getattr(app, "hdrs", None)
    if hdrs is None:
        # No existing headers - inject favicon + bootstrap
        app.hdrs = list(favicon_links) + list(bootstrap_assets)
    else:
        if isinstance(hdrs, tuple):
            app.hdrs = list(hdrs)
        # Prepend: favicon first, then bootstrap, then existing headers
        app.hdrs[0:0] = list(favicon_links) + list(bootstrap_assets)

    # 5. Apply theme
    if theme in {"light", "dark"}:
        existing_htmlkw = getattr(app, "htmlkw", {}) or {}
        existing_htmlkw.update({"data-bs-theme": theme})
        app.htmlkw = existing_htmlkw

    # 6. Mount static files with thread-safe extraction
    if not use_cdn and mount_static:
        try:
            if not is_mounted(app, actual_static_url):
                static_path = get_static_path()
                app.mount(
                    actual_static_url,
                    StaticFiles(directory=str(static_path)),
                    name="faststrap_static",
                )
                # ✅ CRITICAL FIX: Store on app instance, not globally
                app._faststrap_static_url = actual_static_url
        except Exception as e:
            # Fall back to CDN + helpful warning
            caution = f"""
            FastStrap: Could not mount local static files ({e}).
            Falling back to CDN mode. You can explicitly set use_cdn=True.
            """
            warnings.warn(caution, RuntimeWarning, stacklevel=2)

            # Remove local asset references
            app.hdrs = [
                item
                for item in getattr(app, "hdrs", [])
                if not (
                    (hasattr(item, "href") and "static" in (item.href or ""))
                    or (hasattr(item, "src") and "static" in (item.src or ""))
                )
            ]

            # Inject CDN assets (with favicon)
            cdn_assets = get_assets(use_cdn=True, include_custom=True)
            cdn_favicon = []
            if favicon_url:
                cdn_favicon = create_favicon_links(favicon_url)
            elif include_favicon:
                cdn_favicon = create_favicon_links(
                    "https://cdn.jsdelivr.net/gh/Evayoung/Faststrap@main/src/faststrap/static/favicon.svg"
                )

            app.hdrs[0:0] = list(cdn_favicon) + list(cdn_assets)

    return app
