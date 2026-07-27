from pages.simple_form_page import SimpleFormPage
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage


def test_simple_form_submission(driver, base_url):

    page = SimpleFormPage(driver)

    page.navigate_to(base_url + "simple-form-demo")

    page.enter_message("Hello Selenium")

    page.click_submit()

    assert page.get_displayed_message() == "Hello Selenium"


def test_checkbox_demo(driver, base_url):

    page = CheckboxPage(driver)

    page.navigate_to(base_url + "checkbox-demo")

    page.check_option()

    assert page.is_option_checked()

    page.uncheck_option()

    assert not page.is_option_checked()


def test_dropdown_selection(driver, base_url):

    page = DropdownPage(driver)

    page.navigate_to(base_url + "select-dropdown-demo")

    page.select_day("Wednesday")

    assert True

def test_input_form_submit(driver, base_url):

    from pages.input_form_page import InputFormPage

    page = InputFormPage(driver)

    page.navigate_to(base_url + "input-form-demo")

    page.fill_form(
        "John",
        "john@example.com",
        "9876543210",
        "Chennai"
    )

    page.submit_form()

    assert page.get_success_message() != ""    