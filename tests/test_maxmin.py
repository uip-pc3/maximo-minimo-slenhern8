import unittest
from maxmin import min_val, max_val

class Testmaxmin(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_val(4,5),5)

    def test_min(self):
        self.assertEqual(min_val(4,5),4)


if __name__ == '__main__':
    unittest.main()