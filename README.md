# AutomationExercise Playwright POM Framework

A beginner-friendly, end-to-end UI automation testing project using **Python**, **Playwright (Sync API)**, **Pytest**, and **Page Object Model (POM)** targetting [AutomationExercise.com](https://automationexercise.com/).

---

## 💡 What is Page Object Model (POM)?

**Page Object Model (POM)** is a design pattern used in software testing where web pages are represented as Python classes.

- **Locators & Page Actions** live inside Page classes (`pages/home_page.py`, `pages/login_page.py`, etc.).
- **Tests** call page methods (`login_page.enter_email(...)`) rather than writing raw Playwright locators (`page.locator(...)`).

### 🔄 Java Selenium vs Python Playwright Comparison

| Concept | Java Selenium | Python Playwright |
|---|---|---|
| **Element Search & Action** | `driver.findElement(By.id("email")).sendKeys("abc");` | `page.locator("#email").fill("abc")` |
| **Element Click** | `driver.findElement(By.id("login")).click();` | `page.locator("#login").click()` |
| **Test Annotation / Runner** | `@Test` (TestNG / JUnit) | `def test_login():` (Pytest) |
| **Browser Setup** | `WebDriver driver = new ChromeDriver();` | `browser = playwright.chromium.launch()` |
| **Data Provider** | `@DataProvider` (TestNG) | `@pytest.mark.parametrize` |

---

## 📁 Project Structure

```
AutomationExercise_Playwright/
│
├── pages/                  # Page Object classes (one per web page)
│   ├── base_page.py        # Parent class with reusable actions (click, fill, navigate)
│   ├── home_page.py        # Home page locators and actions
│   ├── login_page.py       # Login & signup page locators and actions
│   ├── products_page.py    # Product catalog and search page
│   └── cart_page.py        # Shopping cart view and checkout
│
├── tests/                  # Test suites
│   ├── test_login.py               # Login tests & CSV data-driven login test
│   └── test_product_purchase.py    # End-to-end product search and purchase test
│
├── utils/                  # Helper utilities
│   ├── browser_factory.py  # Utility for launching Playwright browser instances
│   └── csv_data_provider.py# Utility to read CSV files for data-driven testing
│
├── test_data/              # External data files
│   └── login_data.csv      # CSV file containing test credentials
│
├── screenshots/            # Failure screenshots directory (auto-created on failure)
├── conftest.py             # Pytest fixtures and browser setup/teardown
├── pytest.ini              # Pytest default options & discovery configuration
├── requirements.txt        # Python package dependencies
└── README.md               # Project guide and documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.8 or higher installed on your system.

### 2. Installation
Open a terminal in the project root directory and run:

```bash
# Install dependencies
pip install -r requirements.txt

# Install Playwright browser binaries (Chromium, Firefox, WebKit)
playwright install
```

---

## 🧪 Running Tests

### Run all tests in Headless Mode (Default)
```bash
pytest
```

### Run tests in Headed Mode (Watch browser UI live)
```bash
pytest --headed
```

### Run a specific test file
```bash
pytest tests/test_login.py
```

### Run tests with verbose output
```bash
pytest -v
```

---

## 📸 Failure Screenshots

If any test fails during execution, `conftest.py` automatically captures a screenshot of the browser page at the moment of failure and saves it in the `screenshots/` directory with the format:

```
screenshots/<test_name>_failure.png
```

---

## 📊 CSV Data-Driven Testing

The framework uses `utils/csv_data_provider.py` to parse CSV files in `test_data/`. Pytest's `@pytest.mark.parametrize` decorates test functions to run the same test against multiple data rows automatically.
