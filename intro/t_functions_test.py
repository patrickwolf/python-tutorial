'''
Created on Jul 28, 2013

@author: Patrick
'''
import unittest
import t_functions as f

class Test(unittest.TestCase):

    def test_add(self):
        result = f.add(5)
        self.assertEqual(result, 5)
        self.assertEqual(f.add(5, 10), 15)
        self.assertEqual(f.add(5, cint=20), 25)
        
    def test_multiadd(self):
        self.assertEqual(f.multiadd(5, 10), 15)
        self.assertEqual(f.multiadd(5, 20), 25)
        self.assertEqual(f.multiadd(5, 20, 100, 200), 325)


if __name__ == "__main__":
    unittest.main()\
