from screens.base_screen import BaseScreen
from playwright.sync_api import expect
from time import sleep



class IncomeScreen(BaseScreen):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.all_remaining_balance = ('xpath', "//a/span[text()='Общие остатки']")
        self.all_branches = ('xpath', ".ant-select-selection-overflow")
        self.prixod_screen_title = ('xpath', "//header/following-sibling::main//*[text()='Приход']")
        self.all_remaining_balance_screen_title = ('txt', 'Общие остатки')
        self.select_product_drop_down_field = ('xpath', "xpath=//*[@id='rc_select_2']")
        self.select_product_drop_down_field2 = ('xpath', "xpath=//*[@id='rc_select_1']")
        self.found_product_in_search = ('tit', 'auto-test')
        self.product_info_container = ('xpath', "//tbody/tr/td[{}]")
        self.prixod_sub_menu_navbar = ('role', ['link', 'Приход'])
        self.prixodovat_btn = ('xpath', "//a[text()='Оприходовать']")
        self.prixod_select_branch_dropdown_field = ('xpath', "//input[@id='basic_toBranchId']")
        self.found_branch = ('xpath', 'xpath=//div[@title="Test_mx"]/div')
        self.prixod_add_product_btn = ('role', ['button', 'Добавить товар'])
        self.dialog_title = ('role2', ['dialog', 'txt', 'Добавить товар'])
        # self.dialog_product_name_field = ('xpath', "//input[@id='basic_productId']")
        self.dialog_product_name_field = ('role', ['combobox','Продукт'])
        self.dialog_olchov_birlik = ('role', ['combobox', 'Ед. изм-я'])
        # self.doalog_amount_field = ('xpath', "//*[@placeholder='Количество']")
        self.doalog_amount_field = ('role', ['spinbutton', 'Количество'])
        self.dialog_add_product_btn = ('role', ['button', 'Добавить'])
        self.dialog_oprixodovat_btn = ('role', ['button', 'Оприходовать'])
        self.prixod_success_msg = ('txt', 'оприходован')
        self.prixod_approve_btn = ('role', ['button', 'Подтвердить'])
        self.prixod_final_success_msg = ('txt', 'Приход успешно подтвержден')
        self.all_remaining_table_prod_name = ("xpath", "xpath=//tbody/tr/td[2]/a")



    def is_prixod_screen_open(self):
        expect.set_options(timeout=10000)
        expect(self.get_element(self.prixod_screen_title)).to_be_visible()

    def is_add_product_dialog_open(self):
        expect(self.get_element(self.dialog_title)).to_be_visible()

    def is_first_success_message_exists(self):
        expect(self.get_element(self.prixod_success_msg)).to_be_visible()

    def is_final_success_message_exists(self):
        expect(self.get_element(self.prixod_final_success_msg)).to_be_visible()
        self.re_fresh_screen()

    def click_on_all_remaining_balance(self):
        self.click(self.all_remaining_balance)

    def click_on_prixod_sub_menu(self):
        self.click(self.prixod_sub_menu_navbar)

    def click_on_prixodovat_btn(self):
        self.click(self.prixodovat_btn)

    def click_on_add_product_btn(self):
        self.click(self.prixod_add_product_btn)

    def click_on_dialog_found_product(self):
        self.click(('txt', "auto-test"))

    def click_on_dialog_add_product_btn(self):
        self.click(self.dialog_add_product_btn)

    def click_on_dialog_oprixodovat_btn(self):
        self.click(self.dialog_oprixodovat_btn)

    def click_on_approve_btn(self):
        self.click(self.prixod_approve_btn)

    def click_on_dialog_olchov_birlik_dropdown(self, olchov_birlik):
        self.click(self.dialog_olchov_birlik)
        self.click(('txt', '{}'.format(olchov_birlik)))

    def click_on_all_branches(self):
        self.click(self.all_branches)

    def is_all_remaining_balance_screen_open(self):
        # expect(self.get_element(self.all_remaining_balance_screen_title).nth(1)).to_be_visible()
        return self.get_element(self.all_remaining_balance_screen_title).nth(1).is_visible()

    def select_product_from_drop_down(self, product_name):
        self.clear_field(self.select_product_drop_down_field)
        self.get_element(self.select_product_drop_down_field).click(timeout=10000)
        self.fill(self.select_product_drop_down_field, product_name)
        self.click(self.found_product_in_search)


    def select_product_from_drop_down2(self, product_name):
        self.get_element(self.select_product_drop_down_field2).click(timeout=10000)
        self.fill(self.select_product_drop_down_field2, product_name)
        self.click(self.found_product_in_search)

    def get_product_all_amount(self, index):
        amount = self.get_element_text((self.product_info_container[0], self.product_info_container[1].format(index))).split(' ')
        res = ''
        for i in range(len(amount)):
            res += amount[i]
        print("Amount in wharehouse : ->>>>>>>>>>>>>>>>> ", res)
        return int(float(res))

    def get_olchov_birlik_from_all_remaining_screen(self):
        ol_birlik = self.get_element_text((self.product_info_container[0], self.product_info_container[1].format(4)))
        return ol_birlik

    def get_product_info_and_check_if_exists_in_table(self, list):
        new_list = list
        counter = 0
        for i in range(len(new_list)):
            if self.get_element_text((self.product_info_container[0], self.product_info_container[1].format(i+1))) in new_list:
                counter += 1
            else:
                continue

        if counter == len(new_list):
            return True
        return False


    def select_branch(self, branch_name):
        self.click(self.prixod_select_branch_dropdown_field)
        self.fill(self.prixod_select_branch_dropdown_field, branch_name)
        self.click(self.found_branch)

    def enter_product_name(self, product_name):
        self.fill(self.dialog_product_name_field, product_name)

    def enter_dialog_amount(self, amount):
        self.fill(self.doalog_amount_field, amount)

    def get_and_compare_product_name(self, prod_name):
        prod_name_in_table = self.get_element_text(self.all_remaining_table_prod_name)
        if prod_name in prod_name_in_table:
            return True
        return False

    def get_and_compare_product_amounts(self, old_prod_amount, difference):
        prod_amount = self.get_element_text((self.product_info_container[0], self.product_info_container[1].format(3)))
        prod_amount = prod_amount.split(' ')
        new_prod_amount = ''
        for i in range(len(prod_amount)):
            new_prod_amount += prod_amount[i]

        print("Second updated amount of product ------> ", int(float(new_prod_amount)))
        if int(float(new_prod_amount)) > old_prod_amount:
            if int(float(new_prod_amount)) - old_prod_amount == int(difference):
                return True
        return False
