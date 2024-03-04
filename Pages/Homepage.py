from Pages.Basepage import BasePage
from selenium.webdriver.common.by import By
from config.config import TestData


class Admin(BasePage):
    ADMIN = (By.XPATH, "//a[.='Admin']")
    USER_MANAGEMENT = (By.XPATH, "//li[contains(.,'User Management')]")
    JOBS = (By.XPATH, "//li[contains(.,'Job')]")
    ORGANISATION = (By.XPATH, "//li[contains(.,'Organization')]")
    NATIONALITY = (By.XPATH, "//a[contains(.,'Nationalities')]")
    CORPORATE = (By.XPATH, "//li[contains(.,'Corporate Branding')]")
    QUALIFICATION = (By.XPATH, "//li[contains(.,'Qualifications')]")
    CONFIG = (By.XPATH, "//li[contains(.,'Configuration')]")

    # (By.XPATH, "")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def maximize_win(self):
        self.maximize_wind()

    def do_click_admin(self):
        self.do_click(self.ADMIN)

    def validate_jobs(self):
        return self.is_display(self.JOBS)

    def validate_organisation(self):
        return self.is_display(self.ORGANISATION)

    def validate_nationality(self):
        return self.is_display(self.NATIONALITY)

    def validate_corporate(self):
        return self.is_display(self.CORPORATE)

    def validate_config(self):
        return self.is_display(self.CONFIG)

    def validate_qualification(self):
        return self.is_display(self.QUALIFICATION)

    def user_management(self):
        return self.is_display(self.USER_MANAGEMENT)
