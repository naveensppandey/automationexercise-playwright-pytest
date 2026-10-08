# AutomationExercise Playwright POM Framework

A beginner-friendly, industry-relevant UI automation framework built using **Python**, **Playwright**, **pytest**, **Page Object Model (POM)**, **Data-Driven Testing (CSV & Excel)**, **Keyword-Driven Testing**, **BDD (pytest-bdd)**, **Randomized Testing**, **Multi-Browser Support**, **Jenkins CI/CD**, and **GitHub Actions**.

---

## 📌 Project Overview
This project automates key user scenarios on the [AutomationExercise](https://automationexercise.com/) website. It demonstrates core automation architecture principles while remaining beginner-friendly and easy to explain. 

A key highlight of this repository is the **50-test-case Excel Repository** (`test_data/test_cases.xlsx`), which documents 50 complete test scenarios designed for future automation scope. A focused subset of **~10–12 practical scenarios** (plus BDD, keyword, and randomized tests) is automated in the active Pytest suite.

---

## 📁 Folder Structure

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
├── pages/                        # Page Object Model Classes
│   ├── base_page.py              # Parent class with reusable Playwright actions
│   ├── home_page.py              # Home page locators and actions
│   ├── login_page.py             # Login & signup page locators and actions
│   ├── products_page.py          # Products catalog & randomized selection
│   └── cart_page.py              # Shopping cart view and assertions
│
├── screenshots/                  # Failure screenshots directory (auto-captured)
│
├── test_data/                    # Test Data Files
│   ├── login_data.csv            # CSV file with user login accounts
│   └── test_cases.xlsx           # Excel Repository with 50 test cases (Documentation / Future Scope)
│
├── tests/                        # Test Suites
│   ├── step_definitions/
│   │   └── test_login_steps.py   # BDD Step Definitions using pytest-bdd
│   ├── test_excel_data_driven.py # Excel Data-Driven sample test suite
│   ├── test_keyword_driven.py   # Keyword-Driven test suite
│   ├── test_login.py             # Login tests & CSV data-driven login test
│   └── test_product_purchase.py  # Product search & randomized purchase flow
│
├── utils/                        # Helper Utilities
│   ├── csv_data_provider.py      # Utility to read CSV test data & select random users
│   ├── excel_data_provider.py    # Utility to read Excel test cases (openpyxl)
│   └── keyword_actions.py        # Utility to execute Keyword-Driven actions
│
├── .gitignore
├── conftest.py                   # Pytest fixtures, multi-browser (--browser), hooks
├── Jenkinsfile                   # Jenkins CI/CD Pipeline definition
├── pytest.ini                    # Pytest configuration & test discovery
├── README.md                     # Project documentation
└── requirements.txt              # Python package dependencies
```

---

## 🛠️ Technologies Used
- **Language**: Python 3.8+
- **Automation Tool**: Playwright (Sync API)
- **Test Runner**: pytest & pytest-bdd
- **Excel Reader**: openpyxl
- **Data Formats**: CSV & Excel (.xlsx)
- **Design Pattern**: Page Object Model (POM)
- **CI/CD**: Jenkins Pipeline & GitHub Actions

---

## 🚀 How to Install

1. **Clone the repository**:
   ```bash
   git clone https://github.com/naveensppandey/automationexercise-playwright-pytest.git
   cd AutomationExercise_Playwright
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browser binaries**:
   ```bash
   playwright install
   ```

---

## 🧪 How to Run Tests

### 1. Run Full Test Suite (Default - Headless Chromium)
```bash
pytest
```

### 2. Run Tests on Chromium Browser
```bash
pytest --browser chromium
```

### 3. Run Tests on Firefox Browser
```bash
pytest --browser firefox
```

### 4. Run Tests in Headed Mode (Watch Browser UI Live)
```bash
pytest --headed -s
```

### 5. Run Specific Test Modules
```bash
# Run Login Tests & CSV Data-Driven Tests
pytest tests/test_login.py

# Run Product Purchase & Randomization Tests
pytest tests/test_product_purchase.py

# Run BDD Feature Tests
pytest tests/step_definitions/test_login_steps.py

# Run Keyword-Driven Tests
pytest tests/test_keyword_driven.py

# Run Excel Data-Driven Sample Tests
pytest tests/test_excel_data_driven.py
```

---

## 💡 Key Framework Concepts Explained

### 1. Excel Test-Case Repository (Documentation & Future Scope)
- Located in `test_data/test_cases.xlsx`.
- Contains **50 structured test cases** across Authentication, Product Navigation, Cart Management, Search, Category Navigation, and Checkout.
- **Strategy**: Serves as a test repository demonstrating full test coverage design. A sample subset is executed in `tests/test_excel_data_driven.py`, keeping test execution fast while leaving the remaining rows for future automation expansion.

### 2. Data Driven Testing (CSV & Excel)
- **CSV Data Provider** (`utils/csv_data_provider.py`): Parametrizes login tests using `@pytest.mark.parametrize` over `test_data/login_data.csv`.
- **Excel Data Provider** (`utils/excel_data_provider.py`): Uses `openpyxl` to parse `.xlsx` files into dictionaries.

### 3. Simple Keyword Driven Testing
- **Helper** (`utils/keyword_actions.py`): Maps high-level keywords (`OPEN`, `CLICK`, `FILL`, `SEARCH`, `ADD_TO_CART`, `LOGOUT`) directly to Page Object locator calls.
- **Test File** (`tests/test_keyword_driven.py`): Demonstrates executing a sequence of keyword steps.

### 4. BDD (Behavior-Driven Development)
- **Feature File** (`features/login.feature`): Written in standard Gherkin format (`Given`, `When`, `Then`).
- **Step Definitions** (`tests/step_definitions/test_login_steps.py`): Binds Gherkin steps to Page Objects using `pytest-bdd`.

### 5. Randomization
- Demonstrates dynamic test execution using Python's `random` module in `tests/test_product_purchase.py`:
  1. Opens Products page.
  2. Selects a random product dynamically (`random.randint`).
  3. Opens details, adds it to cart, and asserts cart contents.

### 6. Cross-Browser Execution (Chromium & Firefox)
- Handled cleanly via `conftest.py` with `--browser chromium` and `--browser firefox` flags.

### 7. Jenkins CI/CD Pipeline
- Defined in `Jenkinsfile` with 4 declarative stages:
  1. **Checkout Code**
  2. **Install Dependencies**
  3. **Install Playwright Browsers**
  4. **Run Pytest** (Generates `test-results.xml` JUnit reports)

### 8. GitHub Actions CI/CD Workflow
- Defined in `.github/workflows/playwright-tests.yml`.
- Automatically triggers test execution on `push` or `pull_request` across both Chromium and Firefox.

---

## 🔮 Future Enhancements (Future Scope)
- Automate remaining Excel test cases from `test_data/test_cases.xlsx`.
- Add Webkit / Safari browser support.
- Add API testing integration.
- Add Allure HTML reporting integration.
- Add parallel test execution using `pytest-xdist`.




