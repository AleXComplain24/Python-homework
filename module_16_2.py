from fastapi import FastAPI, Path
from typing import Annotated

# Создание объекта FastAPI
app = FastAPI()

# Маршрут для страницы пользователя с валидацией user_id
@app.get("/user/{user_id}")
def read_user(
    user_id: Annotated[
        int,
        Path(title="Enter User ID", ge=1, le=100, example=1)  # Валидация значения user_id
    ]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут для страницы пользователя с валидацией username и age
@app.get("/user/{username}/{age}")
def user_info(
    username: Annotated[
        str,
        Path(title="Enter username", min_length=5, max_length=20, example="UrbanUser")  # Валидация длины строки
    ],
    age: Annotated[
        int,
        Path(title="Enter age", ge=18, le=120, example=24)  # Валидация значения age
    ]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
