from behave import given, when, then
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


@given('open the app.vwo.com')
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    context.browser = webdriver.Chrome(options=chrome_options)
    context.browser.get("https://app.vwo.com/")


@when('I enter {username} and {password}')
def step_impl(context, username, password):
    username_element = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "login-username"))
    )
    username_element.send_keys(username)
    password_element = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_element.send_keys(password)


@when('I click the sign-in button')
def step_impl(context):
    sign_in_element = context.browser.find_element(By.ID, "js-login-btn")
    sign_in_element.click()


@then('I get this {message}')
def step_impl(context, message):
    try:
        # Wait for the notification box to appear
        notification_box = WebDriverWait(context.browser, 20).until(
            EC.presence_of_element_located((By.ID, "js-notification-box-msg"))
        )
        print(notification_box.text)
        context.browser.save_screenshot("screenshot.png")

        # Get the actual message text
        actual_message = notification_box.text
        print(actual_message)


        # Assert the expected message matches the actual message
        assert message in actual_message, f"Expected message '{message}', but got '{actual_message}'"

    finally:
        # Quit the browser regardless of success or failure
        context.browser.quit()
