from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from Locators import TestLocators


class TestEnterBurgersSite:
    def test_enter_account(self, driver, rightly):
        driver.find_element(*TestLocators.ENTER_IN_ACCOUNT).click()
        driver.find_element(*TestLocators.EMAIL).send_keys(rightly.email)
        driver.find_element(*TestLocators.PASSWORD).send_keys(rightly.password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.BUTTON_ORDER)))
        assert driver.find_element(*TestLocators.BUTTON_ORDER).is_displayed()

    def test_enter_personal_area(self, driver, rightly):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.EMAIL).send_keys(rightly.email)
        driver.find_element(*TestLocators.PASSWORD).send_keys(rightly.password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.BUTTON_ORDER)))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/" and driver.find_element(
            *TestLocators.BUTTON_ORDER).is_displayed()

    def test_enter_from_reg_form(self, driver, rightly):
        driver.find_element(*TestLocators.ENTER_IN_ACCOUNT).click()
        driver.find_element(*TestLocators.REGISTRATION).click()
        driver.find_element(*TestLocators.LINK_ENTER).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((
            TestLocators.BUTTON_ENTER)))
        driver.find_element(*TestLocators.EMAIL).send_keys(rightly.email)
        driver.find_element(*TestLocators.PASSWORD).send_keys(rightly.password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.BUTTON_ORDER)))
        assert driver.find_element(*TestLocators.BUTTON_ORDER).is_displayed()

    def test_enter_restore_form(self, driver, rightly):
        driver.find_element(*TestLocators.ENTER_IN_ACCOUNT).click()
        driver.find_element(*TestLocators.RESTORE_PASSWORD).click()
        driver.find_element(*TestLocators.LINK_ENTER).click()
        WebDriverWait(driver, 3).until(ec.element_to_be_clickable((
            TestLocators.BUTTON_ENTER)))
        driver.find_element(*TestLocators.EMAIL).send_keys(rightly.email)
        driver.find_element(*TestLocators.PASSWORD).send_keys(rightly.password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.BUTTON_ORDER)))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
