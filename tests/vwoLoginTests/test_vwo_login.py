import time

import allure
import pytest
import selenium
from selenium import webdriver
from tests.pageObjects.loginPage import LogInPage
from tests.pageObjects.dashboardPage import DashboardPage

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/")
    return driver

@allure.epic("VWO Login Test")
@allure.feature("TC#0 - VWO App Negative Test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    driver = setup
    loginPage = LogInPage(driver)
    loginPage.login_vwo(username="test@gmail.com", password="12345")
    time.sleep(10)
    error_message = loginPage.get_error_message_text()
    assert error_message == "Your email, password, IP address or location did not match"


@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App positive Test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    driver = setup
    loginPage = LogInPage(driver)
    loginPage.login_vwo(username="py4x@testingacademy.com", password="Wingify1234")
    time.sleep(5)
    dashboard_page =  DashboardPage(driver)
    assert "Dashboard" in driver.title
    assert "test aaa" in dashboard_page.user_logged_in_text()


