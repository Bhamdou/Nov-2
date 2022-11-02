import unittest
import math_operations

class TestDivision(unittest.TestCase):
    def test_division(self):
        self.assertEqual(math_operations.division(2, 2),1)
        
if __name__=='__main__':
    unittest.main()
            