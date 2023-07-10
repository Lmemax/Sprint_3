from selenium.webdriver.common.by import By


class TestLocators:
    CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")  # кнопка Конструктор
    LOGO = (By.XPATH, ".//*[contains(@class, 'header__logo')]")  # логотип сайта
    PERSONAL_AREA = (By.XPATH, ".//p[text()='Личный Кабинет']")  # кнопка личный кабинет
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # кнопка выход в личном кабинете
    ENTER_IN_ACCOUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # кнопка войти в аккаунт
    CHAPTER_ROLLS = (By.XPATH, ".//div/div/*[text()='Булки']")  # кнопка выбор булок
    CHAPTER_SOUSE = (By.XPATH, ".//div/div/*[text()='Соусы']")  # кнопка выбор соуса
    CHAPTER_FILLING = (By.XPATH, ".//div/div/*[text()='Начинки']")  # кнопка выбор начинки
    EXAM_SOUSE = (By.XPATH, ".//img[@alt='Соус традиционный галактический']")  # проверка для перехода в раздел Cоусы
    EXAM_ROLLS = (By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']")  # проверка для перехода в раздел Булки
    BEFORE = (By.XPATH, ".//*[@href='/ingredient/61c0c5a71d1f82001bdaaa70']")
    EXAM_FILLING = (By.XPATH, ".//img[@alt='Говяжий метеорит (отбивная)']")  # проверка для перехода в раздел Начинки
    BAD_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")  # ошибка при некорректном пароле
    BUTTON_ENTER = (By.XPATH, ".//*[text()='Войти']")  # кнопка входа
    LINK_ENTER = (By.XPATH, ".//a[@href='/login']")  # ссылка для входа при регистрации
    REGISTRATION = (By.XPATH, ".//a[text()='Зарегистрироваться']")  # cсылка для перехода к регистрации
    REG_NAME = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")  # поле ввода имени
    REG_EMAIL = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  # поле ввода email
    REG_PASSWORD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")  # поле ввода пароля
    REG_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # кнопка подтверждения регистрации
    EMAIL = (By.XPATH, ".//*[text()='Email']/following-sibling::input")  # поле ввода email
    PASSWORD = (By.XPATH, ".//*[text()='Пароль']/following-sibling::input")  # поле ввода пароля
    RESTORE_PASSWORD = (By.XPATH, ".//a[text()='Восстановить пароль']")  # кнопка восстановить пароль
    RESTORE_EMAIL = (By.XPATH, ".//a[text()='Восстановить пароль']")  # поле ввода email для восстановления пароля
    BUTTON_RESTORE = (By.XPATH, ".//*[text()='Восстановить']")  # кнопка восстановить
    BUTTON_RESTORE_ENTER = (By.XPATH, ".//*[text()='Войти']")  # кнопка для входа, если восстановления не нужно
    BUTTON_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")  # кнопка оформить заказ
