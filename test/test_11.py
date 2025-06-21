import unittest
import time
from test.base import TestSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestPageLoadTime(TestSetup):
    def test_page_loads_under_5_seconds(self):
        start = time.time()
        self.driver.get(self.BASE_URL)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        load_duration = time.time() - start
        self.assertLess(load_duration, 5, f"Page took too long to load: {load_duration:.2f} seconds")

if __name__ == "__main__":
    unittest.main(verbosity=2)
