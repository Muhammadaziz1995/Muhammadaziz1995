import time

from screens.base_screen import BaseScreen
from playwright.sync_api import expect
from time import sleep



class CatalogueScreen(BaseScreen):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.catalogue_screen_title = ('xpath', "//*[@placeholder='Поиск по категориям']")
        self.all_branches = ('xpath', "//*[text()='Все филиалы']")
        self.new_product_name_container_in_table = ('xpath', "xpath=//tbody/tr[last()]/td[2]")
        self.three_dot_icon_in_product_raw = ('xpath', "xpath=//tbody/tr[last()]/td[last()]/button")
        self.top_search_field = ('xpath', "//*[@placeholder='Поиск по товарам']")
        self.first_search_result_container_in_table = ('xpath', "//tbody/tr/td[2]")
        self.selected_branch = ('xpath', "//span[@title='Test_mx']")
        self.branch_in_the_list = ('txt', "Test_mx")
        self.all_alcohol_beer_category = ('txt', "Bez alkologolniy PIVO")
        self.all_product_menu_three_dot_icon = ('xpath', "//span[@title='Bez alkologolniy PIVO']//div/button")
        self.add_product_option = ('txt', 'Добавить товар')
        self.add_product_form_title = ('xpath', "//div[contains(text(), 'Добавить товар')]")
        self.enter_code_input_field = ('xpath', "//*[@placeholder='Введите код']")
        self.search_icon_to_autofill_product_data = ('xpath', "//form/div[2]/div[2]/button")
        self.product_name_input_field = ('xpath', "//input[@id='name']")
        self.shtrix_code_input_field = ('xpath', "//*[@id='barcode']")
        self.shtuk_option_in_drop_down = ('role', ["combobox", "Ед. изм-я (SMARTPOS TRADE) *"])
        self.shtuk_option = ('xpath', "//span[@title='шт']")
        self.result_list_shtuk_option = ('txt', "шт")
        self.tovar_olchovi = ('label', "Ед. изм-я (SMARTPOS TRADE)")
        # self.select_olchov_birlik = ('xpath', "//*[@id='defaultPackage']")
        self.select_olchov_birlik = ('role', ['combobox', "Ед. изм-я (Tasnif) *"])
        self.suggested_olchov_birlik = ('txt', "литр -- 1378893")
        self.sales_price_input_field = ('xpath', "//input[@id='salesPrice']")
        self.select_NDS_input_field = ('role', ['combobox', 'НДС *'])
        self.add_product_btn = ('xpath', '//*[text()="Добавить"]')
        self.product_origin = ('role', ['combobox', 'Происхождение товара *'])
        self.selected_products_group = ('xpath', "//*[text()='Избранный']")
        self.success_message = ('txt', "Товар добавлен")
        self.success_deleted_product = ('txt', "Товар удален")
        self.delete_product_from_table_btn = ('role', ['button', 'Удалить'])
        self.warning_msg_while_delete_prod = ('txt', 'Вы точно хотите удалить товар?')
        self.delete_option_in_popup = ('txt', 'OK')
        self.add_category_plus_icon = ('xpath', "//main//div[contains(@class, 'categoriesSearchRow')]/div[2]/button[1]")
        self.add_category_title_locator1 = ('role', 'dialog')     #getByRole('dialog').getByText('Добавить категорию')
        self.add_category_title_locator2 = ('txt', 'Добавить категорию')
        self.add_category_input_field = ('role', ['textbox', 'Название *'])
        self.category_added_success_msg = ('txt', 'Категория добавлена')
        self.category_group_items_container = ('xpath', "//*[@class='ant-tree-list-holder-inner']/div")
        self.category_single_item_container = ('xpath', "//*[@class='ant-tree-list-holder-inner']/div[{}]/span[3]/span/div/div[1]")
        self.category_single_item_button_container = ('xpath', "//*[@class='ant-tree-list-holder-inner']/div[{}]/span[3]/span/div/div[3]/button")
        self.delete_category_option = ('role', ['button', 'Удалить категорию'])
        # self.delete_category_option = ('xpath', "//div[@id='root']/following-sibling::div[5]//*[text()='Удалить категорию']")
        self.approval_question_before_delete_category = ('txt', "Вы точно хотите удалить категорию? \"{}\"?")
        self.yes_btn = ('xpath', "//*[text()='Да']")
        self.category_has_deleted_msg = ('xpath', "//*[text()='Категория удалена']")

    def is_add_category_dialog_title_exists(self):
        self.is_element_visible(self.page.get_by_role('dialog').get_by_text('Добавить категорию'))

    def is_added_category_success_msg_appeared(self):
        expect(self.get_element(self.category_added_success_msg)).to_be_visible()

    def is_category_has_deleted_msg_appeared(self):
        expect(self.get_element(self.category_has_deleted_msg)).to_be_visible()

    def is_catalogue_screen_open(self):
        expect.set_options(timeout=15000)
        expect(self.get_element(self.catalogue_screen_title)).to_be_visible()
        # self.is_element_visible()

    def is_new_added_prod_appears_in_products_table(self, new_prod_name):
        expect(self.get_element(self.new_product_name_container_in_table)).to_contain_text(new_prod_name)

    def is_approval_question_before_delete_category_exists(self, deleted_category_name):
        expect.set_options(timeout=15000)
        expect(self.get_element((self.approval_question_before_delete_category[0], self.approval_question_before_delete_category[1].format(deleted_category_name)))).to_be_visible()

    def is_all_alcohol_beer_category_exists(self):
        assert self.is_element_visible(self.all_alcohol_beer_category)

    def is_add_product_form_title_exists(self):
        self.check_expected_txt_exists("Добавить товар", self.add_product_form_title)
        return True

    def is_selected_shtuk_option_exists(self):
        expect.set_options(timeout=15000)
        expect(self.get_element(self.shtuk_option)).to_be_visible()
        return True

    def is_warning_message_exists(self):
        assert self.is_element_visible(self.warning_msg_while_delete_prod)

    def is_deleted_product_success_message(self):
        assert self.is_element_visible(self.success_deleted_product)

    def check_deleted_product_not_exists(self, product_name):
        if not self.is_element_visible(self.page.get_by_text(product_name)):
            return True
        return False

    def click_on_all_branches_drop_down(self):
        elem = self.get_element(self.all_branches)
        elem.click()

    def select_branch_in_the_list(self):
        self.infinite_scroll_to_element(self.branch_in_the_list)
        # assert self.is_element_visible(self.selected_branch) == True
        expect(self.get_element(self.selected_branch)).to_be_visible()

    def click_on_three_dot_icon_to_open_all_product_menu(self):
        self.click(self.all_product_menu_three_dot_icon)

    def click_on_add_product(self):
        self.click(self.add_product_option)


    def click_on_search_button_to_get_autofill_data(self):
        self.click(self.search_icon_to_autofill_product_data)

    def click_on_OK_btn_in_popup(self):
        self.click(self.delete_option_in_popup)

    def select_shtuk_option_from_drop_down(self, olchov_nomi):
        self.fill(self.shtuk_option_in_drop_down, olchov_nomi)
        elem = self.page.get_by_text(olchov_nomi, exact=True)
        elem.click()
        expect(self.get_element(self.shtuk_option)).to_be_visible()

    def click_on_olchov_birlik_dimension(self):
        self.click(self.select_olchov_birlik)
        self.click(self.suggested_olchov_birlik)

    def click_on_tovar_olchovi(self):
        self.click(self.tovar_olchovi)

    def click_on_yes_btn(self):
        self.click(self.yes_btn)

    def click_on_add_product_btn(self):
        self.click(self.add_product_btn)
        self.re_fresh_screen2('text="Товар добавлен"')

    def click_on_add_product_btn_in_add_category(self):
        self.click(self.add_product_btn)

    def click_on_three_dot_icon(self):
        self.click(self.three_dot_icon_in_product_raw)

    def click_on_add_category_plus_button(self):
        self.click(self.add_category_plus_icon)

    def delete_category(self):
        self.click(self.delete_category_option)

    def search_category_for_delete(self):
        all_categories = self.get_element(self.category_group_items_container).all()
        for i in range(len(all_categories)):
            if "Avto-test:" in self.get_element((self.category_single_item_container[0], self.category_single_item_container[1].format(i+1))).text_content():
                self.get_element((self.category_single_item_button_container[0], self.category_single_item_button_container[1].format(i+1))).click()
                return self.get_element((self.category_single_item_container[0], self.category_single_item_container[1].format(i+1))).text_content()
            else:
                continue
        return None

    def delete_product_from_table(self):
        self.click(self.delete_product_from_table_btn)

    def select_nds_from_list(self, nds):
        self.click(self.select_NDS_input_field)
        if nds == "with":
            res_nds = "НДС - 12%"
        elif nds == "without":
            res_nds = "НДС - 0%"
        else:
            res_nds = "Без НДС"

        self.click(('txt', res_nds))

    def select_product_origin(self, origin_type):
        """
        p => "Производитель"
        k => "Куплено"
        u => "Услуга"
        nu => "Не участвую"
        :param origin_type:
        :return:
        """
        if origin_type == "p":
            res_origin = "Производитель"
        elif origin_type == "k":
            res_origin = "Куплено"
        elif origin_type == "u":
            res_origin = "Услуга"
        else:
            res_origin = "Не участвую"

        self.click(self.product_origin)
        self.click(('txt', res_origin))


    def enter_mxik_code_to_get_product(self, mxik_code):
        self.fill(self.enter_code_input_field, mxik_code)

    def enter_product_name(self, length):
        res_name = self.generate_random_str(length) + " BEER"
        self.fill(self.product_name_input_field, res_name)
        return res_name

    def enter_shtrix_code(self, shtrix_code):
        self.click(self.shtrix_code_input_field)
        self.fill(self.shtrix_code_input_field, shtrix_code)

    def enter_sales_price(self, sales_price):
        self.fill(self.sales_price_input_field, sales_price)

    def enter_new_category_name(self, name_catalog):
        self.fill(self.add_category_input_field, name_catalog)

    def scroll_to_bottom(self):
        self.infinite_scroll_to_element(self.selected_products_group)

    def search_new_added_prod(self, new_prod_name):
        self.fill(self.top_search_field, new_prod_name)
        time.sleep(2)
        search_result = self.get_element_text(self.first_search_result_container_in_table)
        print("Search result: ------------> " + search_result)
        assert new_prod_name in search_result

    def get_last_added_prod_name(self):
        prod_name = self.get_element_text(self.new_product_name_container_in_table)
        return prod_name

    def new_random_category_name(self):
        return self.generate_random_str(6)