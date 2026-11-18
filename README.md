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
