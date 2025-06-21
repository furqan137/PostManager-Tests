import unittest
from test.base import TestSetup  # Adjust if your folder is named "test"
from selenium.webdriver.common.by import By

class TestNavigateNewPost(TestSetup):
    def test_click_new_post_button(self):
        self.driver.find_element(By.LINK_TEXT, "New Post").click()
        self.assertIn("post", self.driver.current_url)

if __name__ == "__main__":
    unittest.main(verbosity=2)
