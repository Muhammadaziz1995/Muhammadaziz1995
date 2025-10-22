import time

import pytest
import allure
from unicodedata import category
from screens.web_kassa.auth_main_screen.web_auth_home_screen import WebAuthHomeScreen


class TestCatalogue:
    def test_web_kassa(self, authorize_user, company_screen, home_screen, income_screen, web_auth_home_screen, catalogue_screen, cheque_screen):
        with allure.step("Click on Warehouse from Home screen"):
            home_screen.click_on_warehouse_drop_down_navbar()
        with allure.step("Click on Obshiy ostatki sub menu"):
            income_screen.click_on_all_remaining_balance()
        with allure.step("Check Obshiy ostatki screen is open"):
            assert income_screen.is_all_remaining_balance_screen_open()
        with allure.step("Click on 'Все филиалы' drop-down menu"):
            income_screen.click_on_all_branches()
        with allure.step("Choose 'Test_mx' from the drop-down list"):
            catalogue_screen.select_branch_in_the_list()
        with allure.step("Close branches drop-down menu"):
            income_screen.click_on_all_branches()
        with allure.step("Selecting product in products drop-down menu"):
            income_screen.select_product_from_drop_down("auto-test")
        with allure.step("Get all product amount from table"):
            prod_amount = income_screen.get_product_all_amount(3)
        with allure.step("Navigate to kassa-dev.smartpos.uz"):
            web_auth_home_screen = income_screen.open_new_tab("https://kassa-dev.smartpos.uz")
            web_auth_home_screen = WebAuthHomeScreen(web_auth_home_screen)
            assert web_auth_home_screen.check_new_tab_by_title("Web-Kassa")
            web_auth_home_screen.switch_to_tab_by_index(1)
        with allure.step("Authorize cashier"):
            web_auth_home_screen.check_web_kassa_title_has_expected_text()
        with allure.step("Enter cashier phone number"):
            web_auth_home_screen.enter_web_kassa_phone("905439771")
        with allure.step("Enter cashier password"):
            web_auth_home_screen.enter_password_web_kassa("832145")
        with allure.step("Click on 'Submit' button"):
            web_auth_home_screen.click_on_submit_button_web_kassa()
        with allure.step("Selecting 'auto-test' from products list"):
            web_auth_home_screen.click_on_product_by_title("auto-test")
        with allure.step("Checking active cheque bar title exists or not"):
            web_auth_home_screen.active_cheque_side_bar_title_exists()
        with allure.step("Checking selected product title appears in active cheque side bar"):
            web_auth_home_screen.is_selected_product_title_appears_in_active_cheque_side_bar("auto-test")
        with allure.step("Click on 'К оплате' button"):
            web_auth_home_screen.click_on_go_to_payments_button()
        with allure.step("Checking 'Оплата' side bar title exists"):
            web_auth_home_screen.is_payment_side_bar_title_exists()
        with allure.step("Comparing selected product numbers are correct in 'Оплата' side bar"):
            web_auth_home_screen.compare_selected_number_of_product(1)
        with allure.step("Click on 'Cash' payment type"):
            web_auth_home_screen.click_on_cash_payment_type()
        with allure.step("'Наличные' side bar exists"):
            web_auth_home_screen.is_nalichniye_payment_screen_title_exists()
        with allure.step("Click on 'bez sdachi' button"):
            web_auth_home_screen.click_on_bez_sdachi_button()
        with allure.step("Checking 'Печать кассового чека' cheque side bar exists"):
            web_auth_home_screen.is_kassa_cheque_modal_title_exists()
            web_auth_home_screen.is_product_cheque_has_been_created_msg_appear()
        with allure.step("Checking cheque details"):
            web_auth_home_screen.check_cheque_details_for_purchasing()
            # cheque_screen.check_cheque_details_for_purchasing()
        # with allure.step(""):
        # with allure.step(""):
        # with allure.step(""):
        # with allure.step(""):