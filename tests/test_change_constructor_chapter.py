from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from Locators import TestLocators


class TestChangeConstructorChapter:
    def test_change_chapter_rolls(self, driver, rightly):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.EMAIL).send_keys(rightly.email)
        driver.find_element(*TestLocators.PASSWORD).send_keys(rightly.password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.BUTTON_ORDER)))
        driver.find_element(*TestLocators.CHAPTER_SOUSE).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.EXAM_SOUSE)))
        driver.find_element(*TestLocators.CHAPTER_ROLLS).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.EXAM_ROLLS)))
        assert driver.find_element(*TestLocators.EXAM_ROLLS).is_displayed()

    def test_change_chapter_souse(self, driver, rightly):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.EMAIL).send_keys(rightly.email)
        driver.find_element(*TestLocators.PASSWORD).send_keys(rightly.password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.BUTTON_ORDER)))
        driver.find_element(*TestLocators.CHAPTER_SOUSE).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.EXAM_SOUSE)))
        assert driver.find_element(*TestLocators.EXAM_SOUSE).is_displayed()

    def test_change_chapter_filling(self, driver, rightly):
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.EMAIL).send_keys(rightly.email)
        driver.find_element(*TestLocators.PASSWORD).send_keys(rightly.password)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.BUTTON_ORDER)))
        driver.find_element(*TestLocators.CHAPTER_FILLING).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((
            TestLocators.EXAM_FILLING)))
        assert driver.find_element(*TestLocators.EXAM_FILLING).is_displayed()
