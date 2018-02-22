import logging
from constants import logger
from constants_private import FIRSTRADE, NUMBER_MAPPING

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)


def get_balance(user='Troy'):
    driver = webdriver.Chrome()
    driver.get("https://www.firstrade.com/content/en-us/welcome")
    logger.info('Log in Firstrade account: {}'.format(user))

    # log in
    elem_username = driver.find_element_by_name("username")
    elem_username.clear()
    elem_username.send_keys(FIRSTRADE[user]['username'])
    elem_password = driver.find_element_by_name("password")
    elem_password.clear()
    elem_password.send_keys(FIRSTRADE[user]['password'])
    elem_password.send_keys(Keys.RETURN)

    # pin page
    if driver.current_url == "https://invest.firstrade.com/cgi-bin/enter_pin":
        for key in _decode_pin(FIRSTRADE[user]['pin']):
            element = driver.find_element_by_id(key)
            element.click()
        element = driver.find_element_by_id("submit")
        element.click()

    # fetch balance data
    if driver.current_url == "https://invest.firstrade.com/cgi-bin/main#/cgi-bin/acctbalance":
        logger.info('Fetching account balance')
        element = driver.find_element_by_xpath('//table[@class="total_all"]/tbody/tr/td')
        balance = _format_balance(element.text)

    # close driver
    logger.info('Closing driver')
    driver.close()

    return balance


def _decode_pin(pin):
    return [NUMBER_MAPPING[key] for key in list(pin)]


def _format_balance(balance):
    for char in ['$', ',']:
        balance = balance.replace(char, '')
    return float(balance)
