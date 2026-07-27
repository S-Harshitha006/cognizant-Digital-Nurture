from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)

try:
    # Open Selenium Playground
    driver.get("https://www.lambdatest.com/selenium-playground/")

    # Open Simple Form Demo
    driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

    print("===== Task 32 : Locator Strategies =====")

    # By.ID
    element_id = driver.find_element(By.ID, "user-message")
    print("By.ID ✓")

    # By.NAME
    element_name = driver.find_element(By.NAME, "message")
    print("By.NAME ✓")

    # By.CLASS_NAME
    element_class = driver.find_element(By.CLASS_NAME, "form-control")
    print("By.CLASS_NAME ✓")

    # By.TAG_NAME
    element_tag = driver.find_element(By.TAG_NAME, "input")
    print("By.TAG_NAME ✓")

    # By.XPATH (Absolute)
    element_xpath_absolute = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/section[2]/div/div/div[1]/div/input"
    )
    print("Absolute XPath ✓")

    # By.XPATH (Relative)
    element_xpath_relative = driver.find_element(
        By.XPATH,
        "//input[@id='user-message']"
    )
    print("Relative XPath ✓")

    print("\n===== Task 33 : CSS Selectors =====")

    # CSS by ID
    css1 = driver.find_element(By.CSS_SELECTOR, "#user-message")
    print("CSS #id ✓")

    # CSS by Attribute
    css2 = driver.find_element(
        By.CSS_SELECTOR,
        "input[name='message']"
    )
    print("CSS Attribute ✓")

    # CSS Parent > Child
    css3 = driver.find_element(
        By.CSS_SELECTOR,
        "div.form-group > input"
    )
    print("CSS Parent > Child ✓")

    print("\n===== Task 34 : XPath text() & contains() =====")

    driver.back()

    driver.find_element(By.LINK_TEXT, "Checkbox Demo").click()

    # XPath using text()
    label = driver.find_element(
        By.XPATH,
        "//label[text()='Option 1']"
    )

    print("Label:", label.text)

    # XPath contains()
    labels = driver.find_elements(
        By.XPATH,
        "//label[contains(text(),'Option')]"
    )

    print("Labels Found:", len(labels))

    for l in labels:
        print(l.text)

    """
    Task 35 - Locator Ranking

    1. ID
       - Unique, fastest, most reliable.

    2. Name
       - Usually unique and readable.

    3. CSS Selector
       - Fast and flexible.

    4. Relative XPath
       - Powerful but slightly slower.

    5. Class Name
       - May not be unique.

    6. Absolute XPath
       - Least preferred because it breaks
         whenever page structure changes.
    """

finally:
    driver.quit()