from fastapi import FastAPI

# Создание объекта FastAPI
app = FastAPI()

# Маршрут для главной страницы
@app.get("/")
def read_main() -> str:
    return "Главная страница"

# Маршрут для страницы администратора
@app.get("/user/admin")
def read_admin() -> str:
    return "Вы вошли как администратор"

# Маршрут для страницы пользователя с параметром user_id
@app.get("/user/{user_id}")
def read_user(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"

# Маршрут для страницы пользователя с передачей параметров через адресную строку
@app.get("/user")
def user_info(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
