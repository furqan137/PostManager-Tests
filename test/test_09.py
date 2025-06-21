import unittest
from test.base import TestSetup
from selenium.webdriver.common.by import By

class TestSortClick(TestSetup):
    def test_sort_button_clickable(self):
        sort = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Newest')]")
        sort.click()
        self.assertTrue(sort.is_displayed())

if __name__ == "__main__":
    unittest.main(verbosity=2)
