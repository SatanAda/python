import pytest
from selenium import webdriver
from aktivator import SMSActivator
from sms import activation, response


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


@pytest.fixture(scope='class')
def get_number():
    return str(activation.phone_number)


@pytest.fixture(scope='class')
def wait_sms():
    return response['code']