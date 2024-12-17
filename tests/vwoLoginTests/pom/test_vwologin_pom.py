import time
import allure
import pytest
import selenium
from selenium import webdriver
from tests.pageObjects.loginPage import LogInPage
from tests.pageObjects.dashboardPage import DashboardPage
from selenium.webdriver.common.by import By


class TestLogin:

    def __init__(self):
        self.password = None
        self.name = None
        self.base_url = None

    @allure.epic("VWO Login Test")
    @allure.feature("TC#0 - VWO App Negative Test")
    @pytest.mark.usefixtures("setup")
    @pytest.mark.negative
    def test_vwo_login_negative(self, setup):
        driver = setup
        driver.get(self.base_url)
        loginPage = LogInPage(driver)
        loginPage.login_vwo(username="test@gmail.com", password="12345")
        time.sleep(10)
        error_message = loginPage.get_error_message_text()
        assert error_message == "Your email, password, IP address or location did not match"

    @allure.epic("VWO Login Test")
    @allure.feature("TC#1 - VWO App positive Test")
    @pytest.mark.usefixtures("setup")
    @pytest.mark.positive
    def test_vwo_login_positive(self, setup):
        driver = setup
        driver.get(self.base_url)
        loginPage = LogInPage(driver)

        loginPage.login_vwo(username=self.name, password=self.password)
        time.sleep(5)
        dashboard_page = DashboardPage(driver)
        assert "Dashboard" in driver.title
        assert "test aaa" in dashboard_page.user_logged_in_text()