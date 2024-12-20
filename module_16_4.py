from fastapi import FastAPI, HTTPException, Path
from typing import Annotated, List
from pydantic import BaseModel

# Создание объекта FastAPI
app = FastAPI()

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# Список пользователей
users: List[User] = []

# GET-запрос: Получение всех пользователей
@app.get("/users")
def get_users() -> List[User]:
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
    ]
) -> User:
    # Определение нового id
    new_id = users[-1].id + 1 if users else 1
    # Создание нового пользователя
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

# PUT-запрос: Обновление информации о пользователе
@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: Annotated[
        int,
        Path(title="Enter User ID", ge=1, example=1)
    ],
    username: Annotated[
        str,
        Path(title="Enter username", min_length=5, max_length=20, example="UrbanProfi")
    ],
    age: Annotated[
        int,
        Path(title="Enter age", ge=18, le=120, example=28)
    ]
) -> User:
    # Поиск пользователя по id
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    # Если пользователь не найден
    raise HTTPException(status_code=404, detail="User was not found")

# DELETE-запрос: Удаление пользователя
@app.delete("/user/{user_id}")
def delete_user(
    user_id: Annotated[
        int,
        Path(title="Enter User ID", ge=1, example=2)
    ]
) -> User:
    # Поиск и удаление пользователя
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    # Если пользователь не найден
    raise HTTPException(status_code=404, detail="User was not found")