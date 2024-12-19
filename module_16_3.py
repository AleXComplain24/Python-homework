from fastapi import FastAPI, HTTPException, Path
from typing import Annotated

# Создание объекта FastAPI
app = FastAPI()

# Инициализация словаря пользователей
users = {"1": "Имя: Example, возраст: 18"}

# GET-запрос: Получение всех пользователей
@app.get("/users")
def get_users():
    return users

# POST-запрос: Добавление нового пользователя
@app.post("/user/{username}/{age}")
def create_user(
    username: Annotated[
        str,
        Path(title="Enter username", min_length=5, max_length=20, example="UrbanUser")
    ],
    age: Annotated[
        int,
        Path(title="Enter age", ge=18, le=120, example=24)
    ],
):
    # Получение нового user_id
    new_user_id = str(max(map(int, users.keys())) + 1)
    # Добавление нового пользователя
    users[new_user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_user_id} is registered"

# PUT-запрос: Обновление информации о пользователе
@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: Annotated[
        str,
        Path(title="Enter User ID", example="1")
    ],
    username: Annotated[
        str,
        Path(title="Enter username", min_length=5, max_length=20, example="UrbanProfi")
    ],
    age: Annotated[
        int,
        Path(title="Enter age", ge=18, le=120, example=28)
    ],
):
    # Проверка, существует ли пользователь
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    # Обновление информации
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

# DELETE-запрос: Удаление пользователя
@app.delete("/user/{user_id}")
def delete_user(
    user_id: Annotated[
        str,
        Path(title="Enter User ID", example="2")
    ]
):
    # Проверка, существует ли пользователь
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    # Удаление пользователя
    del users[user_id]
    return f"User {user_id} has been deleted"
