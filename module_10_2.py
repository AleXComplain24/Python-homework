import threading
import time


class Knight(threading.Thread):
    total_enemies = 100  # Общее количество врагов
    lock = threading.Lock()  # Блокировка для синхронизации доступа к врагам

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0  # Счетчик дней для каждого рыцаря

    def run(self):
        print(f"{self.name}, на нас напали!")
        while True:
            with Knight.lock:
                if Knight.total_enemies <= 0:
                    break
                # Уменьшение количества врагов
                enemies_defeated = min(self.power, Knight.total_enemies)
                Knight.total_enemies -= enemies_defeated

            # Увеличение количества дней
            self.days += 1
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {Knight.total_enemies} воинов.")
            time.sleep(1)

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание объектов рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
time.sleep(0.1)  # Небольшая задержка для обеспечения порядка вывода
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

# Вывод сообщения о завершении всех битв
print("Все битвы закончились!")
