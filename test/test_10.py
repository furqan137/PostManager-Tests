import unittest
from test.base import TestSetup  # ✅ Assumes your folder is named 'tests'

class TestUrlContainsIP(TestSetup):
    def test_current_url_has_domain(self):
        # current_url returns the full URL, so include protocol in assertion
        self.assertIn("postmanager.vercel.app", self.driver.current_url)

if __name__ == "__main__":
    unittest.main(verbosity=2)
