import allure

from selene import browser, be, by


@allure.label('owner', 'fanncola')
@allure.feature('Issues')
@allure.story('Find Issues by Selene')
@allure.tag('Web')
@allure.severity(allure.severity_level.CRITICAL)
@allure.link('https://github.com', name='Testing')
def test_github(set_window_size):
    browser.open("https://github.com")

    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("#76")).should(be.visible)
