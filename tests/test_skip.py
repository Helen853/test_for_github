import pytest
from selene.support.shared import browser
from selene import have
from tests import size


@pytest.fixture(params=[(1400, 1200), (830, 530)], ids=['desktop', 'mobile'])
def browser_config(request):
    browser.config.window_width = request.param[0]
    browser.config._window_height = request.param[1]
    browser.open('https://github.com')
    yield

def test_browser(browser_config):
    if (browser.config.window_width, browser.config.window_height) not in size.desktop:
        pytest.skip('Test skip because  not apply to desktop testing')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))


def test_mobile_browser(browser_config):
    if (browser.config.window_width, browser.config.window_height) not in size.mobile:
        pytest.skip('Test skip because  not apply to mobile testing')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))