# fnv32

FNV-1a 32-bit hash. The result is an integer in `0 .. 2**32-1`. The empty string hashes to the FNV offset basis.

```python
from fnv32 import fnv1a, fnv1a_hex, same_hash, bucket, same_bucket

fnv1a("a")
fnv1a_hex("a")  # 8 hex digits
same_hash("a", "a")  # True
```

```bash
python -m unittest test_fnv32.py
```

MIT
