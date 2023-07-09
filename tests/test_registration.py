import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from Locators import TestLocators


class TestBurgersSiteRegistration:
    def test_registration_wrong_password(self, driver, wronger):
        driver.find_element(*TestLocators.ENTER_IN_ACCOUNT).click()
        driver.find_element(*TestLocators.REGISTRATION).click()
        driver.find_element(*TestLocators.REG_NAME).send_keys(wronger.name)
        driver.find_element(*TestLocators.REG_EMAIL).send_keys(wronger.email)
        driver.find_element(*TestLocators.REG_PASSWORD).send_keys(wronger.password)
        driver.find_element(*TestLocators.REG_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(
            TestLocators.BAD_PASSWORD))
        assert driver.find_element(*TestLocators.BAD_PASSWORD).is_displayed()

    def test_registration_rigth_password(self, driver, rightly):
        driver.find_element(*TestLocators.ENTER_IN_ACCOUNT).click()
        driver.find_element(*TestLocators.REGISTRATION).click()
        driver.find_element(*TestLocators.REG_NAME).send_keys(rightly.name)
        driver.find_element(*TestLocators.REG_EMAIL).send_keys(rightly.email)
        driver.find_element(*TestLocators.REG_PASSWORD).send_keys(rightly.password)
        driver.find_element(*TestLocators.REG_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(
            TestLocators.BUTTON_ENTER))
        assert driver.find_element(*TestLocators.BUTTON_ENTER).is_displayed()
