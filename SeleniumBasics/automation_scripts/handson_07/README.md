## Page Object Model Benefit

Without Page Object Model, if the Submit button ID changes from:

submit

to

btn-submit

every Selenium test using:

driver.find_element(By.ID, "submit")

must be modified individually.

With Page Object Model, the locator is stored only once inside the page class.

Only one line needs to be updated:

SUBMIT_BUTTON = (By.ID, "btn-submit")

All tests continue to work without modification.

This improves maintainability, readability, and reduces duplication.