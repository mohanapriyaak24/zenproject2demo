import pytest
from config.config import TestData
from Pages.Loginpage import LoginPage
from Tests.test_base import BaseTest
from time import sleep


class Test_forget_password(BaseTest):

    def test_forget_password_01(self):
        self.forgetPassword = LoginPage(self.driver)
        self.forgetPassword.clk_forget_password(TestData.USER_NAME)
        sleep(3)


