from selene import browser, be, by
import allure


def test_github(set_window_size):
    with allure.step('Открываем github'):
        browser.open("https://github.com")

    with allure.step('Ищем репозиторий'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Переходим в Issues'):
        browser.element("#issues-tab").click()

    with allure.step('Ищем Issue 76'):
        browser.element(by.partial_text("#76")).should(be.visible)
