import unittest
import time
from test.base import TestSetup  # Make sure your folder is named 'tests'
from selenium.webdriver.common.by import By

class TestEditPost(TestSetup):
    def test_edit_post_title(self):
        edit_buttons = self.driver.find_elements(By.XPATH, "//button[@aria-label='Edit']")
        if edit_buttons:
            edit_buttons[0].click()
            title_field = self.driver.find_element(By.NAME, "title")
            title_field.clear()
            title_field.send_keys("Updated by Selenium")
            self.driver.find_element(By.XPATH, "//button[contains(text(),'Update')]").click()
            time.sleep(1)
            self.assertIn("Updated by Selenium", self.driver.page_source)
        else:
            self.skipTest("No post available to edit.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
