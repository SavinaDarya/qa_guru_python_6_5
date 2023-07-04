import pytest
from selene import browser,have
from selene import command
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_management():

    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 1080
    browser.config.window_height = 2300
    browser.config.timeout = 4.0

    yield

    browser.quit()
