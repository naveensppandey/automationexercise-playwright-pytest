# 🛍️ AutomationExercise Playwright Python Automation Framework

A clean, beginner-friendly UI test automation framework built using **Python**, **Playwright**, and **pytest**, following the **Page Object Model (POM)** design pattern. 

This project automates end-to-end testing for the [AutomationExercise](https://automationexercise.com/) e-commerce web application, covering **all 50 test cases** from `test_data/test_cases.xlsx` along with a **3-level dynamic product randomization test**.

---

## 📖 Table of Contents
1. [Project Overview](#-project-overview)
2. [Why Playwright? (Playwright vs Selenium)](#-why-playwright-playwright-vs-selenium)
3. [Pytest Basics](#-pytest-basics)
4. [Page Object Model (POM) Architecture](#-page-object-model-pom-architecture)
5. [Project Folder & File Structure](#-project-folder--file-structure)
6. [Prerequisites & Installation](#-prerequisites--installation)
7. [How to Run Tests](#-how-to-run-tests)
8. [Mapping of All 50 Excel Test Cases](#-mapping-of-all-50-excel-test-cases)
9. [The 3-Level Randomization Flow](#-the-3-level-randomization-flow)
10. [Step-by-Step Test Execution Flow](#-step-by-step-test-execution-flow)
11. [College Viva & Interview Questions & Answers](#-college-viva--interview-questions--answers)

---

## 📌 Project Overview

This framework is designed for clarity, maintainability, and educational presentation. It provides:
- **100% Automation Coverage**: All 50 test cases defined in the project Excel sheet (`test_data/test_cases.xlsx`) are implemented and automated.
- **Data-Driven Testing (DDT)**: Validates multiple user credentials using `test_data/login_data.csv`.
- **Dynamic 3-Level Randomization**: Eliminates hardcoded test flows by discovering available categories, subcategories, and products directly from the live DOM at runtime.
- **Robust Execution**: Includes built-in handling for third-party ad blocking and dynamic modal popups.
- **Standard Pytest Terminal Output**: Clean, native pytest output showing test names, pass/fail status, and execution times without any third-party reporting overhead.

---

## ⚡ Why Playwright? (Playwright vs Selenium)

| Feature | Playwright | Selenium |
| :--- | :--- | :--- |
| **Speed & Performance** | Extremely fast; runs over Chrome DevTools Protocol / WebSockets. | Slower; communicates via HTTP JSON Wire Protocol / WebDriver. |
| **Auto-Waiting** | Automatically waits for elements to be visible, enabled, and stable before acting. No manual `time.sleep()`. | Requires explicit waits (`WebDriverWait`) or risks flaky `NoSuchElementException`. |
| **Browser Architecture** | Single browser instance can isolate tests using lightweight **Browser Contexts** (like incognito tabs) in milliseconds. | Opening a new browser window requires launching a fresh, heavy process. |
| **Network Interception** | Native network routing to block slow ads or mock API responses (`context.route`). | Requires third-party proxies (e.g. BrowserMob Proxy) or complex CDP wrappers. |
| **Setup Simplicity** | Bundles browser binaries via one command (`playwright install`). No manual ChromeDriver downloads. | Requires matching browser drivers (ChromeDriver, GeckoDriver) to exact browser versions. |

---

## 🧪 Pytest Basics

[pytest](https://docs.pytest.org/) is the test runner used in this framework:
1. **Automatic Discovery**:
   - Pytest searches for files matching `test_*.py`.
   - Inside those files, it executes every function starting with `test_*()`.
2. **Configuration (`pytest.ini`)**:
   - Sets default command-line flags (e.g. `-v` for verbose output).
   - Points pytest to the `tests/` directory.
   - Disables `.pytest_cache` to keep the project folder clean.
3. **Fixtures (`conftest.py`)**:
   - The `@pytest.fixture` named `page` handles browser setup before each test and teardown after each test.
   - Using `yield`, setup code runs first, the test executes, and cleanup runs automatically when the test finishes.
4. **Simple Assertions**:
   - Uses standard Python `assert condition, "Error message"` syntax instead of complex assertion libraries.

---

## 🏗️ Page Object Model (POM) Architecture

The **Page Object Model** is an industry-standard design pattern where each web page has a corresponding Python class.

### Why POM?
- **Separation of Concerns**: Test files focus only on *assertions* and *business logic*. Page classes focus on *locators* and *user interactions*.
- **Code Reusability**: If the "Login" button changes on the website, we only update it in `pages/login_page.py`. All tests using that button will immediately work without changes.
- **Readability**: Tests read like human instructions:
  ```python
  login_page.navigate()
  login_page.login("user@example.com", "Password123")
  assert login_page.is_logged_in_as("User Name")
  ```

### Architecture Diagram
```
                     ┌───────────────────────┐
                     │     Pytest Tests      │
                     │  (tests/test_*.py)    │
                     └───────────┬───────────┘
                                 │ Calls action methods & asserts results
                                 ▼
                     ┌───────────────────────┐
                     │     Page Objects      │
                     │  (pages/*_page.py)    │
                     └───────────┬───────────┘
                                 │ Inherits reusable click/fill/navigate
                                 ▼
                     ┌───────────────────────┐
                     │       BasePage        │
                     │  (pages/base_page.py) │
                     └───────────┬───────────┘
                                 │ Controls browser
                                 ▼
                     ┌───────────────────────┐
                     │    Playwright API     │
                     └───────────────────────┘
```

---

## 📁 Project Folder & File Structure

```
AutomationExercise_Playwright/
│
├── .vscode/
│   └── settings.json                  # Editor settings (Python interpreter path)
│
├── pages/                             # Page Object Model classes
│   ├── base_page.py                   # Reusable base wrapper (navigate, click, fill, is_visible)
│   ├── home_page.py                   # Home page, navbar, scroll to top/bottom, contact form, subscribe
│   ├── login_page.py                  # Login, logout, signup forms, validation messages, delete account
│   ├── products_page.py               # Products catalog, search, category accordion, dynamic randomization
│   └── cart_page.py                   # Cart table, product items, quantity checks, proceed to checkout
│
├── test_data/                         # External test data files
│   ├── login_data.csv                 # CSV users with email, password, and expected result
│   ├── sample_upload.txt              # Sample text file used for contact us file upload (TC46)
│   └── test_cases.xlsx                # Master Excel repository containing all 50 test cases
│
├── tests/                             # Test suites (Pytest)
│   ├── test_login.py                  # TC01–TC10 (Login/Logout), TC37–TC43 (Signup), and CSV data-driven test
│   ├── test_products.py               # TC11–TC14, TC16–TC25 (Products/Search/Category) & TC44–TC49 (Contact/Home)
│   ├── test_cart.py                   # TC29–TC36 (Cart operations, quantity, modal popup, checkout)
│   └── test_randomization.py          # TC15, TC26–TC28, TC50 (3-level dynamic category-product randomization)
│
├── utils/                             # Helper utilities
│   ├── csv_data_provider.py           # Reads CSV test data & randomly selects valid credentials
│   └── excel_reader.py                # Reads test cases from Excel sheet using openpyxl
│
├── conftest.py                        # Browser fixture setup, teardown, and ad-blocking rules
├── pytest.ini                         # Pytest configuration settings
├── README.md                          # Comprehensive project documentation
└── requirements.txt                   # Minimal project dependencies
```

---

## 💻 Prerequisites & Installation

### 1. Requirements
- Python 3.9 or higher installed on your system.
- Internet connection to install packages and run tests against [AutomationExercise](https://automationexercise.com/).

### 2. Setup Steps

1. **Clone or Download the Project**:
   ```bash
   cd AutomationExercise_Playwright
   ```

2. **(Optional) Create and Activate a Virtual Environment**:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS / Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright Browsers**:
   ```bash
   playwright install chromium
   ```

---

## 🚀 How to Run Tests

Pytest provides flexible options to run test suites directly from your terminal.

### 1. Run All Tests (Standard Headless Mode)
```bash
pytest -v
```

### 2. Run Tests in Headed Mode (Watch the Browser Open)
```bash
pytest -v --headed
```

### 3. Run a Specific Test File
```bash
# Run only Login & Signup tests
pytest tests/test_login.py -v

# Run only Product & Category tests
pytest tests/test_products.py -v

# Run only Cart tests
pytest tests/test_cart.py -v

# Run only Randomization tests
pytest tests/test_randomization.py -v
```

### 4. Run a Single Test Case
```bash
# Run TC02 (Valid Login)
pytest tests/test_login.py -k "test_tc02" -v

# Run the 3-Level Randomization E2E flow
pytest tests/test_randomization.py -k "test_tc50" -v
```

### 5. Run Tests on Firefox
```bash
playwright install firefox
pytest -v --browser firefox
```

---

## 📊 Mapping of All 50 Excel Test Cases

Every test case in `test_data/test_cases.xlsx` is mapped to an automated test function:

| Category | Test Case IDs | Test File | Description |
| :--- | :--- | :--- | :--- |
| **Login & Auth** | TC01 – TC10 | `tests/test_login.py` | Navbar navigation, valid login, invalid email/pass, blank inputs, logout, "Logged in as" assertion, CSV users 1–3 |
| **Products & Search** | TC11 – TC14, TC16 – TC20 | `tests/test_products.py` | Products page navigation, search 'dress', non-existent search, view product details, add 1st & 2nd products, search 'Top' & 'Jeans', All Products header |
| **Categories** | TC21 – TC25 | `tests/test_products.py` | Expand Women/Men/Kids accordions, select Women Dress subcategory, select Men Tshirts subcategory |
| **Randomization** | TC15, TC26 – TC28, TC50 | `tests/test_randomization.py` | Pick random product, pick random category, pick random subcategory, 3-level dependent selection, full E2E random purchase |
| **Cart** | TC29 – TC36 | `tests/test_cart.py` | Cart via navbar, cart via modal popup, verify item name, verify table headers, proceed to checkout button, quantity verification, empty cart navigation, multiple products in cart |
| **Signup & Account** | TC37 – TC43 | `tests/test_login.py` | Initial signup, duplicate email error, fill full account details, delete account flow, HTML5 validation, country dropdown ('India'), gender radio button |
| **Contact Us** | TC44 – TC46 | `tests/test_products.py` | Navigate Contact Us, submit contact form with browser dialog alert, upload sample file |
| **Home Page** | TC47 – TC49 | `tests/test_products.py` | Verify brand logo, scroll to bottom and back to top, footer email subscription |

---

## 🎲 The 3-Level Randomization Flow

Instead of hardcoding a specific product like *"Blue Top"*, the framework dynamically discovers real elements on the website at runtime.

### Step-by-Step Flow (`tests/test_randomization.py::test_tc50_hierarchical_randomization_end_to_end`):
1. **Pick Random Valid User**: Randomly selects a registered user from `test_data/login_data.csv` and logs in.
2. **Level 1 (Category)**:
   - Scans the left sidebar accordions (`Women`, `Men`, `Kids`).
   - Randomly clicks one category to expand its subcategories.
3. **Level 2 (Subcategory)**:
   - Reads the visible subcategory links under the opened category (e.g., `Dress`, `Tops`, `Saree`).
   - Randomly clicks one subcategory.
4. **Level 3 (Product)**:
   - Discovers all products listed under the chosen subcategory catalog.
   - Randomly selects one product card, captures its exact title, and adds it to the cart.
5. **Cart Verification & Cleanup**:
   - Opens the cart and asserts that the exact randomly chosen product name is present in the cart table.
   - Logs out cleanly to end the session.

---

## 🔄 Step-by-Step Test Execution Flow

When you run `pytest tests/test_login.py -k "test_tc02" -v`:

1. **Initialization (`pytest.ini`)**: Pytest reads configuration settings and finds the `tests/` directory.
2. **Fixture Setup (`conftest.py`)**:
   - Playwright launches a Chromium browser process.
   - Creates an isolated `BrowserContext` with network interceptors that abort slow advertisement scripts.
   - Creates a new `Page` instance and injects it into `test_tc02_login_with_valid_credentials(page)`.
3. **Page Object Initialization**:
   - `LoginPage(page)` is created, storing element selectors and interaction methods.
4. **Action Execution (`pages/login_page.py`)**:
   - Navigates to `/login`.
   - Types user credentials into the email and password fields.
   - Clicks the `Login` button.
5. **Validation (`assert`)**:
   - Checks that the navbar displays `"Logged in as <Username>"`.
6. **Fixture Teardown (`conftest.py`)**:
   - The test finishes, and execution resumes after `yield page` in `conftest.py`.
   - The browser context and browser process are cleanly closed.
7. **Report Display**: Pytest prints `PASSED` in green in your terminal.

---

## 🎓 College Viva & Interview Questions & Answers

### 1. What is the Page Object Model (POM)?
> **Answer**: POM is a design pattern where each web page is represented as a Python class. Element locators and action methods (like clicking buttons or typing text) are kept inside the page class. Test files only contain test steps and assertions. This prevents duplication and makes the framework easy to maintain when the UI changes.

### 2. How does Playwright handle element synchronization compared to Selenium?
> **Answer**: Playwright has built-in auto-waiting. Before performing any action (like `.click()` or `.fill()`), Playwright automatically waits for the element to be visible, attached to the DOM, enabled, and stable. In Selenium, testers often need to write explicit `WebDriverWait` code or risk intermittent failures.

### 3. What is the role of `conftest.py` in pytest?
> **Answer**: `conftest.py` is a special pytest configuration file used to share fixtures and hooks across multiple test files without needing to import them. In this project, `conftest.py` provides the `page` fixture for browser launch, ad-blocking, and clean teardown.

### 4. How did you handle intrusive Google advertisements on AutomationExercise?
> **Answer**: AutomationExercise contains third-party ads that can block buttons and delay page loads. In `conftest.py`, we used Playwright's `context.route()` method to intercept and abort requests matching ad domains (such as `*doubleclick*`, `*google-analytics*`, and `*googlesyndication*`). This keeps the tests fast and reliable.

### 5. How is Data-Driven Testing (DDT) implemented in this framework?
> **Answer**: We use `@pytest.mark.parametrize` along with a custom CSV reader function in `utils/csv_data_provider.py`. The reader parses `test_data/login_data.csv` and feeds each user's email, password, and expected outcome into the test function one by one.

### 6. What makes your randomization test unique?
> **Answer**: It implements true runtime discovery across 3 dependent levels: Category → Subcategory → Product. Instead of hardcoding product names, it reads what is dynamically available in the DOM, picks an item using Python's `random.choice()`, adds it to the cart, and verifies that the exact chosen product appears in the shopping cart.

### 7. How does openpyxl work with your Excel test cases?
> **Answer**: `openpyxl` is a Python library used to read and write Excel (`.xlsx`) files. In `utils/excel_reader.py`, we load `test_data/test_cases.xlsx`, read rows from the `Sheet1` worksheet, and return the test cases as dictionaries containing the Test ID, Steps, and Expected Results.

### 8. What happens if an element is hidden behind a hover overlay?
> **Answer**: On the products page, hovering over a card displays a hover overlay that can intercept click events. We handle this reliably by using Playwright's `locator.dispatch_event("click")` or targeting the direct product card button, which triggers the DOM click event directly without being blocked by CSS overlay animations.
