import unittest

from fnv32 import fnv1a, fnv1a_hex, same_hash


class Fnv32Test(unittest.TestCase):
    def test_stable(self) -> None:
        self.assertEqual(fnv1a(""), 2166136261)
        self.assertEqual(fnv1a("a"), fnv1a("a"))
        self.assertNotEqual(fnv1a("a"), fnv1a("b"))
        self.assertEqual(fnv1a_hex("a"), f"{fnv1a('a'):08x}")
        self.assertEqual(len(fnv1a_hex("a")), 8)
        self.assertTrue(same_hash("a", "a"))
        self.assertFalse(same_hash("a", "b"))


if __name__ == "__main__":
    unittest.main()
