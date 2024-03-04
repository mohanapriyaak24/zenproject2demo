from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_sendkeys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return ele.text

    def get_title(self, Title):
        WebDriverWait(self.driver, 10).until(EC.title_is(Title))
        return self.driver.title

    def is_display(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ele.is_displayed()
        return bool(ele)

    def maximize_wind(self):
        self.driver.maximize_window()







