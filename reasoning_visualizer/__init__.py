"""Public API for the Streamlit Reasoning Visualizer component."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

import streamlit.components.v1 as components

__version__ = "0.1.0"
__author__ = "Ketan Mahandule"
__license__ = "Apache-2.0"

_RELEASE = True
_COMPONENT_PATH = Path(__file__).parent / "frontend"

if _RELEASE:
    _component_func = components.declare_component(
        "reasoning_visualizer",
        path=str(_COMPONENT_PATH),
    )
else:
    _component_func = components.declare_component(
        "reasoning_visualizer",
        url="http://localhost:3001",
    )


def visualizer(text: str, key: Optional[str] = None) -> Any:
    """Render the reasoning visualizer Streamlit component.

    Parameters
    ----------
    text:
        Raw model output containing reasoning tags and a final answer.
    key:
        Optional Streamlit key for rendering multiple component instances.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return _component_func(text=text, key=key, default=None)


__all__ = ["visualizer", "__version__", "__author__", "__license__"]
