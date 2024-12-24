from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I am on the Google Home page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://www.google.com')


@when('I search for "{search_term}"')
def step_impl(context, search_term):
    search_box = context.browser.find_element(By.NAME, 'q')
    search_box.send_keys(search_term)
    search_box.submit()


@then('I should see the "{expected_term}" in the results')
def step_impl(context, expected_term):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    assert expected_term in context.browser.page_source
    context.browser.quit()

