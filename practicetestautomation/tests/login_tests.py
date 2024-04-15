import pytest
from selenium.webdriver.common.by import By

from practicetestautomation.infra import WebsiteURL, Messages
from practicetestautomation.pages import LoginPage
from practicetestautomation.utils.drivers.driver_factory import DriverFactory
from practicetestautomation.utils.users.user_credentials import UserCredentials


@pytest.fixture
def driver():
    driver_factory = DriverFactory('chrome')
    driver = driver_factory.create_driver()
    driver.get(WebsiteURL.PRACTICE_AUTOMATION)
    yield driver


@pytest.mark.order(1)
def test_positive_login(driver):
    login_page = LoginPage(driver)
    login_page.login(UserCredentials.VALID_USERNAME, UserCredentials.VALID_PASSWORD)
    assert Messages.SUCCESS_LOGIN in driver.current_url
    assert Messages.CONGRATULATIONS in driver.page_source or Messages.SUCCESSFULLY_LOGGED_IN in driver.page_source
    assert driver.find_element(By.LINK_TEXT, "Log out").is_displayed()


@pytest.mark.order(2)
def test_negative_username(driver):
    login_page = LoginPage(driver)
    login_page.login(UserCredentials.INVALID_USERNAME, UserCredentials.VALID_USERNAME)
    login_page.invalid_user()


def test_negative_password(driver):
    login_page = LoginPage(driver)
    login_page.login(UserCredentials.VALID_USERNAME, UserCredentials.INVALID_PASSWORD)
    login_page.invalid_password()


if __name__ == '__main__':
    pytest.main(['-v', '--strict-markers', 'tests/'])
