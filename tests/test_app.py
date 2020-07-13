import os
import unittest
from pathlib import Path

ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent


class AppTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_manuel(self):
        self.assertEqual(True, True)

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
