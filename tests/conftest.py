from selene import browser
import pytest


@pytest.fixture(autouse=True)
def set_window_size():
    browser.config.window_width = 1366
    browser.config.window_height = 768
