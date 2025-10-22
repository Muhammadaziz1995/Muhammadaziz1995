import pytest
import allure
from screens.company_screens.company_screen import CompanyScreen


class TestCompanyInfo:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.company = CompanyScreen(page)

    def test_company_info(self, authorize_user, home_screen, company_screen, get_failure_screenshot): # test_* should be added
        with allure.step("Click Company drop-down in navbar"):
            home_screen.click_on_company_drop_down_navbar()
        with allure.step("Click Company-Info option"):
            company_screen.click_comp_info_opt()
        with allure.step("Check company_screens title exists"):
            company_screen.check_company_title_exists("SPECIAL TEXNO SOFT")
        director_name = company_screen.get_director_name()
        with allure.step("Click on Edit => Редактировать button"):
            company_screen.click_edit_btn()
        with allure.step("Check edit screen title exists"):
            company_screen.check_edit_screen_title_exists()
        with allure.step("Editing info of Director using random String - Фамилия/Имя/Отчество"):
            random_str = company_screen.generate_random_str(5)
            company_screen.edit_existing_FIO([random_str])
        # with allure.step("Opening new tab -> Web-KASSA"):
        #     company_screen = company_screen.open_new_tab("https://kassa-dev.smartpos.uz/")
        #     company_screen = CompanyScreen(company_screen)
        #     company_screen.switch_to_tab_by_index(1)
        #     company_screen.check_web_kassa_title_has_expected_text()
        #     company_screen.enter_web_kassa_phone()
        #     company_screen = company_screen.switch_to_tab_by_index(0)
        #     company_screen = CompanyScreen(company_screen)
        with allure.step("Select 'Проверка принадлежности маркировок юридическому лицу' checkbox"):
            company_screen.selecting_first_checkbox_under_additional_options()
        with allure.step("Click Save button"):
            company_screen.click_save_btn()
        with allure.step("Checking Success message appears or not after editing company_screens info"):
            assert company_screen.check_success_message_appears()
        with allure.step("Comparing Company Director's fullname with test Data"):
            edited_director_name = company_screen.get_director_name()
            assert director_name != edited_director_name