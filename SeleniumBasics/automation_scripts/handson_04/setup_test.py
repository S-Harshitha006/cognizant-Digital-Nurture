"""
Hands-On 4 – Selenium WebDriver Setup

Task 24: Selenium Components

1. WebDriver
   - WebDriver is a browser automation API that controls web browsers.
   - It communicates with browser-specific drivers (such as ChromeDriver)
     to perform actions like opening pages, clicking elements, and entering text.

2. Selenium Grid
   - Selenium Grid enables parallel execution of tests across multiple
     browsers, browser versions, and machines.
   - It reduces test execution time and supports cross-browser testing.

3. Selenium IDE
   - Selenium IDE is a browser extension used for recording and replaying
     browser interactions.
   - It is useful for beginners and can generate automation scripts.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Task 27 - Run Chrome in headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

# Launch Chrome using webdriver-manager
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Task 26 - Implicit Wait
# Implicit wait applies globally to all element searches.
# Explicit waits are preferred because they wait only for specific elements,
# making tests faster, more reliable, and easier to maintain.
driver.implicitly_wait(10)

try:
    # Task 25
    driver.get("https://www.lambdatest.com/selenium-playground/")

    print("Page Title:")
    print(driver.title)

finally:
    driver.quit()