import pytest
from selenium import webdriver
from Eater import Eaterburger


@pytest.fixture
def wronger():  # регистрация с неправильным паролем меньше 6 знаков
    return Eaterburger(name = 'Max', email = 'MaxIudin11123@yandex.ru', password = 'yame1')

@pytest.fixture
def rightly():  ## регистрация и данные для входа на сайт
    return Eaterburger(name = 'Max', email = 'MaxIudin11123@yandex.ru', password = 'yame12')

@pytest.fixture(scope='function')  # при каждом новом тесте браузер перезапускается
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()
