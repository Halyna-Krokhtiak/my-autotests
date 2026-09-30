# UI & API Autotests for automationexercise.com

Test automation project built with **Python**, **pytest**, **Playwright** and **requests**.

## Tech stack
- Python 3.12
- pytest
- Playwright
- requests (API testing)
- Allure / pytest-html reports
- GitHub Actions (CI)
- Page Object Model

## Test coverage
<!-- TODO: заповни, коли напишеш тести -->
| Area | Type | Tests |
|------|------|-------|
| Home page | UI | smoke |
| Products API | API | smoke |

## How to run
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium

pytest                           # all tests
pytest -m smoke                  # smoke only
pytest tests/api                 # API only
pytest --headed                  # see the browser
```

## Allure report
```bash
allure serve allure-results
```

## CI
Tests run automatically on every push via GitHub Actions.
Reports are available in the **Actions → run → Artifacts** section.
