import unittest
from test.base import TestSetup  # ✅ use 'test.base' if your folder is named 'test'
from selenium.webdriver.common.by import By

class TestSortButtonVisible(TestSetup):
    def test_sort_button_visible(self):
        sort = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Newest')]")
        self.assertTrue(sort.is_displayed(), "Sort button is not visible.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
