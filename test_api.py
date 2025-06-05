import requests

print("🚀 Старт теста...")


def test_get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"🌐 Запрос отправлен на {url}")
    print(f"📦 Код ответа: {response.status_code}")

    # Проверка: статус должен быть 200
    assert response.status_code == 200, "❌ Статус не 200!"

    data = response.json()
    print(f"📄 Получено записей: {len(data)}")

    # Проверка: это список
    assert isinstance(data, list), "❌ Ответ не список!"
    # Проверка: 100 записей
    assert len(data) == 100, "❌ Не 100 постов в ответе!"

    print("✅ Всё прошло успешно!")


# Вызов функции
test_get_posts()
