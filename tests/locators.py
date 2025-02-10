
class RegistrationPageLocators:
    NAME_FIELD = 'fieldset:nth-child(1) > div > div > input' # для поля Имя (регистрация)
    EMAIL_FIELD = 'fieldset:nth-child(2) > div > div > input' # для поля Email (регистрация)
    PASSWORD_FIELD = 'fieldset:nth-child(3) > div > div > input' # для поля Пароль (регистрация)
    SUBMIT_BUTTON = 'button.button_button__33qZ0' # для кнопки Зарегистрироваться
    ERROR_MESSAGE_PASSWORD = 'fieldset:nth-child(3) > div > p'  # для сообщения об ошибке пароля

class AuthorizationLocators:
    EMAIL_FIELD = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input' # для поля Имя (авторизация)
    PASSWORD_FIELD = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input' # для поля Пароль (авторизация)
    ENTER_BUTTON = '//*[@id="root"]/div/main/div/form/button' # для кнопки "Войти"
    LOGIN_BUTTON = '//*[@id="root"]/div/main/section[2]/div/button'  # Кнопка "Войти в аккаунт"
    PERSONAL_ACCOUNT_BUTTON = '//*[@id="root"]/div/header/nav/a/p'  # Кнопка "Личный кабинет"
    REGISTER_BUTTON = '//*[@id="root"]/div/main/div/div/p/a'  # Кнопка "Зарегистрироваться"
    RECOVERY_BUTTON = '//*[@id="root"]/div/main/div/div/p/a'  # Кнопка "Восстановить пароль"
    LOGOUT_BUTTON = '//*[@id="root"]/div/main/div/nav/ul/li[3]/button' #Кнопка "Выход"

class NavigationLocators:
    CONSTRUCTOR_BUTTON = '//*[@id="root"]/div/header/nav/ul/li[1]/a' # Локатор для кнопки "Конструктор"
    LOGO = '//*[@id="root"]/div/header/nav/div' # Локатор для логотипа Stellar Burgers
    BULKI_BUTTON = '//*[@id="root"]/div/main/section[1]/div[1]/div[1]' #Локатор для кнопки "Булки"
    SAUSES_BUTTON = '//*[@id="root"]/div/main/section[1]/div[1]/div[2]' #Локатор для кнопки "Соусы"
    FILLINGS_BUTTON = '//*[@id="root"]/div/main/section[1]/div[1]/div[3]' #Локатор для кнопки "Начинки"