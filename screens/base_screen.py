from typing import List

from playwright.sync_api import Page, expect
from time import sleep
import allure, random, string


class BaseScreen:
    def __init__(self, page: Page):
        self.context = page.context
        self.page = page
        self.timeout = 20000

    def get_element(self, locator):
        method = locator[0]
        values = locator[1]
        return self.get_element_by_type(method, values)


    def get_element_by_type(self, method, value):
        if method == 'role':
            return self.page.get_by_role(value[0], name=value[1], exact=True)
        elif method == 'role2':
            if value[1] == 'txt':
                return self.page.get_by_role(value[0]).get_by_text(value[2])
            else:
                raise Exception('Invalid locator method.')
        elif method == 'id':
            return self.page.get_by_test_id(value)
        elif method == 'xpath':
            return self.page.locator(value)
        elif method == 'alt':
            return self.page.get_by_alt_text(value)
        elif method == 'pla':
            return self.page.get_by_placeholder(value)
        elif method == 'tit':
            return self.page.get_by_title(value)
        elif method == 'txt':
            return self.page.get_by_text(value)
        elif method == 'label':
            return self.page.get_by_label(value)
        else:
            raise Exception('Invalid locator method.')

    def navigate_to(self, url):
        self.page.goto(url)

    # """-----------------------------------------------------------------------------------------------------------------
    def wait_for_page_load(self, timeout):
        self.page.wait_for_load_state('networkidle', timeout=timeout)

    def get_current_url(self):
        return self.page.url

    def get_page_title(self):
        return self.page.title()

    def check_new_tab_by_title(self, new_tab_title):
        print(self.page.title())
        try:
            if new_tab_title in self.get_page_title():
                return True
        except Exception as e:
            print("No new tab found with given title!")
        return False

    def get_all_tabs(self) -> List[Page]:
        return self.context.pages

    def get_all_tab_count(self) -> int:
        return len(self.context.pages)

    def open_new_tab(self, url: str = None):
        new_page = self.context.new_page()
        if url:
            new_page.goto(url)
        return new_page

    def switch_to_tab_by_index(self, index: int) -> Page:
        tabs = self.get_all_tabs()
        if index < len(tabs):
            tab = tabs[index]
            tab.bring_to_front()
            return tab
        else:
            raise IndexError(f"Tab Index -> {index} out of range. Total tabs: {len(tabs)}")

    def switch_to_tab_by_url(self, url: str) -> Page:
        tabs = self.get_all_tabs()

        for tab in tabs:
            print("Page's url -------------------------------------------------> ", tab.url)
            if tab.url == url:
                return tab
            if url in tab.url:
                tab.bring_to_front()
                return tab
            else:
                raise ValueError(f"Tab URL -> {url} not found.")
        return None

    def switch_to_last_tab(self):
        pages = self.context.pages
        if pages:
            return pages[-1]
        raise ValueError("No tabs available")

    def close_tab(self, index: int = None):
        if index is None:
            self.page.close()
        else:
            tabs = self.get_all_tabs()
            if index < len(tabs):
                tabs[index].close()
            else:
                raise IndexError(f"Index -> {index} out of range. Total tabs: {len(tabs)}")

    def close_all_tab_except_current(self):
        current_tab = self.page
        tabs = self.get_all_tabs()

        for tab in tabs:
            if tab != current_tab:
                tab.close()

    def wait_for_new_tab(self, original_tab_count:int, timeout: int = 10000) -> Page:
        self.page.wait_for_function(f"() => {self.context}.pages.length > {original_tab_count}",timeout=timeout)
        new_tabs = [tab for tab in self.context.pages if tab not in self.get_all_tabs()[:original_tab_count]]
        if new_tabs:
            return new_tabs[0]
        raise TimeoutError("No new tabs did not open within {timeout} timeout")
    # """-----------------------------------------------------------------------------------------------------------------

    def re_fresh_screen(self):
        # self.page.wait_for_selector(success_message)
        self.page.reload()

    def re_fresh_screen2(self, success_message):
        self.page.wait_for_selector(success_message)
        self.page.reload()

    def click(self, locator):
        global elem
        try:
            self.get_element(locator).wait_for(timeout=self.timeout)
            elem = self.get_element(locator)
            elem.click(timeout=self.timeout)
        except Exception as e:
            self.page.eval_on_selector_all(".error-message", """elements => {
                        elements.forEach(el => {
                            el.style.border = "2px solid red";
                            el.style.backgroundColor = "rgba(255, 0, 0, 0.1)";
                        });
                    }""")
            # print(f"Error --> {e}")

    def click_by_order(self, locator, order=1):
        global elem
        try:
            self.get_element(locator).nth(order).wait_for(timeout=self.timeout)
            self.get_element(locator).nth(order).click(timeout=self.timeout)
        except Exception as e:
            self.page.eval_on_selector_all(".error-message", """elements => {
                                    elements.forEach(el => {
                                        el.style.border = "2px solid red";
                                        el.style.backgroundColor = "rgba(255, 0, 0, 0.1)";
                                    });
                                }""")
            # print(f"Error --> {e}")

    def fill(self, locator: object, text: object) -> None:
        global elem
        try:
            self.get_element(locator).wait_for(timeout=self.timeout)
            elem = self.get_element(locator)
            elem.fill(text, timeout=self.timeout)
        except Exception as e:
            self.page.eval_on_selector_all(".error-message", """elements => {
                                    elements.forEach(el => {
                                        el.style.border = "2px solid red";
                                        el.style.backgroundColor = "rgba(255, 0, 0, 0.1)";
                                    });
                                }""")
            # print(f"Error --> {e}")

    def type(self, locator, text):
        global elem
        try:
            self.get_element(locator).wait_for(timeout=self.timeout)
            elem = self.get_element(locator)
            elem.type(text, timeout=self.timeout)
        except Exception as e:
            self.page.eval_on_selector_all(".error-message", """elements => {
                                    elements.forEach(el => {
                                        el.style.border = "2px solid red";
                                        el.style.backgroundColor = "rgba(255, 0, 0, 0.1)";
                                    });
                                }""")
            print(f"Error --> {e}")

    def clear_field(self, locator):
        global elem
        try:
            self.get_element(locator).wait_for(timeout=self.timeout)
            elem = self.get_element(locator)
            elem.clear(timeout=self.timeout)
        except Exception as e:
            self.page.eval_on_selector_all(".error-message", """elements => {
                                                elements.forEach(el => {
                                                    el.style.border = "2px solid red";
                                                    el.style.backgroundColor = "rgba(255, 0, 0, 0.1)";
                                                });
                                            }""")
            print(f"Error --> {e}")

    def get_element_text(self, locator):
        self.get_element(locator).wait_for(timeout=self.timeout)
        return self.get_element(locator).text_content(timeout=self.timeout)

    def wait_element(self, locator):
        self.get_element(locator).wait_for(timeout=self.timeout)

    def is_element_visible(self, locator):
        try:
            self.get_element(locator).wait_for(timeout=self.timeout)
            return self.get_element(locator).is_visible(timeout=self.timeout)
        except Exception as e:
            print(f"Error --> {e}")
            return False

    def get_screenshot(self, screenshot_name):
        self.page.screenshot(path="screenshots/{}".format(screenshot_name), full_page=True)

    def scroll_to_element(self, locator):
        self.get_element(locator).scroll_into_view_if_needed(timeout=self.timeout)

    def check(self, locator):
        self.get_element(locator).wait_for(timeout=self.timeout)
        self.get_element(locator).check()

    def is_element_checked(self, locator):
        self.get_element(locator).wait_for(timeout=self.timeout)
        return self.get_element(locator).is_checked()

    def upload_file(self, locator, file_path):
        self.get_element(locator).wait_for(timeout=self.timeout)
        with self.page.expect_file_chooser() as f_c:
            self.get_element(locator).click()
            file_chooser = f_c.value
            file_chooser.set_files(file_path)

    def check_expected_txt_exists(self, txt, locator):
        self.get_element(locator).wait_for(timeout=self.timeout)
        expect(self.get_element(locator)).to_contain_text(txt)
        return True

    def generate_random_str(self, length):
        rand_str = "Avto-test: " + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        return rand_str

    def infinite_scroll_to_element(self, target_element_or_text, max_tries=30):
        for _ in range(max_tries):
            try:
                if self.is_element_visible(target_element_or_text):
                    self.click(target_element_or_text)
                    break
            except Exception as e:
                self.page.keyboard.press("Down")
                self.page.wait_for_timeout(timeout=5000)
