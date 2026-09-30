"""
Спільні фікстури для всіх тестів.
pytest автоматично знаходить цей файл, імпортувати його не треба.

Фікстури `page`, `browser`, `context` та `base_url` дає плагін pytest-playwright.
"""
import pytest
import requests

AD_DOMAINS = ("googlesyndication", "doubleclick", "googleadservices", "adservice")


@pytest.fixture(autouse=True)
def block_ads(page):
    """На automationexercise.com багато реклами, яка перекриває кнопки.
    Блокуємо запити до рекламних доменів, щоб тести не були flaky."""
    def handle(route):
        if any(domain in route.request.url for domain in AD_DOMAINS):
            route.abort()
        else:
            route.continue_()

    page.route("**/*", handle)
    yield


@pytest.fixture(scope="session")
def api_url(base_url):
    return f"{base_url}/api"


@pytest.fixture(scope="session")
def api_session():
    """Одна HTTP-сесія на весь прогін тестів."""
    session = requests.Session()
    yield session
    session.close()
