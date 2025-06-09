#  API Test with Python

Этот проект демонстрирует простой автотест публичного API с использованием библиотеки `requests`.

###  Содержимое:
- `test_api.py` — тестирует:
  - доступность API по URL `https://jsonplaceholder.typicode.com/posts`
  - корректный статус ответа `200 OK`
  - структуру: должен быть список
  - количество записей: должно быть ровно 100

---

###  Как запустить

Убедись, что установлен Python и библиотека `requests`.

```bash
pip install requests
python test_api.py
