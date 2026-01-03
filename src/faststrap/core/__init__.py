"""Core functionality for FastStrap."""

from .assets import add_bootstrap, get_assets
from .base import BaseComponent, Component, merge_classes
from .registry import get_registry, register
from ._stability import beta, experimental, stable

__all__ = [
    "add_bootstrap",
    "get_assets",
    "Component",
    "BaseComponent",
    "merge_classes",
    "get_registry",
    "register",
    "beta",
    "experimental",
    "stable",
]
