import time

import pytest
import allure
from unicodedata import category


class TestCatalogue:
    def test_catalogue_add_new_product(self, authorize_user, home_screen, catalogue_screen, get_failure_screenshot):
        with allure.step("Click on 'Каталог' from navigation bar"):
            home_screen.click_on_catalogue_drop_down_navbar()
        with allure.step("Click on 'Все филиалы' drop-down menu"):
            catalogue_screen.click_on_all_branches_drop_down()
        with allure.step("Choose 'Test_mx' from the drop-down list"):
            catalogue_screen.select_branch_in_the_list()
        with allure.step("Check 'Bez alkogolniy PIVO' exists"):
            catalogue_screen.is_all_alcohol_beer_category_exists()
        with allure.step("Click on all product menu using three dot icon"):
            catalogue_screen.click_on_three_dot_icon_to_open_all_product_menu()
        with allure.step("Click on 'Добавить товар'"):
            catalogue_screen.click_on_add_product()
        with allure.step("Check add product form title 'Добавить товар в категорию' exists"):
            assert catalogue_screen.is_add_product_form_title_exists()
        with allure.step("Enter MXIK '02202004002000000' code"):
            catalogue_screen.enter_mxik_code_to_get_product('02202004002000000')
        with allure.step("Click on search button to autofill product by MXIK code"):
            catalogue_screen.click_on_search_button_to_get_autofill_data()
        with allure.step("Enter product name to 'Название продукции'"):
            AUTO_GENERATED_PRODUCT = catalogue_screen.enter_product_name(6)
            print("AUTO GENERATED PRODUCT: --------> ", AUTO_GENERATED_PRODUCT)
        with allure.step("Enter 'Штрихкод' (random)"):
            catalogue_screen.enter_shtrix_code('1995777')
        with allure.step("Selecting 'шт' from dropdown-list"):
            catalogue_screen.click_on_tovar_olchovi()
            catalogue_screen.select_shtuk_option_from_drop_down('шт')
            catalogue_screen.is_selected_shtuk_option_exists()
        with allure.step("Click on 'Ед. изм-я (Tasnif) *' input field"):
            catalogue_screen.click_on_olchov_birlik_dimension()
        with allure.step("Enter products's sales price"):
            catalogue_screen.scroll_to_bottom()
            catalogue_screen.enter_sales_price('4')
        with allure.step("Selecting NDS from list"):
            catalogue_screen.select_nds_from_list('with') # can be past param from ['with', 'without', 'no nds']
        with allure.step("Selecting 'Происхождение товара *' from list"):
            catalogue_screen.select_product_origin('k') # can be past param from ['k'-> kupleno, 'p'-> prozivoditel, 'u'-> usluga, 'nu'-> ne uchastvuyu]
        with allure.step("Click on 'Добавить' button"):
            catalogue_screen.click_on_add_product_btn()
        with allure.step("Checking new product in the PRODUCTS table on Catalogue screen"):
            catalogue_screen.is_new_added_prod_appears_in_products_table(AUTO_GENERATED_PRODUCT)
        with allure.step("Checking new product by searching on Catalogue screen"):
            catalogue_screen.search_new_added_prod(AUTO_GENERATED_PRODUCT)

    def test_catalogue_delete_last_added_product(self, authorize_user, home_screen, catalogue_screen, get_failure_screenshot):
        with allure.step("Click on 'Каталог' from navigation bar"):
            home_screen.click_on_catalogue_drop_down_navbar()
        with allure.step("Click on 'Все филиалы' drop-down menu"):
            catalogue_screen.click_on_all_branches_drop_down()
        with allure.step("Choose 'Test_mx' from the drop-down list"):
            catalogue_screen.select_branch_in_the_list()
        with allure.step("Getting last product name in the table"):
            last_prod_name = catalogue_screen.get_last_added_prod_name()
        with allure.step("Getting last product name in the table"):
            catalogue_screen.click_on_three_dot_icon()
        with allure.step("Deleting the LAST product from table"):
            catalogue_screen.delete_product_from_table()
            catalogue_screen.is_warning_message_exists()
            catalogue_screen.click_on_OK_btn_in_popup()
        with allure.step("Check message of DELETED product appear"):
            catalogue_screen.is_deleted_product_success_message()
        with allure.step("Check deleted product not exists in table"):
            assert catalogue_screen.check_deleted_product_not_exists(last_prod_name)
    #
    def test_add_new_category(self,authorize_user, home_screen,catalogue_screen, get_failure_screenshot):
        with allure.step("Click on 'Каталог' from navigation bar"):
            home_screen.click_on_catalogue_drop_down_navbar()
        with allure.step("Click on 'Все филиалы' drop-down menu"):
            catalogue_screen.click_on_all_branches_drop_down()
        with allure.step("Choose 'Test_mx' from the drop-down list"):
            catalogue_screen.select_branch_in_the_list()
        with allure.step("Click on Add category plus '+' icon"):
            catalogue_screen.click_on_add_category_plus_button()
        with allure.step("Check 'Добавить категорию' screen open"):
            catalogue_screen.is_add_category_dialog_title_exists()
        with allure.step("Enter new category name"):
            category_name = catalogue_screen.new_random_category_name()
            catalogue_screen.enter_new_category_name(category_name)
        with allure.step("Click on 'Добавить' button"):
            catalogue_screen.click_on_add_product_btn_in_add_category()
        with allure.step("Check added category's success message appeared"):
            catalogue_screen.is_added_category_success_msg_appeared()

    def test_delete_category_from_category_list(self, authorize_user, home_screen, catalogue_screen, get_failure_screenshot):
        with allure.step("Click on 'Каталог' from navigation bar"):
            home_screen.click_on_catalogue_drop_down_navbar()
        with allure.step("Click on 'Все филиалы' drop-down menu"):
            catalogue_screen.click_on_all_branches_drop_down()
        with allure.step("Choose 'Test_mx' from the drop-down list"):
            catalogue_screen.select_branch_in_the_list()
        with allure.step("Find category from list"):
            deleted_category_name = catalogue_screen.search_category_for_delete()
            print("Deleted category name: ------> ", deleted_category_name)
        with allure.step("Delete found category from list by clicking 'Удалить категорию'"):
            catalogue_screen.delete_category()
        with allure.step("Check approval question apppears before finishing delete category"):
            catalogue_screen.is_approval_question_before_delete_category_exists(deleted_category_name)
        with allure.step("Click on 'Да' button"):
            catalogue_screen.click_on_yes_btn()
        with allure.step("Check category deleted msg 'Категория удалена' appeared"):
            catalogue_screen.is_category_has_deleted_msg_appeared()