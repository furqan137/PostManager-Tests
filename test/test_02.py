import unittest
from test.base import TestSetup  # 👈 Adjusted to match your folder name if it's still 'test'
from selenium.webdriver.common.by import By

class TestSearchFieldPresent(TestSetup):
    def test_search_input_field_is_visible(self):
        search = self.driver.find_element(By.XPATH, "//input[@placeholder='Search posts...']")
        self.assertTrue(search.is_displayed(), "Search input field is not visible.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
