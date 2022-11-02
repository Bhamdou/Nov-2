import unittest
from string_operations import name_title

class TestTitle(unittest.TestCase):

    def test_title(self):
        self.assertEqual(name_title("hello", "world"),("Hello","World"))
        
if __name__=='__main__':
    unittest.main()