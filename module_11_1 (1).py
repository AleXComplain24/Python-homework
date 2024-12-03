import requests

# 1. Выполнение GET-запроса
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(f"Статус-код: {response.status_code}")
print(f"Данные: {response.json()}")

# 2. Отправка POST-запроса
data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response_post = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print(f"Ответ на POST-запрос: {response_post.json()}")

# 3. Получение заголовков
print(f"Заголовки ответа: {response.headers}")