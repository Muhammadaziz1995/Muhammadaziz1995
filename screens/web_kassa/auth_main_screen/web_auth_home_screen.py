from screens.base_screen import BaseScreen
from screens.web_kassa.cheque_screen import ChequeScreen
from playwright.sync_api import expect
from datetime import datetime



class WebAuthHomeScreen(BaseScreen):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        """ ****************    Authorization    **************** """
        self.web_kassa_auth_screen_title = ('xpath', '//h1')
        self.web_kassa_phone_number_input_field = ('xpath', '//input[@placeholder="+998 __ ___ __ __"]')
        self.password_input_field = ('xpath', "//*[@placeholder='Введите пароль']")
        self.web_kassa_submit_button = ('xpath', "//*[text()='Войти']")
        """ ****************    Authorization    **************** """

        """ ****************    Purchasing Products    **************** """
        self.product_title = ('xpath', "//*[@title=\"{}\"]")
        self.go_to_payments_button = ('xpath', "//*[text()='К оплате']")
        self.active_cheque_title = ('xpath', "//*[text()='Активный чек']")
        self.product_in_active_cheques_section = ('xpath', "//main/div/div/div[2]//*[text()=\"{}\"]")
        self.cash_payment_type = ('xpath', "//*[contains(text(),'Наличные')]")
        self.payment_side_bar_title = ('xpath', "//*[text()='Оплата']")
        self.number_of_products_in_payment = ('xpath', "//*[text()='Кол-во позиций']/following-sibling::div")
        self.number_of_products_label_in_payment = ('xpath', "//*[text()='Кол-во позиций']")
        self.NDS = ('xpath', "//*[text()='НДС']/following-sibling::div")
        self.NDS_label = ('xpath', "//*[text()='НДС']")
        self.total_price = ('xpath', "//*[text()='Всего к оплате']/following-sibling::div")
        self.total_price_label = ('xpath', "//*[text()='Всего к оплате']")
        self.nalichniye_payment_dialog_title = ('xpath', "//*[text()='Наличные']")
        self.bez_sdachi_button = ('xpath', "//*[text()='Без сдачи']")
        self.pechat_kassogo_cheka_title = ('xpath', "//*[text()='Печать кассового чека']")
        self.product_cheque_has_created_msg = ('xpath', "//*[text()='Товарный чек создан']")
        """ ****************    Purchasing Products    **************** """


        #############################################################################################################
        self.company_name = ('xpath',
                             "//*[text()='Печать кассового чека']/parent::div/following-sibling::div//*[contains(text(), 'SPECIAL TEXNO SOFT')]")
        self.branch_name = ('xpath',
                            "//*[text()='Печать кассового чека']/parent::div/following-sibling::div//*[contains(text(), 'Test_mx')]")
        self.address = ('xpath', "//*[text()='123, 123, 123']")
        self.inn_label = ('xpath', "//*[text()='ИНН']")
        self.inn_value = ('xpath', "//*[text()='306351564']")
        self.smena = ('xpath', "//*[text()='Смена']")
        self.cheque = ('xpath', "//*[text()='№ Чека']")
        self.date_time_label = ('xpath', "//*[text()='Дата и время']")
        self.date_time_value = ('xpath', "//*[text()='Дата и время']/following-sibling::span")  # needs to be calculated
        self.cheque_type = ('xpath', "//*[text()='Тип чека']")
        self.cheque_type_value = ('xpath', "//span[text()='Тип чека']/following-sibling::strong[text()='Продажа']")
        self.selected_product_name = ('xpath', "//*[text()=' auto-test']")
        self.product_quantity = ('xpath', "//span[text()='1' and text()='шт' and text()=' х' and text()='100.00']")
        self.prod = ('txt', "1 шт х 100.00")
        self.shtrix_code_label = ('xpath', "//*[text()='Штрих код']")
        self.shtrix_code_value = ('xpath', "//*[text()='7777777']")
        self.mxik_label = ('xpath', "//*[text()='ИКПУ']")
        self.mxik_value = ('xpath', "//*[text()='02202004002000000']")
        # self.nds_label = ('xpath', "//*[text()='в т.ч. НДС' and text()='12']")
        # self.nds_value = ('xpath', "//span[text()='в т.ч. НДС']/following-sibling::strong[text()='107.14']")
        self.inn_committe = ('xpath', "//*[text()='ИНН Комитента']")
        self.inn_committe_value = ('xpath', "//*[text()='123123123']")
        self.uid_label = ('xpath', "//*[text()='UID:']")
        self.uid_value = ('xpath', "//*[text()='UID:']/following-sibling::strong")  # needs to be scroll and find
        self.x_icon_in_cheque = ('xpath', "//*[text()='Печать кассового чека']/following-sibling::div/button")

        self.cheque_details = [self.company_name, self.branch_name, self.address, self.inn_label, self.inn_value,
                               self.smena, self.cheque, self.date_time_label, self.cheque_type,
                               self.cheque_type_value, self.selected_product_name, self.product_quantity, self.prod,
                               self.shtrix_code_label, self.shtrix_code_value, self.mxik_label, self.mxik_value, self.inn_committe, self.inn_committe_value,
                               self.uid_label
                               ]

    def check_cheque_details_for_purchasing(self):
        all_items = len(self.cheque_details)
        count_items_checked = 0
        date = datetime.today()
        today = date.strftime("%d-%m-%Y %H")
        if today == self.date_time_value:
            count_items_checked += 1

        for detail in self.cheque_details:
            self.infinite_scroll_to_element(detail, 30)
            print("Cheque detail: ---------->>> ", self.get_element_text(detail))
            if self.is_element_visible(detail):
                count_items_checked += 1
            else:
                continue

        if count_items_checked == all_items + 1:
            return True
        return False

    def click_on_x_icon_in_cheque(self):
        self.click(self.x_icon_in_cheque)
        #############################################################################################################

    """ ****************    Authorization    **************** """
    def check_web_kassa_title_has_expected_text(self):
        expect(self.get_element(self.web_kassa_auth_screen_title)).to_have_text("Авторизация")

    def enter_web_kassa_phone(self, number):
        self.fill(self.web_kassa_phone_number_input_field, number)

    def enter_password_web_kassa(self, password):
        self.fill(self.password_input_field, password)

    def click_on_submit_button_web_kassa(self):
        self.click(self.web_kassa_submit_button)
    """ ****************    Authorization    **************** """

    """ ****************    Purchasing Products     **************** """
    def click_on_product_by_title(self, title_of_product):
        self.click((self.product_title[0], self.product_title[1].format(title_of_product)))

    def click_on_bez_sdachi_button(self):
        self.click(self.bez_sdachi_button)

    def is_nalichniye_payment_screen_title_exists(self):
        try:
            print("Наличные : ------->", self.get_element_text(self.nalichniye_payment_dialog_title))
            if "Наличные" in self.get_element_text(self.nalichniye_payment_dialog_title):
                return True
        except Exception as e:
            print(e)
        return False

    def is_kassa_cheque_modal_title_exists(self):
        expect(self.get_element(self.pechat_kassogo_cheka_title)).to_be_visible()

    def is_product_cheque_has_been_created_msg_appear(self):
        expect(self.get_element(self.product_cheque_has_created_msg)).to_be_visible()

    def click_on_go_to_payments_button(self):
        self.click(self.go_to_payments_button)

    def active_cheque_side_bar_title_exists(self):
        self.is_element_visible(self.active_cheque_title)

    def click_on_cash_payment_type(self):
        self.click(self.cash_payment_type)

    def is_selected_product_title_appears_in_active_cheque_side_bar(self, product_title):
        self.is_element_visible((self.product_in_active_cheques_section[0], self.product_in_active_cheques_section[1].format(product_title)))

    def is_payment_side_bar_title_exists(self):
        self.is_element_visible(self.payment_side_bar_title)

    def get_number_of_products_in_payment(self):
        selected_products = self.get_element_text(self.number_of_products_in_payment)
        return int(selected_products)

    def get_NDS_amount(self):
        NDS_amount = self.get_element_text(self.NDS)
        return float(NDS_amount)

    def get_total_price(self):
        total_price = self.get_element_text(self.total_price)
        return int(float(total_price))


    def compare_selected_number_of_product(self, number_of_product):
        try:
            assert self.is_element_visible(self.number_of_products_label_in_payment)
            selected_products = self.get_element_text(self.number_of_products_in_payment)
            if number_of_product == int(selected_products):
                return True
            else:
                return False
        except Exception as e:
            raise e
    """ ****************    Purchasing Products     **************** """