import pytest
from selenium import webdriver
from selenium.webdriver import Chrome

import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__),
                           '.env')
load_dotenv(dotenv_path)


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    base_url = os.getenv("BASE_URL")
    username = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")

    print(f"Base URL: {base_url}, Username: {username}, Password: {password}")

    request.cls.driver = driver
    request.cls.base_url = base_url
    request.cls.username = username
    request.cls.password = password

    driver = webdriver.Chrome()
    driver.maximize_window()
    print("DOne!")

    yield driver
    driver.quit()
