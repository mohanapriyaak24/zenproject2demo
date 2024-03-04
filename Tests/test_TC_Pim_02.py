import pytest
from config.config import TestData
from Pages.Loginpage import LoginPage
from Tests.test_base import BaseTest
from Pages.Homepage import Admin
from time import sleep


class Test_Header(BaseTest):

    def get_page_title(self):
        self.loginPage = LoginPage(self.driver)
        Title = self.loginPage.get_title(TestData.PAGE_TITLE)
        assert Title == TestData.PAGE_TITLE

    def test_login_02(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(3)

    def test_user_management(self):
        self.homepage = Admin(self.driver)
        sleep(3)
        self.homepage.do_click_admin()
        self.homepage.user_management()
        self.homepage.validate_jobs()
        self.homepage.validate_organisation()
        self.homepage.validate_nationality()
        self.homepage.validate_config()
        self.homepage.validate_corporate()
        self.homepage.validate_qualification()





