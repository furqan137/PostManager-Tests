import time
import unittest
from test.base import TestSetup  # Adjust 'tests' to 'test' if your folder is still named 'test'
from selenium.webdriver.common.by import By

class TestSearchPost(TestSetup):
    def test_search_post_text(self):
        search_box = self.driver.find_element(By.XPATH, "//input[@placeholder='Search posts...']")
        search_box.clear()
        search_box.send_keys("Blog")
        time.sleep(2)
        self.assertIn("Blog", self.driver.page_source)

if __name__ == "__main__":
    unittest.main(verbosity=2)
