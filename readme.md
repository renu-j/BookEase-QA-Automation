# BookEase QA Automation

A professional UI, API, and End-to-End (E2E) test automation framework built with Python, Selenium, Pytest, and Requests
for validating the BookEase / Restful Booker demo application.

The framework follows the "Page Object Model (POM)" design pattern and includes functional, negative, boundary, API, and E2E testing,
together with automatic failure screenshots, HTML reporting, and a lightweight AI-assisted failure analysis component.


##  Project Overview
BookEase QA Automation is designed to demonstrate a maintainable and scalable automated testing framework for a hotel booking application.

The framework validates:
* Website navigation and core UI functionality
* Room availability and date validation
* Booking form validation
* Contact form validation
* REST API functionality
* Complete end-to-end booking flow
* Negative and boundary scenarios
* Automatic screenshots when UI tests fail
* AI-assisted failure analysis
* Automated HTML test reporting

##  Testing Objectives

The primary objectives of this project are to:

1. Automate critical application workflows.
2. Validate positive and negative functional scenarios.
3. Validate boundary conditions.
4. Validate REST API endpoints.
5. Validate an end-to-end hotel booking workflow.
6. Reduce manual regression testing effort.
7. Capture visual evidence automatically when UI tests fail.
8. Provide actionable failure analysis.
9. Generate a consolidated HTML execution report.


## 🛠️ Technology Stack

| Technology          | Purpose                    |
| ------------------- | -------------------------- |
| Python 3.14.7       | Programming language       |
| Selenium 4.49.0     | Web UI automation          |
| Pytest 9.1.1        | Test framework             |
| Requests 2.34.2     | API testing                |
| pytest-html 4.2.0   | HTML test reporting        |
| python-dotenv 1.2.3 | Environment configuration  |
| Microsoft Edge      | WebDriver / browser        |
| Page Object Model   | UI automation architecture |
| Git / GitHub        | Version control            |



## Project Architecture


BookEase-QA-Automation/
│
├── config/
│
├── pages/
│   ├── base_page.py
│   ├── home_page/
│   ├── availability_page/
│   ├── rooms_page.py
│   ├── booking_page/
│   └── contact_page/
│
├── tests/
│   ├── api/
│   │   ├── test_auth_api.py
│   │   └── test_booking_api.py
│   │
│   ├── e2e/
│   │   └── test_e2e_booking.py
│   │
│   └── ui/
│       ├── test_availability.py
│       ├── test_booking.py
│       ├── test_contact.py
│       ├── test_homepage.py
│       ├── test_rooms.py
│       └── test_smoke.py
│
├── utils/
│   └── ai_failure_analyzer.py
│
├── reports/
│   ├── ai/
│   ├── screenshots/
│   └── final_report.html
│
├── .env
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md


> The `config/` directory is reserved for future environment/framework configuration as the automation framework grows. 
> It is currently not required by the implemented test execution flow.



# Framework Design

## Page Object Model

The UI automation framework uses the Page Object Model (POM) pattern.

Common page functionality is centralized in:
pages/base_page.py


The `BasePage` provides reusable Selenium operations such as:

* Click
* Enter text
* Retrieve text
* Visibility checks
* Element presence checks
* Explicit waits
* Scrolling before interaction

Individual application pages inherit from `BasePage`.

This reduces duplicated Selenium code and makes the framework easier to maintain when UI locators or workflows change.

# Test Coverage

The final automated execution contains 30 active tests.

## API Testing

### Authentication API
tests/api/test_auth_api.py
Covered scenarios:
* Valid login
* Invalid password
* Invalid username

### Booking API
```text
tests/api/test_booking_api.py
```
Covered scenarios:
* Retrieve bookings
* Create booking
* Delete booking


#  UI Testing
## Availability Testing
```text
tests/ui/test_availability.py
```
Covered scenarios:
* Valid check-in and check-out dates
* Multi-night stay
* Check-out before check-in
* Same check-in and check-out date
* Clear check-in date
* Clear check-out date
* Historical dates

## Booking Testing
```text
tests/ui/test_booking.py
```
Covered scenarios include phone-number boundary validation:
* Phone number below minimum
* Minimum valid phone number
* Maximum valid phone number
* Phone number above maximum

## Contact Testing
```text
tests/ui/test_contact.py
```
Covered scenarios:
* Valid contact submission
* Empty contact form validation
* Phone number below minimum length
* Message below minimum length
* Minimum boundary values

## Homepage Testing
```text
tests/ui/test_homepage.py
```
Covered scenarios:
* Homepage loads successfully
* Navigation is visible
* Hotel heading is visible

## Rooms Testing
```text
tests/ui/test_rooms.py
```
Covered scenarios:
* Rooms section visibility
* Rooms are displayed
* Room names are displayed


## Smoke Testing
```text
tests/ui/test_smoke.py
```
The smoke test validates that the primary application homepage is available and functioning.


#  End-to-End Testing
The framework includes a complete hotel booking E2E workflow:
```text
tests/e2e/test_e2e_booking.py
```
The E2E test validates the complete user journey through the application rather than testing an isolated component.
## E2E Result
```text
test_complete_hotel_booking_e2e PASSED
```


#  AI-Assisted Failure Analysis
The framework includes a lightweight AI-assisted failure analysis component:
```text
utils/ai_failure_analyzer.py
```
The component analyzes failure messages and provides troubleshooting guidance based on common failure categories such as:
* TimeoutException
* NoSuchElementException
* AssertionError
* TypeError
* Connection-related failures
* Unknown/unclassified failures

