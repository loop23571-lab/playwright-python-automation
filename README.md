# Playwright Python Automation Framework

An end-to-end (E2E), API, and database test automation framework built with **Python 3.12**, **Playwright**, and **Pytest**. This repository demonstrates a structured progression from foundational UI automation to a scalable **Page Object Model (POM)** architecture, parameterized test execution, backend **SQLite** database validation, and automated **GitHub Actions** CI/CD with HTML reporting and failure trace capture.

---

## What Has Been Built So Far

* **Foundational UI & API Automation:** Built initial login, checkout, and API validation test suites (`test_day1_login.py`, `test_day2_checkout.py`, `test_api.py`).
* **Page Object Model (POM) Refactor:** Encapsulated UI locators and page workflows into reusable page classes (`pages/login_page.py`, `pages/inventory_page.py`, `pages/checkout_page.py`), keeping test modules clean and focused on assertions (`test_login_pom.py`, `test_e2e_pom.py`).
* **Data-Driven Testing:** Implemented `@pytest.mark.parametrize` (`test_login_parameterized.py`) to run multiple credential and validation scenarios through a unified test flow.
* **Hybrid UI + SQLite Backend Validation:** Created `db_helper.py` to query and verify SQLite database state alongside UI checkout and user flows (`test_database_validation.py`, `test_checkout_db_validation.py`).
* **CI/CD Pipeline & Failure Diagnostics:** Configured `.github/workflows/playwright.yml` to run automated Pytest suites on GitHub Actions, generate self-contained HTML reports, and capture Playwright `.zip` trace files on failures for step-by-step debugging.

---

## Project Structure

```text
playwright-python-automation/
├── .github/
│   └── workflows/
│       └── playwright.yml                 # GitHub Actions CI/CD workflow
├── pages/
│   ├── __init__.py
│   ├── login_page.py                      # Login page locators and actions
│   ├── inventory_page.py                  # Inventory page locators and actions
│   └── checkout_page.py                   # Checkout page locators and actions
├── tests/
│   ├── __init__.py
│   ├── test_api.py                        # API validation tests
│   ├── test_day1_login.py                 # Foundational login UI tests
│   ├── test_day2_checkout.py              # Foundational checkout UI tests
│   ├── test_login_pom.py                  # POM-based login tests
│   ├── test_login_parameterized.py        # Data-driven login validation tests
│   ├── test_e2e_pom.py                    # End-to-end POM user flow tests
│   ├── test_database_validation.py        # SQLite database verification tests
│   └── test_checkout_db_validation.py     # Hybrid E2E checkout + SQLite tests
├── db_helper.py                           # SQLite connection and query helpers
├── requirements.txt                       # Python dependencies
└── README.md

```

---

## Prerequisites

* **Python 3.12+**
* **pip**
* **Git**

---

## Setup & Installation

1. **Clone the repository:**
```bash
git clone https://github.com/loop23571-lab/playwright-python-automation.git
cd playwright-python-automation

```


2. **Create and activate a virtual environment:**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

```


3. **Install dependencies and Playwright browser binaries:**
```bash
pip install -r requirements.txt
playwright install chromium

```



---

## Running Tests

* **Run the full test suite (headless):**
```bash
pytest

```


* **Run tests in headed mode (visible browser):**
```bash
pytest --headed

```


* **Run specific test suites:**
```bash
pytest tests/test_e2e_pom.py
pytest tests/test_login_parameterized.py
pytest tests/test_checkout_db_validation.py
pytest tests/test_api.py

```


* **Generate a self-contained HTML report:**
```bash
pytest --html=reports/report.html --self-contained-html

```



---

## Debugging Failure Traces

When a test fails, Playwright saves a trace archive (`.zip`) containing DOM snapshots, action timelines, network requests, and console logs. Open any trace file locally using Playwright Trace Viewer:

```bash
playwright show-trace reports/traces/<trace_file>.zip

```

---

## CI/CD Pipeline

Automated test execution is configured in `.github/workflows/playwright.yml`. On repository pushes and pull requests, GitHub Actions:

1. Sets up Python 3.12 and installs dependencies from `requirements.txt`.
2. Installs Playwright Chromium and required system dependencies (`playwright install --with-deps chromium`).
3. Executes the Pytest suite and generates the HTML report.
4. Archives the HTML report and failure trace `.zip` files as workflow artifacts for inspection.

---

## Next Planned Enhancements

* [ ] Session authentication state caching (`storage_state`) to bypass repetitive UI login steps
* [ ] Parallel test execution using `pytest-xdist`
* [ ] Network interception and API response mocking (`page.route`) for error-state coverage
