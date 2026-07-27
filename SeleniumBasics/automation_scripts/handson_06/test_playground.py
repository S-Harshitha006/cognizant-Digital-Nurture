from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_simple_form_submission(driver):

    driver.get("https://www.lambdatest.com/selenium-playground/")

    driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

    message = driver.find_element(By.ID, "user-message")
    message.clear()
    message.send_keys("Hello Selenium")

    driver.find_element(By.ID, "showInput").click()

    output = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert output.text == "Hello Selenium"


def test_checkbox_demo(driver):

    driver.get("https://www.lambdatest.com/selenium-playground/")

    driver.find_element(By.LINK_TEXT, "Checkbox Demo").click()

    checkbox = driver.find_element(By.ID, "isAgeSelected")

    checkbox.click()

    assert checkbox.is_selected()

    checkbox.click()

    assert not checkbox.is_selected()