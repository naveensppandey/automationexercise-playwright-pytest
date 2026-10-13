# AutomationExercise Playwright POM Framework

A beginner-friendly, production-grade UI automation framework built using **Python**, **Playwright**, **pytest**, **Page Object Model (POM)**, **Data-Driven Testing (CSV & Excel)**, **Keyword-Driven Testing**, **BDD (pytest-bdd)**, **Hierarchical Randomized Testing**, and **Automated Excel Reporting**.

---

## 📌 Project Overview
This project provides end-to-end test automation for [AutomationExercise](https://automationexercise.com/). 

### Key Highlights
1. **All 50 Excel Test Cases Automated (`TC01`–`TC50`)**: Every single test case defined in `test_data/test_cases.xlsx` is implemented across modular test suites and achieves a **100% Pass Rate**.
2. **Automated Excel Execution Report**: A custom pytest session reporter generates `reports/execution_results.xlsx` containing all 50 test cases with their `Test Case ID`, `Module`, `Test Steps`, `Expected Result`, `Execution Status` (`PASS`/`FAIL`), and `Actual Result`.
3. **Preserved 3-Level Hierarchical Product Randomization**: Fully preserves the dependent dynamic chain:
   - **Level 1**: Discovers and selects a random category (`Women`, `Men`, `Kids`)
   - **Level 2**: Discovers and selects a random subcategory belonging to the chosen category
   - **Level 3**: Discovers and selects a random product from that specific subcategory catalog
   - **Cart & Logout**: Adds the chosen product to cart, asserts its presence in cart, and cleanly logs out.
4. **Data-Driven & Multi-Pattern Coverage**: Supports CSV login data-driven execution, keyword-driven execution, and BDD (Gherkin) execution.

---

## 📁 Project Structure

```
AutomationExercise_Playwright/
│
├── .github/
│   └── workflows/
│       └── playwright-tests.yml       # GitHub Actions CI/CD Workflow
│
├── features/
│   └── login.feature                  # BDD Feature File (Gherkin format)
│
├── pages/                             # Page Object Model Classes
│   ├── base_page.py                   # Reusable Playwright actions (click, fill, navigate)
│   ├── home_page.py                   # Home page, navbar, scroll & footer subscription
│   ├── login_page.py                  # Login, logout, signup initial forms & error handling
│   ├── signup_page.py                 # Full registration fields, country dropdown, delete account
│   ├── contact_us_page.py             # Contact form, file upload & alert dialog handling
│   ├── products_page.py               # Search, accordion, category navigation & randomization
│   └── cart_page.py                   # Shopping cart verification, quantity & checkout
│
├── reports/
│   └── execution_results.xlsx         # Generated Excel Test Execution Report (50 Cases)
│
├── screenshots/                       # Automated failure screenshots directory
│
├── test_data/                         # Test Data Files
│   ├── login_data.csv                 # CSV test accounts for data-driven testing
│   ├── test_cases.xlsx                # Master 50-test-case Excel repository
│   └── sample_upload.txt              # Sample file for file upload testing (TC46)
│
├── tests/                             # Modular Pytest Suites
│   ├── step_definitions/
│   │   └── test_login_steps.py        # BDD step definitions using pytest-bdd
│   ├── test_login.py                  # TC01–TC10 + CSV data-driven login test
│   ├── test_products.py               # TC11–TC14, TC16–TC25 (Search, Catalog, Accordion)
│   ├── test_cart.py                   # TC29–TC36 (Cart navigation, quantity, headers)
│   ├── test_excel_cases.py            # TC37–TC49 (Signup, Delete Account, Contact Us, Home)
│   ├── test_randomization.py          # TC15, TC26–TC28, TC50 (3-Level Randomization Chain)
│   ├── test_keyword_driven.py         # Keyword-Driven test execution
│   └── test_product_purchase.py       # Preserved E2E purchase & randomization test
│
├── utils/                             # Utilities & Data Providers
│   ├── csv_data_provider.py           # Reads CSV data & random valid user helper
│   ├── excel_data_provider.py         # Reads Excel test data with openpyxl
│   └── keyword_actions.py             # Action router for keyword-driven testing
│
├── conftest.py                        # Fixtures, ad-blocking, screenshot hook & Excel report generator
├── Jenkinsfile                        # Jenkins CI/CD Pipeline definition
├── pytest.ini                         # Pytest configuration & test markers
├── README.md                          # Framework documentation
└── requirements.txt                   # Project dependencies
```

---

## 📊 Test Case Coverage Mapping (50 Test Cases)

| Module | Test Case IDs | Test File | Description | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Login** | TC01 – TC10 | `tests/test_login.py` | Navigation, Valid Login, Invalid Email/Pass, Blank Fields, Logout, 'Logged in as', CSV Users 1–3 | **PASS** (10/10) |
| **Products** | TC11 – TC14, TC16 – TC20 | `tests/test_products.py` | Navigate Products, Search 'dress', Non-existent Search, View Details, Add 1st & 2nd Item, Search 'Top'/'Jeans', All Products Header | **PASS** (9/9) |
| **Category** | TC21 – TC25 | `tests/test_products.py` | Expand Women/Men/Kids, Select Women Dress, Select Men Tshirts | **PASS** (5/5) |
| **Randomization** | TC15, TC26 – TC28, TC50 | `tests/test_randomization.py` | Random Product, Random Category, Random Subcategory, 3-Level Dynamic Chain, Full E2E Randomization Flow | **PASS** (5/5) |
| **Cart** | TC29 – TC36 | `tests/test_cart.py` | Navbar Cart, Modal Cart, Verify Name, Verify Table Headers, Checkout Button, Quantity, Empty Cart, Multiple Products | **PASS** (8/8) |
| **Signup** | TC37 – TC43 | `tests/test_excel_cases.py` | Initial Signup, Existing Email Error, Dynamic Account Creation, Delete Account Flow, HTML5 Blank Validation, Country Dropdown ('India'), Gender Radio ('Mr.') | **PASS** (7/7) |
| **Contact Us** | TC44 – TC46 | `tests/test_excel_cases.py` | Navigate Contact Us, Submit Contact Form with Alert Dialog, File Upload Attachment | **PASS** (3/3) |
| **Home** | TC47 – TC49 | `tests/test_excel_cases.py` | Logo Verification, Scroll Bottom & Top, Footer Subscription | **PASS** (3/3) |
| **Total** | **TC01 – TC50** | **All Test Suites** | **50 Out of 50 Automated Scenarios** | **100% PASS** |

---

## 🎲 3-Level Hierarchical Randomization Logic

The framework avoids hardcoding selectors for product purchases by implementing true DOM discovery at runtime:

```
[Random User from CSV]
        │
        ▼
[Level 1: Category] ──► Discovers #accordian .panel elements ──► Picks random Category (e.g., "Men")
        │
        ▼
[Level 2: Subcategory] ─► Discovers child links in that panel ──► Picks random Subcategory (e.g., "Tshirts")
        │
        ▼
[Level 3: Product] ────► Discovers .product-image-wrapper cards ─► Picks random Product (e.g., "Men Tshirt")
        │
        ▼
[Cart & Logout] ───────► Adds to cart ──► Asserts item in /view_cart ──► Logs out cleanly
```

This guarantees test stability regardless of changes in product inventory while verifying real end-to-end user journeys.

---

## 🛠️ Setup & Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/naveensppandey/automationexercise-playwright-pytest.git
   cd AutomationExercise_Playwright
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright Browsers**:
   ```bash
   playwright install chromium
   ```

---

## 🧪 How to Run Tests

### 1. Run Complete Test Suite (All 50 Cases)
```bash
pytest -v
```

### 2. Run Individual Modules
```bash
# Run Login Tests (TC01 - TC10)
pytest tests/test_login.py -v

# Run Product & Category Tests (TC11 - TC14, TC16 - TC25)
pytest tests/test_products.py -v

# Run Cart Tests (TC29 - TC36)
pytest tests/test_cart.py -v

# Run Signup, Contact Us & Home Tests (TC37 - TC49)
pytest tests/test_excel_cases.py -v

# Run Randomization Suite (TC15, TC26 - TC28, TC50)
pytest tests/test_randomization.py -v
```

### 3. Run in Headed Mode
```bash
pytest -v --headed
```

### 4. Run on Firefox
```bash
pytest -v --browser firefox
```

---

## 📈 Excel Execution Report

Every pytest run automatically updates **`reports/execution_results.xlsx`** with:
- **Test Case ID** (`TC01`–`TC50`)
- **Module** (`Login`, `Products`, `Category`, `Cart`, `Signup`, `Contact Us`, `Home`, `End-to-End`)
- **Test Case Name** & **Test Steps**
- **Expected Result** & **Actual Result**
- **Execution Status** (Styled in Green for `PASS`, Red for `FAIL`)
- **Screenshot Path** (Auto-populated if any test fails)

---

## 👨‍💻 Author & Contribution
- **Framework Owner**: Naveen Pandey
- **Repository**: [automationexercise-playwright-pytest](https://github.com/naveensppandey/automationexercise-playwright-pytest.git)
- **Framework Architecture**: Python + Playwright + Pytest + POM + openpyxl + pytest-bdd
