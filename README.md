
# Playwright Python Automation Framework

A scalable, data-driven, and CI/CD-integrated End-to-End (E2E) test automation framework built with **Python 3.12**, **Playwright**, **Pytest**, and **SQLite**. 

This project implements modern automation design patterns including the **Page Object Model (POM)**, parameterized data-driven testing, and hybrid UI-to-database assertions.

---

## 🏗️ Project Architecture & Structure

```text
playwright-python-automation/
├── .github/
│   └── workflows/
│       └── playwright.yml      # GitHub Actions CI/CD pipeline configuration
├── pages/
│   ├── __init__.py
│   ├── login_page.py           # Page Object: Login functionality & locators
│   ├── inventory_page.py       # Page Object: Product catalog & cart actions
│   └── checkout_page.py        # Page Object: Shipping and order completion
├── tests/
│   ├── test_login_parameterized.py # Data-driven login tests using @pytest.mark.parametrize
│   └── test_checkout_db_validation.py # Hybrid E2E test combining UI workflow & SQL assertions
├── db_helper.py                # SQLite database helper for seeding and backend verification
├── requirements.txt            # Project dependencies
└── README.md

```

---

## 🛠️ Core Capabilities & Design Patterns

1. **Page Object Model (POM):** Decouples test scripts from UI locators and page interactions, ensuring high maintainability and modularity across test suites.
2. **Data-Driven Testing (DDT):** Leverages `@pytest.mark.parametrize` to execute single test logic across multiple datasets (e.g., valid credentials, locked-out users, invalid states) with automatic test isolation.
3. **Backend Database Validation (SQLite):** Integrates custom SQL helpers (`db_helper.py`) to seed test data and verify transaction integrity at the database layer immediately following UI workflows.
4. **Cloud CI/CD Pipeline (GitHub Actions):** Automatically provisions an Ubuntu virtual environment, installs Python and Playwright browser binaries, and executes the full test suite on every `push` or `pull_request` to `main`.

---

## ⚙️ Getting Started Locally

### 1. Clone the Repository

```bash
git clone [https://github.com/loop23571-lab/playwright-python-automation.git](https://github.com/loop23571-lab/playwright-python-automation.git)
cd playwright-python-automation

```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# On Windows (PowerShell):
.\venv\Scripts\Activate
# On macOS/Linux:
source venv/bin/activate

```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install

```

---

## 🚀 Running the Tests

* **Run all tests (headless mode):**
```bash
python -m pytest -v

```


* **Run tests in headed mode with slow motion (great for debugging):**
```bash
python -m pytest --headed --slowmo 300 -v

```


* **Run a specific test file:**
```bash
python -m pytest tests/test_login_parameterized.py -v --headed

```



---

## 🔄 CI/CD Workflow (`playwright.yml`)

The automated pipeline triggers on every push to the main branch, executing the following steps:

1. Checks out repository code.
2. Sets up Python 3.12 with pip caching enabled.
3. Installs project dependencies from `requirements.txt`.
4. Installs Playwright system dependencies and browser binaries.
5. Executes the `pytest` test suite and reports status.

```

```
