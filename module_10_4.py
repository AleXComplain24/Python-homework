import threading
import time
from queue import Queue
from random import randint


# Класс Table:
# Имеет атрибуты number (номер стола) и guest
# (гость за столом, изначально None).

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None  # Гость за столом (изначально None)


# Класс Guest:
# Наследуется от Thread.
# Хранит имя гостя.
# В методе run делает случайную задержку от 3 до 10 секунд,
# имитируя время, которое гость проводит за столом.

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # Гость проводит случайное время за столом (3-10 секунд)
        time.sleep(randint(3, 10))


# Класс Cafe:
# Хранит столы в атрибуте tables и очередь гостей в queue.

class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)  # Столы кафе
        self.queue = Queue()        # Очередь гостей


# Метод guest_arrival:
# Проверяет наличие свободных столов.
# Если стол свободен, садит за него гостя и запускает поток.
# Если столов нет, помещает гостя в очередь.

    def guest_arrival(self, *guests):
        for guest in guests:
            # Найти первый свободный стол
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()  # Запускаем поток гостя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            else:
                # Если нет свободных столов, добавить гостя в очередь
                self.queue.put(guest)
                print(f"{guest.name} в очереди")


# Метод discuss_guests:
# Работает, пока есть гости за столами или в очереди.
# Проверяет, завершил ли гость поток (покинул стол).
# Если стол освобожден, из очереди берется следующий гость.

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    # Гость завершил поток, покидает стол
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

                    # Если очередь не пуста, посадить следующего гостя за этот стол
                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()  # Запускаем поток следующего гостя
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            time.sleep(0.1)  # Задержка для имитации процесса обслуживания

# Пример выполнения задачи
# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guest_names = [
    "Maria", "Oleg", "Vakhtang", "Sergey", "Darya", "Arman",
    "Vitoria", "Nikita", "Galina", "Pavel", "Ilya", "Alexandra"
]

# Создание гостей
guests = [Guest(name) for name in guest_names]

# Создание кафе с заданными столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()