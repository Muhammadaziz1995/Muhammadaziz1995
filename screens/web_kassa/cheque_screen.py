from screens.base_screen import BaseScreen
from playwright.sync_api import expect
from datetime import datetime



class ChequeScreen(BaseScreen):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.company_name = ('xpath', "//*[text()='Печать кассового чека']/parent::div/following-sibling::div//*[contains(text(), 'SPECIAL TEXNO SOFT')]")
        self.branch_name = ('xpath', "//*[text()='Печать кассового чека']/parent::div/following-sibling::div//*[contains(text(), 'Test_mx')]")
        self.address = ('xpath', "//*[text()='123, 123, 123']")
        self.inn_label = ('xpath', "//*[text()='ИНН']")
        self.inn_value = ('xpath', "//*[text()='306351564']")
        self.smena = ('xpath', "//*[text()='Смена']")
        self.cheque = ('xpath', "//*[text()='№ Чека']")
        self.date_time_label = ('xpath', "//*[text()='Дата и время']")
        self.date_time_value = ('xpath', "//*[text()='Дата и время']/following-sibling::span") # needs to be calculated
        self.cheque_type = ('xpath', "//*[text()='Тип чека']")
        self.cheque_type_value = ('xpath', "//span[text()='Тип чека']/following-sibling::strong[text()='Продажа']")
        self.selected_product_name = ('xpath', "//*[text()=' auto-test']")
        self.product_quantity = ('xpath', "//span[text()='1' and text()='шт' and text()=' х' and text()='1 000.00']")
        self.prod = ('txt', "1 шт х 1 000.00")
        self.shtrix_code_label = ('xpath', "//*[text()='Штрих код']")
        self.shtrix_code_value = ('xpath', "//*[text()='1995777']")
        self.mxik_label = ('xpath', "//*[text()='ИКПУ']")
        self.mxik_value = ('xpath', "//*[text()='02202004002000000']")
        self.nds_label = ('xpath', "//*[text()='в т.ч. НДС' and text()='12']")
        self.nds_value = ('xpath', "//span[text()='в т.ч. НДС']/following-sibling::strong[text()='107.14']")
        self.inn_committe = ('xpath', "//*[text()='ИНН Комитента']")
        self.inn_committe_value = ('xpath', "//*[text()='02345678912345']")
        self.uid_label = ('xpath', "//*[text()='UID:']")
        self.uid_value = ('xpath', "//*[text()='UID:']/following-sibling::strong") # needs to be scroll and find
        self.x_icon_in_cheque = ('xpath', "//*[text()='Печать кассового чека']/following-sibling::div/button")


        self.cheque_details = [ self.company_name, self.branch_name, self.address, self.inn_label, self.inn_value,
                           self.smena, self.cheque, self.date_time_label, self.cheque_type,
                           self.cheque_type_value, self.selected_product_name, self.product_quantity, self.prod,
                           self.shtrix_code_label, self.shtrix_code_value, self.mxik_label, self.mxik_value,
                           self.nds_label, self.nds_value, self.inn_committe, self.inn_committe_value, self.uid_label
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
