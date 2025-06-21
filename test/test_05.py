import unittest
from test.base import TestSetup
from selenium.webdriver.common.by import By

class TestReadMoreLink(TestSetup):
    def test_read_more_link_opens_post(self):
        links = self.driver.find_elements(By.LINK_TEXT, "Read More")
        if links:
            links[0].click()
            self.assertIn("Post", self.driver.page_source)
        else:
            self.skipTest("No 'Read More' links found.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
