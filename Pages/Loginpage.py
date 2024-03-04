from Pages.Basepage import BasePage
from selenium.webdriver.common.by import By
from config.config import TestData


class LoginPage(BasePage):
    USERNAME = (By.XPATH, "//input[@name='username']")
    RESET_BUTTON = (By.XPATH, "//button[@type='submit']")
    FORGET_PASSWORD = (By.XPATH, "//p[.='Forgot your password? ']")
    PASSWORD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.do_sendkeys(self.USERNAME, username)
        self.do_sendkeys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

    def clk_forget_password(self, username):
        self.do_click(self.FORGET_PASSWORD)
        self.do_sendkeys(self.USERNAME, username)
        self.do_click(self.RESET_BUTTON)
