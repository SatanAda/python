import pytest

from selenium import webdriver
from funkcii.imap import imap
from funkcii.aktivator import SMSActivator


@pytest.fixture (autouse=True)
def driver():
    driver = webdriver.Chrome ()
    driver.maximize_window ()
    return driver


@pytest.fixture (scope='class')
def auth():
    mail = imap ()
    link = mail
    return link


@pytest.fixture (scope='session')
def get_number():
    activator = SMSActivator ()
    phone_number = activator.get_number ()
    return phone_number,


@pytest.fixture (scope='session')
def wait_sms():
    activator = SMSActivator ()
    code = activator.wait_sms ()
    return code
