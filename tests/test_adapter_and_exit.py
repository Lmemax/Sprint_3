from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from Locators import TestLocators


class TestAdapterExitSite:

    def test_adapter_personal_area(self, driver, rightly):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.EMAIL).send_keys(rightly.email)
        driver.find_element(*TestLocators.PASSWORD).send_keys(rightly.password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.BUTTON_ORDER)))
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.EXIT_BUTTON)))
        assert driver.find_element(*TestLocators.EXIT_BUTTON).is_displayed()

    def test_adapter_constructor(self, driver, rightly):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.EMAIL).send_keys(rightly.email)
        driver.find_element(*TestLocators.PASSWORD).send_keys(rightly.password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.BUTTON_ORDER)))
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.EXIT_BUTTON)))
        driver.find_element(*TestLocators.CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.CHAPTER_ROLLS)))
        assert driver.find_element(*TestLocators.CHAPTER_ROLLS).is_displayed()

    def test_adapter_logo(self, driver, rightly):
        """Этот тест проверяет переход из личного кабинета на главную страницу по клику на логотип сайта"""
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.EMAIL).send_keys(rightly.email)
        driver.find_element(*TestLocators.PASSWORD).send_keys(rightly.password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.BUTTON_ORDER)))
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.EXIT_BUTTON)))
        driver.find_element(*TestLocators.LOGO).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.BUTTON_ORDER)))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_exit_site(self, driver, rightly):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.EMAIL).send_keys(rightly.email)
        driver.find_element(*TestLocators.PASSWORD).send_keys(rightly.password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.BUTTON_ORDER)))
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.EXIT_BUTTON)))
        driver.find_element(*TestLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.BUTTON_ENTER)))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
