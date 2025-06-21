import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

class TestSetup(unittest.TestCase):
    BASE_URL = 'https://postmanager.vercel.app/'
    TIMEOUT = 30

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--unsafely-treat-insecure-origin-as-secure=https://postmanager.vercel.app')

        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.wait = WebDriverWait(cls.driver, cls.TIMEOUT)
        cls.driver.get(cls.BASE_URL)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
