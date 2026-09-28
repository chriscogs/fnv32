import unittest

from fnv32 import fnv1a


class Fnv32Test(unittest.TestCase):
    def test_stable(self) -> None:
        self.assertEqual(fnv1a(""), 2166136261)
        self.assertEqual(fnv1a("a"), fnv1a("a"))
        self.assertNotEqual(fnv1a("a"), fnv1a("b"))


if __name__ == "__main__":
    unittest.main()
