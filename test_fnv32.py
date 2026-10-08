import unittest

from fnv32 import bucket, fnv1a, fnv1a_hex, same_bucket, same_hash


class Fnv32Test(unittest.TestCase):
    def test_stable(self) -> None:
        self.assertEqual(fnv1a(""), 2166136261)
        self.assertEqual(fnv1a("a"), fnv1a("a"))
        self.assertNotEqual(fnv1a("a"), fnv1a("b"))
        self.assertEqual(fnv1a_hex("a"), f"{fnv1a('a'):08x}")
        self.assertEqual(len(fnv1a_hex("a")), 8)
        self.assertTrue(same_hash("a", "a"))
        self.assertFalse(same_hash("a", "b"))
        self.assertEqual(bucket("a", 1), 0)
        self.assertTrue(same_bucket("a", "a", 8))
        self.assertGreaterEqual(bucket("a", 8), 0)
        self.assertLess(bucket("a", 8), 8)
        with self.assertRaises(ValueError):
            bucket("a", 0)


if __name__ == "__main__":
    unittest.main()
