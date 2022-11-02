import unittest
from string_operations import join_name

class TestString(unittest.TestCase):
    
    def test_str(self):
        self.assertEqual(join_name(["bahaa","ahmad","zied"]),"bahaaahmadzied")
        
if __name__=='__main__':
    unittest.main()
            
