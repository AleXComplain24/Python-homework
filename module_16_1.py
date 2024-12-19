from fastapi import FastAPI

# Создание объекта FastAPI
app = FastAPI()

# Маршрут для главной страницы
@app.get("/")
def read_main():
    return {"message": "Главная страница"}

# Маршрут для страницы администратора
@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

# Маршрут для страницы пользователя с параметром user_id
@app.get("/user/{user_id}")
def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут для страницы пользователя с передачей параметров через адресную строку
@app.get("/user")
def user_info(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
