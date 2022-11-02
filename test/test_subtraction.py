import unittest
import math_operations

class TestSubtraction(unittest.TestCase):
    def test_subtraction(self):
        self.assertEqual(math_operations.subtraction(2, 2),0)
        
if __name__=='__main__':
    unittest.main()
            