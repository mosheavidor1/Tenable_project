from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from practicetestautomation.infra.messages import Messages


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.XPATH, "//input[@id='username']")
        self.password_field = (By.XPATH, "//input[@id='password']")
        self.submit_button = (By.XPATH, "//button[@id='submit']")
        self.invalid_user_error = (By.XPATH, "//div[contains(text(),'Your username is invalid!')]")
        self.invalid_password_error = (By.XPATH, "//div[contains(text(),'Your password is invalid!')]")
        self.wait = WebDriverWait(self.driver, 10)

    def enter_text(self, locator, text, field_name):
        try:
            field = self.wait.until(EC.visibility_of_element_located(locator))
            field.send_keys(text)
        except:
            print(f"{field_name} field is not clickable")

    def check_error_message(self, locator, expected_message):
        try:
            error_message = self.wait.until(EC.visibility_of_element_located(locator))
            assert error_message.text == expected_message
            print(error_message.text)
        except:
            pass

    def click_login_button(self):
        try:
            login_button = self.wait.until(EC.visibility_of_element_located(self.submit_button))
            login_button.click()
        except:
            pass

    def login(self, username, password):
        self.enter_text(self.username_field, username, Messages.USER_ELEMENT_ERROR)
        self.enter_text(self.password_field, password, Messages.PASSWORD_ELEMENT_ERROR)
        self.click_login_button()

    def invalid_user(self):
        self.check_error_message(self.invalid_user_error, Messages.USER_INVALID_MESSAGE)

    def invalid_password(self):
        self.check_error_message(self.invalid_password_error, Messages.PASSWORD_INVALID_MESSAGE)
