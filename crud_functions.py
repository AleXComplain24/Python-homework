import sqlite3

DB_PATH = "products.db"  # Имя базы данных


def initiate_db():
    """Создает таблицы Products и Users, если они не существуют."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Создаем таблицу Products
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    # Создаем таблицу Users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        )
    ''')

    conn.commit()
    conn.close()


def add_user(username, email, age):
    """Добавляет нового пользователя в таблицу Users."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                       (username, email, age, 1000))  # Баланс по умолчанию 1000
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Пользователь {username} уже существует.")
    finally:
        conn.close()


def is_included(username):
    """Проверяет, существует ли пользователь в таблице Users."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def get_all_products():
    """Возвращает все записи из таблицы Products."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()  # Получаем все записи из таблицы
    conn.close()
    return products
