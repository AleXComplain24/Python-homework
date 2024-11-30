# Импортируем потоки, random, time
import threading
from random import randint
from time import sleep

#Инициализация объекта Bank:
# Хранить начальный баланс в атрибуте balance.
# Использовать объект Lock для управления потоками.

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()


#Метод deposit:Выполнять 100 итераций пополнения баланса на случайное значение от 50 до 500.\n
# Если баланс превышает 500, разблокировать поток с помощью метода release объекта Lock.
# Выводить сообщения о произведенных операциях.
# Учитывать небольшую задержку в 0.001 секунды.
    def deposit(self):
        for _ in range(100):
            amount = randint(50,500)
            self.balance += amount
            print(F"Пополнение: {amount}. Баланс: {self.balance}")

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            sleep(0.001)

    #Метод take:
    # Выполнять 100 итераций запроса на снятие средств.
    # Если запрашиваемая сумма превышает текущий баланс,
    # блокировать поток методом acquire.
    # Иначе, уменьшать баланс на запрашиваемую сумму и выводить соответствующие сообщения.
    def take(self):
        for _ in range(100):
            amount = randint(50, 500)
            print(f"Запрос на {amount}")

            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print ("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

            sleep(0.001)

# Создание объекта класса Bank
bk = Bank()

# Создание потоков:
# Запустить два потока: один для deposit, другой для take.
# Дождаться завершения потоков и вывести итоговый баланс.
# Создание потоков

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

# Запуск потоков
th1.start()
th2.start()


# Ожидание завершения потоков
th1.join()
th2.join()

# Итоговый баланс
print(f'Итоговый баланс: {bk.balance}')