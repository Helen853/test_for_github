import pytest
from selene import have
from selene.support.shared import browser


@pytest.fixture(params=[(1400, 1200), (830, 530)])
def browser_config(request):
    browser.config.window_width = request.param[0]
    browser.config._window_height = request.param[1]
    yield


@pytest.mark.parametrize('browser_config', [(1400, 1200)], indirect=True)
def test_browser(browser_config):
    browser.open_url('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))


@pytest.mark.parametrize('browser_config', [(830, 530)], indirect=True)
def test_mobile_browser(browser_config):
    browser.open_url('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))