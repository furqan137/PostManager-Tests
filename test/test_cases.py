import time
import unittest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PostManagerTests(unittest.TestCase):
    BASE_URL = 'http://34.230.89.192:3000'
    TIMEOUT = 30

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.wait = WebDriverWait(cls.driver, cls.TIMEOUT)
        cls.driver.get(cls.BASE_URL)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # --- 1. Homepage ---
    def test_homepage_loads(self):
        self.driver.get(self.BASE_URL)
        self.assertIn("Posts", self.driver.page_source)

    # --- 2. Title Exists ---
    def test_homepage_title_exists(self):
        self.assertTrue(self.driver.title)

    # --- 3. Search Field Exists ---
    def test_search_field_present(self):
        search = self.driver.find_element(By.XPATH, "//input[@placeholder='Search posts...']")
        self.assertTrue(search.is_displayed())

    # --- 4. Sort Button Exists ---
    def test_sort_button_visible(self):
        sort = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Newest')]")
        self.assertTrue(sort.is_displayed())

    # --- 5. Theme Toggle Exists ---
    def test_theme_toggle_button(self):
        toggle = self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Toggle theme')]")
        self.assertTrue(toggle.is_displayed())

    # --- 6. Click 'New Post' Button ---
    def test_navigate_to_new_post(self):
        self.driver.find_element(By.LINK_TEXT, "New Post").click()
        self.assertIn("post", self.driver.current_url)

    # --- 7. Create Valid Post ---
    def test_create_valid_post(self):
        self.driver.find_element(By.LINK_TEXT, "New Post").click()
        self.driver.find_element(By.NAME, "title").send_keys("Selenium Test Post")
        self.driver.find_element(By.NAME, "author").send_keys("Tester")
        self.driver.find_element(By.NAME, "content").send_keys("Post content written for automated test.")
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Publish')]").click()
        time.sleep(2)
        self.assertIn("Selenium Test Post", self.driver.page_source)

    # --- 8. Try Empty Post Submit ---
    def test_create_invalid_post_empty(self):
        self.driver.find_element(By.LINK_TEXT, "New Post").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Publish')]").click()
        time.sleep(1)
        self.assertIn("required", self.driver.page_source.lower() or "error")

    # --- 9. Read More Works ---
    def test_read_more_link(self):
        links = self.driver.find_elements(By.LINK_TEXT, "Read More")
        if links:
            links[0].click()
            self.assertIn("Post", self.driver.page_source)

    # --- 10. Edit a Post ---
    def test_edit_post(self):
        edit_buttons = self.driver.find_elements(By.XPATH, "//button[@aria-label='Edit']")
        if edit_buttons:
            edit_buttons[0].click()
            title_field = self.driver.find_element(By.NAME, "title")
            title_field.clear()
            title_field.send_keys("Updated by Selenium")
            self.driver.find_element(By.XPATH, "//button[contains(text(),'Update')]").click()
            time.sleep(1)
            self.assertIn("Updated by Selenium", self.driver.page_source)

    # --- 11. Delete a Post ---
    def test_delete_post(self):
        posts = self.driver.find_elements(By.XPATH, "//h2")
        if not posts:
            self.skipTest("No posts to delete.")
        post_title = posts[0].text
        delete_buttons = self.driver.find_elements(By.XPATH, "//button[@aria-label='Delete']")
        delete_buttons[0].click()
        time.sleep(2)
        self.assertNotIn(post_title, self.driver.page_source)

    # --- 12. Search Functionality ---
    def test_search_post(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search posts...']").send_keys("Blog")
        time.sleep(2)
        self.assertIn("Blog", self.driver.page_source)

    # --- 13. Sort Posts ---
    def test_sort_click(self):
        sort = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Newest')]")
        sort.click()
        self.assertTrue(sort.is_displayed())

    # --- 14. Theme Toggle Click ---
    def test_theme_toggle_click(self):
        toggle = self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Toggle theme')]")
        toggle.click()
        self.assertTrue(toggle.is_displayed())

    # --- 15. Footer Present ---
    def test_footer_visible(self):
        footer = self.driver.find_element(By.TAG_NAME, "footer")
        self.assertTrue(footer.is_displayed())

    # --- 16. Page Not 404 ---
    def test_homepage_no_404(self):
        self.assertNotIn("404", self.driver.page_source)

    # --- 17. URL Check ---
    def test_url_contains_ip(self):
        self.assertIn("34.230.89.192", self.driver.current_url)

    # --- 18. Page Loads Fast ---
    def test_page_load_time(self):
        start = time.time()
        self.driver.get(self.BASE_URL)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        duration = time.time() - start
        self.assertLess(duration, 5)

    # --- 19. Edit Button Present ---
    def test_edit_button_exists(self):
        buttons = self.driver.find_elements(By.XPATH, "//button[@aria-label='Edit']")
        self.assertTrue(len(buttons) >= 1)

    # --- 20. Delete Button Present ---
    def test_delete_button_exists(self):
        buttons = self.driver.find_elements(By.XPATH, "//button[@aria-label='Delete']")
        self.assertTrue(len(buttons) >= 1)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PostManagerTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    passed = result.testsRun - len(result.failures) - len(result.errors)
    print(f"\n--- Test Summary ---")
    print(f"Total tests: {result.testsRun}")
    print(f"Passed tests: {passed}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
