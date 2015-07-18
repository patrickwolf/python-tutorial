__author__ = 'Patrick'

import unittest
import multi_add as f

class MultiAddTestCase(unittest.TestCase):

    def test_add(self):
        result = f.add(5)
        self.assertEqual(result, 5)
        self.assertEqual(f.add(5, 10), 15)
        self.assertEqual(f.add(5, cint=20), 25)

    def test_multi_add(self):
        self.assertEqual(f.multi_add(5, 10), 15)
        self.assertEqual(f.multi_add(5, 20), 25)
        self.assertEqual(f.multi_add(5, 20, 100, 200), 325)


if __name__ == '__main__':
    unittest.main()
