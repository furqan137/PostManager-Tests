import unittest
from test.base import TestSetup  # Make sure your folder is named 'tests'
 
class TestHomePageLoad(TestSetup):
    def test_homepage_loads(self):
        self.driver.get(self.BASE_URL)
        self.assertIn("Posts", self.driver.page_source)

if __name__ == "__main__":
    unittest.main(verbosity=2)
