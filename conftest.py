import datetime
import re
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright
import allure_pytest
from slugify.slugify import slugify

from screens.auth_main_screens.authorization_main_screen import AuthorizationScreen
from screens.auth_main_screens.home_screen import HomeScreen
from screens.company_screens.company_screen import CompanyScreen
from screens.catalogue_screens.catalogue_screen import CatalogueScreen
from screens.warehouse_screens.income_screen import IncomeScreen
from screens.web_kassa.auth_main_screen.web_auth_home_screen import WebAuthHomeScreen
# from utils.tab_handler import TabHandler
import pathlib
import allure



@pytest.fixture(autouse=False, scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=450, args=["--start-maximized"])
        yield browser
        browser.close()

@pytest.fixture
def page(browser, new_page=False):
    timeout = 18000
    # context = browser.new_context(no_viewport=True, record_video_dir="./allure-report/video_reports")
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.set_default_navigation_timeout(timeout)
    page.set_default_timeout(timeout)
    # page.set_viewport_size({"width": 1920, "height": 1080})
    yield page
    context.close()

@pytest.fixture
def context(browser):
    timeout = 18000
    context = browser.new_context(no_viewport=True)
    yield context
    context.close()

# @pytest.fixture
# def new_page(browser, page):
#     timeout = 10000
#     # context = browser.new_context(no_viewport=True, record_video_dir="./allure-report/video_reports")
#     context = browser.new_context(no_viewport=True)
#     with context.expect_page() as new_tab:
#         page.evaluate()
#     page = context.new_page()
#     page.set_default_navigation_timeout(timeout)
#     page.set_default_timeout(timeout)
#     # page.set_viewport_size({"width": 1920, "height": 1080})
#     yield page
#     context.close()


@pytest.fixture
def auth_screen(page) -> AuthorizationScreen:
    return AuthorizationScreen(page)

@pytest.fixture
def home_screen(page) -> HomeScreen:
    return HomeScreen(page)

@pytest.fixture
def company_screen(page) -> CompanyScreen:
    return CompanyScreen(page)

@pytest.fixture
def catalogue_screen(page) -> CatalogueScreen:
    return CatalogueScreen(page)

@pytest.fixture
def income_screen(page) -> IncomeScreen:
    return IncomeScreen(page)

@pytest.fixture
def web_auth_home_screen(page) -> WebAuthHomeScreen:
    return WebAuthHomeScreen(page)

# @pytest.fixture
# def tab_handler(page) -> TabHandler:
#     return TabHandler(page)

@pytest.fixture
def authorize_user(page, auth_screen, home_screen):
    page.goto("https://cabinet-dev.smartpos.uz/")
    with allure.step("Checking Authorizatoin page open or not"):
        assert auth_screen.is_authorization_page_open()
    with allure.step("Select authization type - По логину и паролю"):
        auth_screen.select_auth_type()
        print("PAGE TITLE IS:  --------------------> ", home_screen.get_page_title())
    with allure.step("Enter phone number"):
        auth_screen.enter_phone_number("90 320 90 08")
    with allure.step("Enter password"):
        auth_screen.enter_password("aA987654321")
    with allure.step("Check Remember me checkbox"):
        auth_screen.check_remember_me_checkbox()
    with allure.step("Click on 'Войти' btn"):
        auth_screen.click_on_login_btn()
    # with allure.step("Checking 'Главная страница' page is open"):
    #     assert home_screen.is_home_page_open()

@pytest.fixture
def authorize_user_to_virtual_kassa():
    pass

"""
            *******  Configuring video record in allure report  ******* 
"""

allure.attach.file(
    "file_name.png",
    name="video attachment",
    attachment_type=allure.attachment_type.PNG
)

# @pytest.fixture
# def attach_screenshot(page):
#     allure.attach(
#         page.screenshot(path="screenshot.png"),
#         name="Failure_page.png",
#         attachment_type=allure.attachment_type.PNG,
#     )

# @pytest.fixture()
# def get_failure_screenshot(request, page):
#     yield
#     item = request.node
#     if item.rep_call.failed:
#         allure.attach(page.screenshot(), name="video attachment", attachment_type=allure.attachment_type.PNG)

@pytest.fixture
def get_failure_screenshot(request, page):
    yield
    item = request.node
    if hasattr(item, "rep_call") and item.rep_call.failed:  # Check if rep_call exists and failed
        allure.attach(
            page.screenshot(full_page=True),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG
        )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, f"rep_{rep.when}", rep)

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            # Highlight all elements matching error selectors
            page.evaluate("""() => {
                document.querySelectorAll('.error, [aria-invalid="true"]').forEach(el => {
                    el.style.border = '2px solid red';
                });
            }""")

            allure.attach(
                page.screenshot(full_page=True),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )

# @pytest.hookimpl(hookwrapper=True)  WORKING ONE
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     extras = getattr(report, "extras", [])
#     if report.when == "call":
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             page = item.funcargs["page"]
#             screenshot_dir = Path("allure-report/")
#             screenshot_dir.mkdir(exist_ok=True)
#             screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
#             page.screenshot(path=screen_file)
#
#         report.extras = extras
"""
            *******  Configuring video record in allure report  ******* 
"""

