import pytest
from selene import browser

google = 'https://www.google.com/ncr'
@pytest.fixture(autouse=True)
def set_up_browser_settings():
    browser.open(google)
    browser.config.window_height = 768
    browser.config.window_width = 1066
    yield
    browser.quit()
