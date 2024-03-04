from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import pytest


class TestData:
    CHROME_EXECUTABLE_PATH = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    FIREFOX_EXECUTABLE_PATH = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USER_NAME = "Admin"
    PASSWORD = "admin123"
    PAGE_TITLE = "OrangeHRM"
