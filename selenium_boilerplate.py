"""
pip install selenium
"""

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win6; x644) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_DRIVER_PATH = ROOT_DIR + "chromedriver.exe"
START_URL = "https://images.google.com"


class Bot(object):

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument(f'--proxy-server={Storage.get_random_proxy()}')
        self.options.add_argument("--window-size=1920, 1080")
        self.options.add_argument(f'user-agent={USER_AGENT}')
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_argument("--disable-blink-features")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=self.options)
        self.w = WebDriverWait(self.driver, 20)
        self.short_w = WebDriverWait(self.driver, 5)
        self.long_w = WebDriverWait(self.driver, 35)
        self.driver.get(START_URL)
        self.get_data()

    def get_data(self):
        articles = self.w.until(EC.visibility_of_all_elements_located((By.XPATH, "//article")))
        next_button = self.w.until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Next Page']")))
        next_button.click()
