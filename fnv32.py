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


def same_hash(left: str, right: str) -> bool:
    return fnv1a(left) == fnv1a(right)


def fnv1a_hex(text: str) -> str:
    return f"{fnv1a(text):08x}"


def bucket(text: str, count: int) -> int:
    if count < 1:
        raise ValueError("桶数至少为 1")
    return fnv1a(text) % count


def same_bucket(left: str, right: str, count: int) -> bool:
    return bucket(left, count) == bucket(right, count)
