from screens.base_screen import BaseScreen
from time import sleep
from playwright.sync_api import expect



class CompanyScreen(BaseScreen):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.company_info_option = ('txt', "Данные компании")
        self.company_title = ('xpath', '//img/parent::div/following-sibling::div/h3')
        self.director_name = ('xpath', "//h3[text()='Директор компании']/following-sibling::div[2]")
        self.edit_btn = ('txt', 'Редактировать')
        self.edit_screen_title = ('txt', 'Карточка компании')
        self.surname = ('label', "Фамилия")
        self.name = ('label', "Имя")
        self.p_name = ('label', "Отчество")
        self.save_btn = ('role', ['button', "Сохранить"])
        self.yur_litso_checkbox = ('role', ['checkbox', "Проверка принадлежности маркировок юридическому лицу"])
        self.comp_region = ('label', "Регион")
        self.comp_ditrict = ('label', "Район")
        self.comp_address = ('label', "Адрес")
        self.success_msg = ('txt', "Успешно")

    def check_company_title_exists(self, company_title_name):
        self.is_element_visible(self.company_title)
        self.check_expected_txt_exists(company_title_name, self.company_title)

    def check_edit_screen_title_exists(self):
        self.is_element_visible(self.edit_screen_title)
        edit_scr_title = self.get_element_text(self.edit_screen_title)
        assert edit_scr_title == "Карточка компании"

    def check_success_message_appears(self):
        if self.is_element_visible(self.success_msg):
            return True
        return False

    def click_comp_info_opt(self):
        self.click(self.company_info_option)

    def click_edit_btn(self):
        self.click(self.edit_btn)

    def click_save_btn(self):
        self.click(self.save_btn)

    def get_director_name(self):
        dir_name = self.get_element_text(self.director_name)
        return dir_name

    def edit_existing_FIO(self, fio): # fio is LIST for Surname & Name & FatherName
        locs = [self.surname, self.name, self.p_name]
        for loc in locs:
            self.click(loc)
            self.fill(loc, fio[0])
            sleep(2)

    def selecting_first_checkbox_under_additional_options(self):
        self.check(self.yur_litso_checkbox)