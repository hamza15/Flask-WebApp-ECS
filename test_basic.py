from anagram import app
import unittest

class BasicTests(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
    def test_main_page_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

 
if __name__ == "__main__":
    unittest.main()