import allure
from screens.base_screen import BaseScreen


class HomeScreen(BaseScreen):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.title = ('xpath', "section div.custom-content__header__title-withTotal")
        self.company_drop_down_navbar = ('txt', "Компания")
        self.catalogue_drop_down_navbar = ('txt', "Каталог")
        self.warehouse_drop_down_navbar = ('xpath', "//*[text()='Склад']")

    def is_home_page_open(self):
        self.wait_element(self.title)
        if self.is_element_visible(self.title):
            return True
        else:
            return False

    def click_on_company_drop_down_navbar(self):
        self.click(self.company_drop_down_navbar)

    def click_on_catalogue_drop_down_navbar(self):
        self.click(self.catalogue_drop_down_navbar)

    def click_on_warehouse_drop_down_navbar(self):
        self.click(self.warehouse_drop_down_navbar)