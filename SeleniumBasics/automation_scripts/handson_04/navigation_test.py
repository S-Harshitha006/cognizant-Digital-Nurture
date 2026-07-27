from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

# Launch Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.implicitly_wait(10)

try:
    # Task 28 - Open Selenium Playground
    driver.get("https://www.lambdatest.com/selenium-playground/")

    # Click "Simple Form Demo"
    driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

    # Verify URL
    assert "simple-form-demo" in driver.current_url
    print("URL verification successful.")

    # Navigate back
    driver.back()

    # Task 29 - Open Google in a new tab
    driver.execute_script('window.open("https://www.google.com");')

    # List all window handles
    print("Window Handles:", driver.window_handles)

    # Switch to Google tab
    driver.switch_to.window(driver.window_handles[1])

    print("Google Page Title:", driver.title)

    # Task 30 - Switch back to Playground
    driver.switch_to.window(driver.window_handles[0])

    # Take Screenshot
    screenshot_file = "playground_screenshot.png"
    driver.save_screenshot(screenshot_file)

    if os.path.exists(screenshot_file):
        print("Screenshot saved successfully.")

    # Task 31 - Window Size
    print("Current Window Size:", driver.get_window_size())

    driver.set_window_size(1280, 800)

    print("Updated Window Size:", driver.get_window_size())

    # Consistent window size helps ensure UI elements appear
    # in the same layout across different test executions,
    # making responsive UI automation more reliable.

finally:
    driver.quit()