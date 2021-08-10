import os
from datetime import datetime

import names

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_registration(driver, dotenv, get_sms, get_link):
    # Открытие сайта
    driver.get(os.environ['url_reg'])
    element = driver.find_element_by_css_selector(".typography-1:nth-child(1)")
    assert element.text == "Get started"

    # Ввод имя, фамилии и телефона
    name = driver.find_element_by_id("reg-name")
    name.send_keys(names.get_first_name())
    surname = driver.find_element_by_id("reg-surname")
    surname.send_keys(names.get_last_name())
    pfone = driver.find_element_by_id("phone")
    pfone.send_keys(os.environ['phone'])
    next_step = driver.find_element_by_id("reg-next-step")
    next_step.click()
    element = driver.find_element_by_css_selector(".d-flex > span")
    assert element.text != "Code cannot be ask at the moment. Please, try later."
    # Получение кода смс
    (
        WebDriverWait(driver, 10)
            .until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".typography-1:nth-child(1)"), 'Enter the code'))
    )
    # enter_the_code = driver.find_element_by_css_selector('.text-input')
    message_sent_after = datetime.now()
    (
        WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-input")))
            .send_keys(get_sms.read_sms(message_sent_after).split()[-1])
    )
    # enter_the_code.send_keys(get_sms.read_sms().split()[-1])
    confirm_number = driver.find_element_by_id("confirm-number")
    confirm_number.click()

    # Ввод данных о компании и почты
    (
        WebDriverWait(driver, 10)
            .until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".typography-1:nth-child(1)"), "Company info"))
    )
    company_name = driver.find_element_by_id("company")
    company_name.send_keys('QWERTY')
    role_in_company = driver.find_element_by_id("role")
    role_in_company.send_keys('QWERTY')
    your_business_email = driver.find_element_by_id("email")
    your_business_email.send_keys(os.environ['mail'])
    submit = driver.find_element_by_id("company-info-form-submit")
    submit.click()

    # Получение ссылки по почте
    (
        WebDriverWait(driver, 10)
            .until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".typography-1:nth-child(1)"), 'Follow the link'))
    )
    driver.get(get_link.get_link_for_mail())

    # Ввод пароля
    (
        WebDriverWait(driver, 10)
            .until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".mb-4"), 'Create password'))
    )
    (
        WebDriverWait(driver, 3)
            .until(EC.visibility_of_element_located((By.ID, "password")))
            .send_keys(os.environ['password'])
    )
    (
        WebDriverWait(driver, 5)
            .until(EC.visibility_of_element_located((By.ID, "confirm")))
            .send_keys(os.environ['password'])
    )
    (
        WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located((By.ID, "create-password")))
            .click()
    )
    (
        WebDriverWait(driver, 15)
            .until(EC.text_to_be_present_in_element((By.ID, "case-name-input"), 'My Case'))
    )
