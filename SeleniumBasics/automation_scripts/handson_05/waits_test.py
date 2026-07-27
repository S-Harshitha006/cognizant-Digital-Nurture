import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # Open Selenium Playground
    driver.get("https://www.lambdatest.com/selenium-playground/")

    # Open Bootstrap Alerts Demo
    driver.find_element(By.LINK_TEXT, "Bootstrap Alerts").click()

    print("========== Task 36 ==========")

    # Wait until Success Message button is clickable
    success_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "autoclosable-btn-success"))
    )
    success_btn.click()

    # Wait for success alert to become visible
    success_alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )

    print("Alert Text:", success_alert.text)

    assert "successfully" in success_alert.text.lower()
    print("Alert verification successful.\n")

    print("========== Task 37 ==========")

    # Using time.sleep()
    start = time.time()

    driver.refresh()

    driver.find_element(By.ID, "autoclosable-btn-success").click()
    time.sleep(3)

    print("time.sleep() Execution Time:",
          round(time.time() - start, 2), "seconds")

    # Using Explicit Wait
    start = time.time()

    driver.refresh()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "autoclosable-btn-success"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )

    print("Explicit Wait Execution Time:",
          round(time.time() - start, 2), "seconds")

    print("\n========== Task 38 ==========")

    """
    visibility_of_element_located():
    - Element exists in DOM
    - Element is visible

    element_to_be_clickable():
    - Element is visible
    - Element is enabled
    - Element can actually be clicked
    """

    print("Clickability verified using Explicit Wait.\n")

    print("========== Task 39 ==========")

    # Fluent Wait (implemented using WebDriverWait)
    fluent_wait = WebDriverWait(
        driver,
        timeout=10,
        poll_frequency=0.5,
        ignored_exceptions=[NoSuchElementException]
    )

    try:
        table = fluent_wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )
        print("Fluent Wait Successful.")
    except:
        print("Dynamic table not found (website may have changed).")

finally:
    driver.quit()