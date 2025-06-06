import requests


def test_invalid_url_status_code():
    url = "https://jsonplaceholder.typicode.com/badlink"
    response = requests.get(url)
    assert response.status_code == 404


def test_non_json_response():
    url = "https://jsonplaceholder.typicode.com/404"
    response = requests.get(url)
    try:
        response.json()
        assert True  # если не упало — ок
    except ValueError:
        assert False, "❌ Ответ не в формате JSON"


def test_empty_data_check():
    url = "https://jsonplaceholder.typicode.com/badlink"
    response = requests.get(url)
    data = response.text
    assert data == '{}', "❌ Ожидалось пустое тело '{}'"
