"""Base classes and protocols for FastStrap components."""

from abc import ABC, abstractmethod
from typing import Any, Protocol


class Component(Protocol):
    """Protocol for FastStrap components."""

    def render(self) -> Any:
        """Render component to FastHTML object."""
        ...


class BaseComponent(ABC):
    """Base class for components with shared functionality."""

    def __init__(self, *children: Any, **kwargs: Any):
        self.children = list(children)
        self.attrs = kwargs.copy()
        self._classes: list[str] = []

    @abstractmethod
    def render(self) -> Any:
        """Render component. Must be implemented by subclasses."""
        pass

    def add_class(self, *classes: str) -> "BaseComponent":
        """Add CSS classes fluently."""
        self._classes.extend(classes)
        return self

    def merge_attrs(self, **defaults: Any) -> dict[str, Any]:
        """Merge component attributes with defaults."""
        merged = {**defaults, **self.attrs}

        # Merge classes
        all_classes: list[str] = []
        if "cls" in defaults:
            all_classes.append(defaults["cls"])
        if "cls" in self.attrs:
            all_classes.append(self.attrs["cls"])
        if self._classes:
            all_classes.extend(self._classes)

        if all_classes:
            merged["cls"] = " ".join(all_classes)

        return merged


def merge_classes(*class_lists: Any) -> str:
    """Merge multiple class strings or lists, removing duplicates."""
    classes: list[str] = []
    seen = set()

    def _process(item: Any) -> None:
        if not item:
            return
        if isinstance(item, (list, tuple)):
            for sub in item:
                _process(sub)
        elif isinstance(item, str):
            for cls in item.split():
                cls = cls.strip()
                if cls and cls not in seen:
                    classes.append(cls)
                    seen.add(cls)

    for item in class_lists:
        _process(item)

    return " ".join(classes)
