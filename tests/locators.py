
class RegistrationPageLocators:
    NAME_FIELD = "//label[text()='Имя']/following::input[1]" # для поля Имя (регистрация)
    EMAIL_FIELD = "//label[text()='Email']/following::input[1]" # для поля Email (регистрация)
    PASSWORD_FIELD = "//label[text()='Пароль']/following::input[1]" # для поля Пароль (регистрация)
    SUBMIT_BUTTON = "//button[text()='Зарегистрироваться']" # для кнопки Зарегистрироваться
    ERROR_MESSAGE_PASSWORD = "//p[text()='Некорректный пароль']"  # для сообщения об ошибке пароля

class AuthorizationLocators:
    EMAIL_FIELD = "//label[text()='Email']/following::input[1]" # для поля Имя (авторизация)
    PASSWORD_FIELD = "//label[text()='Пароль']/following::input[1]" # для поля Пароль (авторизация)
    ENTER_BUTTON = "//button[text()='Войти']" # для кнопки "Войти"
    LOGIN_BUTTON = "//button[text()='Войти в аккаунт']"  # Кнопка "Войти в аккаунт"
    PERSONAL_ACCOUNT_BUTTON = "//a[@href='/account']"  # Кнопка "Личный кабинет"
    REGISTER_BUTTON = "//a[text()='Войти']"  # Кнопка "Войти" на странице регистрации
    RECOVERY_BUTTON = "//a[text()='Войти']"  # Кнопка "Войти" на странице восстановления пароля
    LOGOUT_BUTTON = "//button[text()='Выход']" #Кнопка "Выход"

class NavigationLocators:
    CONSTRUCTOR_BUTTON = "//p[text()='Конструктор']" # Локатор для кнопки "Конструктор"
    LOGO = '//*[@id="root"]/div/header/nav/div' # Локатор для логотипа Stellar Burgers
    BULKI_BUTTON = "//span[text()='Булки']" #Локатор для кнопки "Булки"
    SAUSES_BUTTON = "//span[text()='Соусы']" #Локатор для кнопки "Соусы"
    FILLINGS_BUTTON = "//span[text()='Начинки']" #Локатор для кнопки "Начинки"