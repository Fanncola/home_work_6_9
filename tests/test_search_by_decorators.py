from selene import browser, be, by
import allure


@allure.step('Открываем github')
def open_github():
    browser.open("https://github.com")


@allure.step('Ищем репозиторий')
def search_repository():
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()


@allure.step('Переходим в Issues')
def move_to_issues():
    browser.element("#issues-tab").click()


@allure.step(f'Ищем issue')
def search_issue(issue):
    browser.element(by.partial_text(issue)).should(be.visible)


def test_github(set_window_size):
    open_github()
    search_repository()
    move_to_issues()
    search_issue('#76')
