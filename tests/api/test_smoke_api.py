"""
Приклад першого API-тесту.
Список усіх ендпоінтів: https://automationexercise.com/api_list
Особливість цього API: HTTP-статус майже завжди 200,
а реальний код відповіді лежить у полі "responseCode" в JSON.
"""
import pytest


@pytest.mark.smoke
@pytest.mark.api
def test_get_products_list(api_session, api_url):
    response = api_session.get(f"{api_url}/productsList")

    assert response.status_code == 200
    body = response.json()
    assert body["responseCode"] == 200
    assert len(body["products"]) > 0
