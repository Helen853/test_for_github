import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def github_desktop():
    browser.config.window_width = 1400
    browser.config.window_height = 1200
    yield


@pytest.fixture(scope='function')
def github_mobile():
    browser.config.window_width = 830
    browser.config.window_height = 530
    yield


def test_browser(github_desktop):
    browser.open_url('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_mobile_browser(github_mobile):
    browser.open_url('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
