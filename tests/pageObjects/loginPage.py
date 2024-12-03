"""
Login page class
Responsibility:
Get username and send keys - email
get password and send keys - password
Click submit button and navigate to dashboard
Invalid credentials - error message
Forgot password
"""
# Page class
# Page locators
# Page Actions
# Webdriver initializations
# Custom functions
# No assertions (in page object class)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogInPage:
    def __init__(self, driver):
        self.driver = driver

    # Page locators
    username = (By.ID, "login-username")
    password = (By.NAME, "password")
    sign_in = (By.XPATH, "//button[@id='js-login-btn']")
    #forgot_password_button = (By.XPATH, "//button[text()='Forgot Password?']")
    #remember_me = (By.XPATH, "//span[text()='Remember me']")
    #SSO_signin = (By.XPATH, "//button[text()='Sign in using SSO']")
    #free_trial = (By.XPATH, "//a[text()='Start a free trial']")
    error_message = (By.XPATH, "//div[text()='Your email, password, IP address or location did not match']")

    # Page Actions

    def get_username(self):
        return self.driver.find_element(*LogInPage.username)

    def get_password(self):
        return self.driver.find_element(*LogInPage.password)

    def get_sign_in(self):
        return self.driver.find_element(*LogInPage.sign_in)

    def get_error_message(self):
        return self.driver.find_element(*LogInPage.error_message)

    # Page Action - Main action

    def login_vwo(self, username, password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_sign_in().click()

    def get_error_message_text(self):
        return self.get_error_message().text
