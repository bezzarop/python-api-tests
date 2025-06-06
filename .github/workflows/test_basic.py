import requests


def test_multiplication()


multiply_numbers = 5 * 4
assert multiply_numbers == 20

# Задание 2


def test_api_returns_list()


url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()
assert isinstance(data, list)

# задание 3


def test_content_type()


url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
contetnt_type = response.get(url)
assert сontent_type == 'application/json; charset=utf-8'

# задание 4


def test_example_com_json_fail():
    url = "https://example.com"
    response = requests.get(url)
    try:
        data = response.json()
        assert True  # если вдруг получится (но не должно)
    except ValueError:
        assert True  # всё ок, мы ожидали ошибку
