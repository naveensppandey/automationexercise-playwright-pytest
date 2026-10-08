# AutomationExercise Playwright POM Framework

A beginner-friendly, end-to-end UI automation testing framework built using **Python**, **Playwright (Sync API)**, **Pytest**, **Page Object Model (POM)**, **Excel & CSV Data-Driven Testing**, **Keyword-Driven Testing**, **BDD (pytest-bdd)**, **Jenkins CI/CD**, and **GitHub Actions**.

---

## 📁 Project Structure

```
AutomationExercise_Playwright/
│
├── .github/
│   └── workflows/
│       └── playwright-tests.yml  # GitHub Actions CI/CD Workflow
│
├── .vscode/
│
├── features/
│   └── login.feature             # BDD Feature File (Gherkin format)
│
├── pages/                        # Page Object Classes
│   ├── base_page.py              # Parent class with reusable Playwright actions
│   ├── home_page.py              # Home page locators and actions
│   ├── login_page.py             # Login & signup page locators and actions
│   ├── products_page.py          # Products catalog & 3-level randomization
│   └── cart_page.py              # Shopping cart view and assertions
│
├── screenshots/                  # Failure screenshots directory (auto-captured)
│
├── test_data/                    # Test Data Files
│   ├── login_data.csv            # CSV file with user login accounts
│   └── test_cases.xlsx           # Excel file containing 50 test cases
│
├── tests/                        # Test Suites
│   ├── step_definitions/
│   │   └── test_login_steps.py   # BDD Step Definitions using pytest-bdd
│   ├── test_excel_data_driven.py # Excel Data-Driven test suite
│   ├── test_keyword_driven.py   # Keyword-Driven test suite
│   ├── test_login.py             # Login tests & CSV data-driven login test
│   └── test_product_purchase.py  # End-to-end product purchase test
│
├── utils/                        # Helper Utilities
│   ├── csv_data_provider.py      # Utility to read CSV test data
│   ├── excel_data_provider.py    # Utility to read Excel test cases (openpyxl)
│   └── keyword_actions.py        # Utility to execute Keyword Driven actions
│
├── .gitignore
├── conftest.py                   # Pytest fixtures, multi-browser (--browser), hooks
├── Jenkinsfile                   # Jenkins CI/CD Pipeline definition
├── pytest.ini                    # Pytest configuration & test discovery
├── README.md                     # Project documentation
└── requirements.txt              # Python package dependencies
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.8 or higher installed on your system.

### 2. Installation
Open your terminal in the project directory and run:

```bash
# Install Python package dependencies
pip install -r requirements.txt

# Install Playwright browser binaries
playwright install
```

---

## 🧪 Running Tests

### Run All Tests (Chromium - Default)
```bash
pytest
```

### Run Tests on Chromium Browser
```bash
pytest --browser chromium
```

### Run Tests on Firefox Browser
```bash
pytest --browser firefox
```

### Run Tests in Headed Mode (Watch Browser UI Live)
```bash
pytest --headed -s
```

### Run BDD Feature Tests
```bash
pytest tests/step_definitions/test_login_steps.py
```

### Run Keyword-Driven Tests
```bash
pytest tests/test_keyword_driven.py
```

### Run Excel Data-Driven Tests
```bash
pytest tests/test_excel_data_driven.py
```

---

## 💡 Key Testing Concepts Explained

### 1. Page Object Model (POM)
Web pages are represented as Python classes (`pages/home_page.py`, `pages/login_page.py`). Locators and actions live inside Page Object classes, keeping test files clean and readable.

### 2. Data-Driven Testing (CSV & Excel)
- **CSV**: Uses `utils/csv_data_provider.py` and `@pytest.mark.parametrize` to run tests across multiple rows in `test_data/login_data.csv`.
- **Excel**: Uses `utils/excel_data_provider.py` (powered by `openpyxl`) to read test cases from `test_data/test_cases.xlsx`.

### 3. Keyword-Driven Testing
Test steps are defined as high-level keywords (`OPEN`, `CLICK`, `FILL`, `SEARCH`, `ADD_TO_CART`, `OPEN_CART`, `LOGOUT`). The keyword execution helper `utils/keyword_actions.py` maps each keyword to Playwright page actions.

### 4. BDD (Behavior-Driven Development)
Feature scenarios are written in Gherkin format inside `features/login.feature` using Given-When-Then steps. Step definitions in `tests/step_definitions/test_login_steps.py` bind each Gherkin step to Page Object actions using `pytest-bdd`.

### 5. Multi-Browser Testing (Chromium & Firefox)
Configured via `conftest.py`. You can execute the test suite against Chromium or Firefox seamlessly using `--browser chromium` or `--browser firefox`.

### 6. Continuous Integration (CI/CD)
- **Jenkins Pipeline (`Jenkinsfile`)**: Defines stages for Checkout, Installing Dependencies, Installing Playwright, Running Pytest, and generating JUnit XML reports (`test-results.xml`).
- **GitHub Actions (`.github/workflows/playwright-tests.yml`)**: Automatically triggers test runs on `push` and `pull_request` to the repository.



