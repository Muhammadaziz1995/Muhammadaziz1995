import pytest, allure


class TestIncome:
    def test_income_product(self, authorize_user, home_screen, catalogue_screen, income_screen, get_failure_screenshot):
        product_name = 'auto-test'
        amount = '100'
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
            income_screen.select_product_from_drop_down(product_name)
        with allure.step("Get all product amount from table"):
            prod_amount = income_screen.get_product_all_amount(3)
            print("First amount before add new products ------>", prod_amount)
        with allure.step("Get o'lchov birlik from table"):
            olchov_birlik = income_screen.get_olchov_birlik_from_all_remaining_screen()
            prod_price = income_screen.get_product_all_amount(7)
        with allure.step("Click on 'Приход' sub menu"):
            income_screen.click_on_prixod_sub_menu()
        with allure.step("Check 'Приход' screen is open"):
            income_screen.is_prixod_screen_open()
        with allure.step("Click on 'Оприходовать' button"):
            income_screen.click_on_prixodovat_btn()
        with allure.step("Selecting 'Test_mx' branch from drop-down menu"):
            income_screen.select_branch('Test_mx')
        with allure.step("Click on 'Добавить товар' button"):
            income_screen.click_on_add_product_btn()
        with allure.step("Check 'Добавить товар' side dialog open"):
            income_screen.is_add_product_dialog_open()
        with allure.step("Select(enter) product name"):
            income_screen.enter_product_name(product_name)
        with allure.step("Click on found product name"):
            income_screen.click_on_dialog_found_product()
        with allure.step("Click on 'Ед. изм-я' o'lchov birlik"):
            income_screen.click_on_dialog_olchov_birlik_dropdown(olchov_birlik)
        with allure.step("Enter amount of product"):
            income_screen.enter_dialog_amount(amount)
        with allure.step("Click on 'Добавить' button"):
            income_screen.click_on_dialog_add_product_btn()
        with allure.step("Get appeared product details 'Название продукции', 'Ед. изм-я', 'Количество' and compare with previous one"):
            income_screen.get_product_info_and_check_if_exists_in_table([product_name, olchov_birlik, amount]) #***
        with allure.step("Click on 'Оприходовать' button"):
            income_screen.click_on_dialog_oprixodovat_btn()
        with allure.step("Check if success message exists"):
            income_screen.is_first_success_message_exists()
        with allure.step("Click on 'Подтвердить' buttons"):
            income_screen.click_on_approve_btn()
        with allure.step("Check if finall success message exists"):
            income_screen.is_final_success_message_exists()
        with allure.step("Click on Obshiy ostatki sub menu 2nd time"):
            income_screen.click_on_all_remaining_balance()
        with allure.step("Check Obshiy ostatki screen is open 2nd time"):
            assert income_screen.is_all_remaining_balance_screen_open()
        with allure.step("Click on 'Все филиалы' drop-down menu"):
            income_screen.click_on_all_branches()
        with allure.step("Choose 'Test_mx' from the drop-down list"):
            catalogue_screen.select_branch_in_the_list()
        with allure.step("Click on all branches drop-down menu"):
            income_screen.click_on_all_branches()
        with allure.step("Selecting product from drop-down"):
            income_screen.select_product_from_drop_down2(product_name)
        with allure.step("Compare product name after changes appear"):
            assert income_screen.get_and_compare_product_name(product_name)
        with allure.step("Compare product amount before changes and after changes"):
            assert income_screen.get_and_compare_product_amounts(prod_amount, amount)
        # check olchov type sht - ('xpath', "//tbody/tr/td[4]")
        # check product price - ('xpath', "//tbody/tr/td[7]")
        # """