"""FNV-1a 32-bit hash of a text string."""
from __future__ import annotations

_OFFSET = 2166136261
_PRIME = 16777619
_MASK = 0xFFFFFFFF


def fnv1a(text: str) -> int:
    value = _OFFSET
    for byte in text.encode("utf-8"):
        value ^= byte
        value = (value * _PRIME) & _MASK
    return value
