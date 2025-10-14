import allure
from screens.base_screen import BaseScreen


class AuthorizationScreen(BaseScreen):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.title = ("xpath", "//*[text()='Авторизация']")
        self.auth_type_btn = ('txt', "По логину и паролю")
        self.phone_number_field = ('label', "Номер телефона")
        self.password_field = ('label', "Пароль")
        self.remember_me_checkbox = ('role', ['checkbox', "Запомнить меня"])
        self.login_btn = ('role', ['button', "Войти"])


    def is_authorization_page_open(self):
        self.wait_element(self.title)
        if self.is_element_visible(self.title):
            return True
        else:
            return False

    def select_auth_type(self):
        self.click(self.auth_type_btn)

    def enter_phone_number(self, phone_number):
        self.fill(self.phone_number_field, phone_number)

    def enter_password(self, password):
        self.fill(self.password_field, password)

    def check_remember_me_checkbox(self):
        self.check(self.remember_me_checkbox)

    def click_on_login_btn(self):
        self.click(self.login_btn)