Example output:
```text
AI FAILURE ANALYSIS
===================

Test: test_home_page_loads

Analysis:
Likely cause: The actual application result did not
match the expected result.

Suggested action:
Review the assertion and compare the expected result
with the actual application behavior.
```

### Important
This implementation is a lightweight rule-based AI-assisted analysis component. 
It does not call an external generative AI API or LLM.
Its purpose is to automatically classify common failures and provide an initial troubleshooting suggestion.


#  Automatic Failure Screenshots
The Selenium fixture in:
```text
conftest.py
```
automatically captures a screenshot when a UI test fails.
Screenshots are stored under:
```text
reports/screenshots/
```

Example:
```text
reports/screenshots/<test_name>.png
```
This provides visual evidence of the application state at the time of failure.


# HTML Test Reporting
The project uses pytest-html to generate a consolidated execution report.
Generate the final report with:
```powershell
pytest -v --html=reports/final_report.html --self-contained-html
```

The report contains:
* Test execution summary
* Pass/fail status
* Individual test results
* Execution duration
* Python/environment information
* Pytest plugin information

The final validated report contains:

```text
30 Tests
30 Passed
0 Failed
0 Skipped
0 Errors
```

---

#  Environment Configuration
Environment-specific values are stored in:
```text
.env
```
Example:
```text
BASE_URL=https://automationintesting.online/
API_BASE_URL=https://automationintesting.online/
BROWSER=edge
HEADLESS=false
AI_ENABLED=false
```
Sensitive or environment-specific values should not be committed to source control.
---
#  Installation

## 1. Clone the Repository

```powershell
git clone <repository-url>
cd BookEase-QA-Automation
```

## 2. Create Virtual Environment

```powershell
python -m venv .venv
```

## 3. Activate Virtual Environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## 4. Install Dependencies

```powershell
pip install -r requirements.txt
```

---

# ▶️ Running the Tests

## Run the complete test suite

```powershell
pytest -v
```

## Run UI tests

```powershell
pytest -v -m ui
```

## Run API tests

```powershell
pytest -v -m api
```

## Run E2E tests

```powershell
pytest -v -m e2e
```

## Run negative tests

```powershell
pytest -v -m negative
```

## Run boundary tests

```powershell
pytest -v -m boundary
```

## Exclude the AI demonstration test

```powershell
pytest -v -m "not ai_demo"
```

---

# Pytest Configuration

Test markers are defined in:

```text
pytest.ini
```

Available markers include:

```text
smoke
regression
ui
api
e2e
negative
boundary
ai_demo
```

These markers allow selective execution of different categories of tests.

---

# Security and Git Hygiene

The project excludes local and sensitive files from version control.

Examples include:

```text
.venv/
.env
.idea/
__pycache__/
.pytest_cache/
```

Generated temporary reports and execution artifacts can also be excluded where appropriate.

The `.env` file should never contain production secrets or credentials committed to Git.

---

# Final Test Results

Latest validated full-suite execution:

| Category    | Result |
| ----------- | -----: |
| Total tests |     30 |
| Passed      |     30 |
| Failed      |      0 |
| Skipped     |      0 |
| Errors      |      0 |

### Final Result

```text
30 passed
0 failed
0 skipped
0 errors
```

Execution time was approximately:

```text
02:48
```

---

# Project Capabilities

The completed framework demonstrates:

* [x] Selenium UI automation
* [x] Page Object Model
* [x] Pytest test framework
* [x] API testing
* [x] End-to-End testing
* [x] Positive testing
* [x] Negative testing
* [x] Boundary testing
* [x] Smoke testing
* [x] Explicit waits
* [x] Automatic failure screenshots
* [x] AI-assisted failure analysis
* [x] HTML test reporting
* [x] Environment configuration
* [x] Git-ready project structure

---

# Future Enhancements

The framework can be extended with additional capabilities as the project grows:

* CI/CD integration using GitHub Actions
* Parallel test execution
* Cross-browser execution
* API schema validation
* Enhanced test-data management
* Database validation
* Allure reporting
* Integration with external LLM-based failure analysis
* Automatic defect/ticket creation
* Advanced execution history and trend reporting

These are future enhancements and are **not required for the current validated implementation**.

---

# Key Files

| File / Directory               | Purpose                           |
| ------------------------------ | --------------------------------- |
| `conftest.py`                  | Selenium fixture and pytest hooks |
| `pytest.ini`                   | Pytest configuration and markers  |
| `pages/`                       | Page Object Model implementation  |
| `tests/ui/`                    | UI test cases                     |
| `tests/api/`                   | API test cases                    |
| `tests/e2e/`                   | End-to-end test cases             |
| `utils/ai_failure_analyzer.py` | Failure analysis component        |
| `reports/`                     | Test reports and evidence         |
| `.env`                         | Environment configuration         |
| `requirements.txt`             | Python dependencies               |
| `README.md`                    | Project documentation             |

---

# Conclusion
BookEase QA Automation provides a structured automated testing solution covering the application's UI, API, and end-to-end workflows.
The framework combines reusable Page Objects, Pytest fixtures, functional/negative/boundary testing, automated failure evidence,
AI-assisted failure analysis, and HTML reporting.
The latest validated execution completed with:
```text
30 / 30 tests passed
0 failures
0 errors
```
The framework is structured to support future expansion while keeping the current automation implementation maintainable and easy to execute.
