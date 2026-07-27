# Hands-On 3 – Test Automation Process, Lifecycle & Framework Types

## Task 1: Automation Decision and Test Case Selection

### 17. Criteria for Deciding Whether to Automate a Test Case

| Criteria | Explanation | Application to POST /api/courses/ Test |
|----------|-------------|-----------------------------------------|
| Repetitive Execution | Tests executed frequently are good automation candidates. | This API test is executed after every code change, so it should be automated. |
| Stable Functionality | Stable features reduce script maintenance. | The POST endpoint is a core API and changes infrequently. |
| Regression Testing | Regression tests are ideal for automation. | The endpoint must always return HTTP 201 for valid requests. |
| High Business Impact | Critical business functionality should be automated. | Course creation is a primary feature of the system. |
| Data-Driven Testing | Tests with multiple input combinations are suitable for automation. | Different course names, IDs, and departments can be tested automatically. |

---

### 18. Automate or Manual

| Test Case | Decision | Justification |
|-----------|----------|---------------|
| (a) Regression test for all CRUD endpoints | Automate | Frequently executed after every code change. |
| (b) Exploratory testing of a new search feature | Manual | Requires human creativity and observation. |
| (c) Performance test for 100 concurrent users | Automate | Performance tools can execute repeated load tests efficiently. |
| (d) UI login form test | Automate | Login is stable and executed in almost every regression cycle. |
| (e) Verify Swagger documentation | Manual | Documentation changes are infrequent and require manual review. |
| (f) Smoke test after deployment | Automate | Must run immediately after every deployment. |

---

### 19. Test Automation ROI

**Definition**

Test Automation ROI (Return on Investment) measures whether the time and effort spent creating automated tests are recovered through repeated execution.

**Calculation**

Automation Development Time = **4 hours**

Manual Execution Time = **30 minutes = 0.5 hour**

Break-even Runs

```
4 ÷ 0.5 = 8 runs
```

Therefore, after approximately **8 executions**, the automation pays for itself.

**Maintenance Overhead**

After the 10th run, assume a maintenance effort of **20%** of the manual execution time.

Maintenance per run:

```
20% × 0.5 hour = 0.1 hour
```

Even with maintenance, automation remains more efficient than manual execution for long-term regression testing.

---

### 20. Flaky Test

**Definition**

A flaky test is a test that sometimes passes and sometimes fails without any changes to the application.

**Example**

A Selenium test clicks the Login button before the page finishes loading, causing random failures.

**Ways to Prevent Flaky Tests**

1. Use Explicit Waits instead of fixed delays.
2. Use reliable locators such as ID or Name instead of dynamic XPath.
3. Ensure test data and environments remain consistent.

---

# Task 2 – Compare Automation Framework Types

## 21. Automation Framework Comparison

### 1. Linear Framework

**Description**

Test scripts are written sequentially from start to finish without separating reusable components.

**Advantage**

Simple and easy to learn.

**Disadvantage**

Poor reusability and difficult maintenance.

**Example**

Suitable for a small login verification script.

---

### 2. Modular Framework

**Description**

The application is divided into reusable modules such as Login, Dashboard, and Course Management.

**Advantage**

Code reuse and easier maintenance.

**Disadvantage**

Requires careful planning of modules.

**Example**

Reuse the Login module across all Course Management tests.

---

### 3. Data-Driven Framework

**Description**

Test data is stored externally in Excel, CSV, or JSON files while the same script executes multiple datasets.

**Advantage**

Supports large numbers of input combinations.

**Disadvantage**

Requires management of external data files.

**Example**

Testing login with 50 different usernames and passwords.

---

### 4. Keyword-Driven Framework

**Description**

Test steps are represented using keywords such as Click, EnterText, Verify, allowing non-programmers to create test cases.

**Advantage**

Easy for non-technical testers.

**Disadvantage**

More complex framework design.

**Example**

Business analysts define keyword-based login tests.

---

### 5. Hybrid Framework

**Description**

Combines Modular, Data-Driven, and Keyword-Driven approaches for maximum flexibility.

**Advantage**

Highly reusable, scalable, and maintainable.

**Disadvantage**

Initial setup is more complex.

**Example**

Large Selenium projects with reusable page objects and external test data.

---

## 22. Recommended Framework

**Recommended Framework: Hybrid Framework**

### Justification

The Hybrid Framework is the best choice because:

- Supports testing with 50 different user/password combinations through Data-Driven Testing.
- Reuses Login functionality across multiple test cases using the Modular approach.
- Allows technical and non-technical team members to contribute through Keyword-Driven concepts.
- Easy to maintain as the application grows.

---

## 23. Hybrid Framework Folder Structure

```text
CourseManagementAutomation/

├── config/
│   └── config.py
│
├── test_data/
│   ├── login_data.xlsx
│   └── course_data.xlsx
│
├── page_objects/
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── course_page.py
│
├── utilities/
│   ├── browser_utils.py
│   ├── wait_utils.py
│   └── logger.py
│
├── test_cases/
│   ├── test_login.py
│   ├── test_courses.py
│   └── test_smoke.py
│
├── reports/
│
├── screenshots/
│
├── requirements.txt
│
└── pytest.ini
```

### Explanation

- **config** – Stores configuration settings.
- **test_data** – Contains Excel or CSV test data.
- **page_objects** – Implements the Page Object Model.
- **utilities** – Contains reusable helper functions.
- **test_cases** – Stores Selenium test scripts.
- **reports** – Stores execution reports.
- **screenshots** – Stores failure screenshots.
- **requirements.txt** – Lists project dependencies.
- **pytest.ini** – Configures pytest execution.