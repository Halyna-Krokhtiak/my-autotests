"""
Базовий клас для всіх сторінок (Page Object Model).
Усі інші сторінки наслідуються від нього: class LoginPage(BasePage).
"""
from playwright.sync_api import Page, expect


class BasePage:
    path = "/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.path)
        return self

    def should_have_title(self, text: str):
        expect(self.page).to_have_title(text)
