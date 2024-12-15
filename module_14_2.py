import sqlite3

# Подключение к базе данных
db_name = "not_telegram.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Создание таблицы Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Очистка таблицы перед заполнением
cursor.execute('DELETE FROM Users')
conn.commit()

# Заполнение таблицы 10 записями
users = [
    ("User1", "example1@gmail.com", 10, 1000),
    ("User2", "example2@gmail.com", 20, 1000),
    ("User3", "example3@gmail.com", 30, 1000),
    ("User4", "example4@gmail.com", 40, 1000),
    ("User5", "example5@gmail.com", 50, 1000),
    ("User6", "example6@gmail.com", 60, 1000),
    ("User7", "example7@gmail.com", 70, 1000),
    ("User8", "example8@gmail.com", 80, 1000),
    ("User9", "example9@gmail.com", 90, 1000),
    ("User10", "example10@gmail.com", 100, 1000),
]
cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users)
conn.commit()

# Обновление баланса у каждой 2-ой записи, начиная с 1-ой
cursor.execute('SELECT id FROM Users')
ids = [row[0] for row in cursor.fetchall()]
for i, id_ in enumerate(ids, start=1):
    if i % 2 == 1:  # Каждая 2-ая строка (по индексу)
        cursor.execute('UPDATE Users SET balance = 500 WHERE id = ?', (id_,))
conn.commit()

# Удаление каждой 3-ей записи, начиная с первой строки (в терминах физического порядка)
cursor.execute('SELECT * FROM Users')
records = cursor.fetchall()
ids_to_delete = [record[0] for i, record in enumerate(records, start=1) if i % 3 == 0]
cursor.executemany('DELETE FROM Users WHERE id = ?', [(id_,) for id_ in ids_to_delete])
conn.commit()

# Удаление пользователя с id = 6
cursor.execute('DELETE FROM Users WHERE id = ?', (6,))
conn.commit()

# Подсчёт общего количества записей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# Вывод среднего баланса всех пользователей
average_balance = all_balances / total_users if total_users > 0 else 0
print(f"Средний баланс всех пользователей: {average_balance:.1f}")

# Закрытие соединения с базой данных
conn.close()
