import logging
from constants import logger
from constants_private import CPWM

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)


def get_balance():
    driver = webdriver.Chrome()
    driver.get("https://www.firstrade.com/content/en-us/welcome")
    logger.info('Log in Firstrade account: {}'.format(user))

    # log in
    elem_username = driver.find_element_by_id("usernameMasked")
    elem_username.clear()
    elem_username.send_keys(CPWM['username'])
    elem_password = driver.find_element_by_name("password")
    elem_password.clear()
    elem_password.send_keys(CPWM['password'])
    elem_password.send_keys(Keys.RETURN)

    # # fetch balance data
    # if driver.current_url == "https://invest.firstrade.com/cgi-bin/main#/cgi-bin/acctbalance":
    #     logger.info('Fetching account balance')
    #     element = driver.find_element_by_xpath('//table[@class="total_all"]/tbody/tr/td')
    #     balance = _format_balance(element.text)

    # close driver
    logger.info('Closing driver')
    driver.close()

    # return balance
    return None


def _format_balance(balance):
    for char in ['$', ',']:
        balance = balance.replace(char, '')
    return float(balance)
