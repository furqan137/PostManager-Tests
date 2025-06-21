import time
import unittest
from test.base import TestSetup
from selenium.webdriver.common.by import By

class TestDeletePost(TestSetup):
    def test_delete_post(self):
        posts = self.driver.find_elements(By.XPATH, "//h2")
        if not posts:
            self.skipTest("No posts to delete.")
        post_title = posts[0].text
        delete_buttons = self.driver.find_elements(By.XPATH, "//button[@aria-label='Delete']")
        if delete_buttons:
            delete_buttons[0].click()
            time.sleep(2)
            self.assertNotIn(post_title, self.driver.page_source)
        else:
            self.skipTest("No delete buttons found.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
