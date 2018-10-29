import unittest
import sys


class SkipTests(unittest.TestCase):
    @unittest.expectedFailure
    def test_fails(self):
        self.assertEqual(False, True)

    @unittest.skip("Test is useless")
    def test_skip(self):
        self.assertEqual(False, True)

    @unittest.skipIf(sys.version_info.minor == 7, "broken on 3.7")
    def test_skipif(self):
        self.assertEqual(False, True)

    @unittest.skipUnless(
        sys.platform.startswith("linux"), "broken unless on linux"
    )
    def test_skipunless(self):
        self.assertEqual(False, True)


if __name__ == "__main__":
    unittest.main()
