"""
Приклад першого UI-тесту. Далі тести пишеш ти сам (див. CLAUDE.md).
"""
import pytest
from playwright.sync_api import expect

from pages.base_page import BasePage


@pytest.mark.smoke
@pytest.mark.ui
def test_home_page_opens(page):
    home = BasePage(page).open()
    home.should_have_title("Automation Exercise")
    expect(page.locator("#slider")).to_be_visible()
