import unittest
import math_operations

class TestMultiplication(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(math_operations.multiplication(2, 2),4)
        
if __name__=='__main__':
    unittest.main()
            