# SauceDemo Test Automation Framework

Professional test automation framework for saucedemo.com using Playwright with Python and Page Object Model design pattern.

## Project Overview

This framework demonstrates advanced test automation practices including:
- Page Object Model (POM) architecture
- Cross-browser testing capabilities
- Comprehensive test reporting with screenshots
- CI/CD ready configuration
- Professional documentation

## Test Coverage

### Functional Requirements Covered:
- TEST_001: Successful login with valid credentials
- TEST_002: Error message validation for invalid credentials
- TEST_003: Product cart functionality and count validation
- TEST_004-006: Browser size impact analysis (additional finding)

### Key Findings Documented:
- UI rendering issue discovered: Cart badge visibility differs between browser sizes
- Functional tests pass but visual user experience varies
- Demonstrates importance of visual validation alongside automation

## Technical Stack

- Framework: Playwright with Python
- Design Pattern: Page Object Model (POM)
- Test Runner: pytest
- Reporting: HTML reports + Screenshot documentation
- CI/CD: GitHub Actions ready

## Project Structure

saucedemotesting/
├── pages/                 # Page Object classes
│   ├── login_page.py
│   └── inventory_page.py
├── tests/                 # Test suites
│   ├── test_saucedemo.py              # Normal browser tests
│   └── test_saucedemo_maximized.py    # Maximized browser tests
├── utilities/             # Configuration and helpers
│   └── config_reader.py
├── test-output/           # Screenshots and evidence
├── playwright.config.js   # Playwright configuration
├── requirements.txt       # Python dependencies
└── README.md             # This file

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd saucedemotesting

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install

Running Tests
# Run all tests in normal browser
pytest tests/test_saucedemo.py --headed -v

# Run all tests in maximized browser
pytest tests/test_saucedemo_maximized.py --headed -v

# Run specific test
pytest tests/test_saucedemo.py::TestSauceDemo::test_successful_login_and_product_display --headed -v -s

I used Chat-gpt 3.5 as my LLM for assistance on the following:

Verification of the project structure setup.

Code syntax verification.

For verification of the cart icon bug I found on the different window size of the browser.

Key technical decisions I took were as below -
1. I used the Page Object Model (POM) structure for maintainability.

2. Separated the test files for different browser configurations.

3. Following a systematic screenshot naming for evidence.

4. A comprehensive error handling and validation
