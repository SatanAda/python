import datetime

import pytest

from dotenv import load_dotenv
from selenium import webdriver

from utils.imap import imap
from utils.twillio import SmsFromTwillio


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    return driver


@pytest.fixture(scope='session')
def get_link():
    return imap()


@pytest.fixture(autouse=True)
def dotenv():
    return load_dotenv()


@pytest.fixture(scope='session')
def get_sms():
    return SmsFromTwillio()
