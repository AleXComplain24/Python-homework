# Класс для исключения некорректного VIN номера
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message  # Сообщение об ошибке

# Класс для исключения некорректных номеров автомобиля
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message  # Сообщение об ошибке

# Класс Car
class Car:
    def __init__(self, model, vin, numbers):
        self.model = model  # Название автомобиля

        # Проверяем и устанавливаем VIN номер через приватный метод
        if self._is_valid_vin(vin):
            self.__vin = vin

        # Проверяем и устанавливаем номера автомобиля через приватный метод
        if self._is_valid_numbers(numbers):
            self.__numbers = numbers

        # Приватный метод проверки VIN номера

    def _is_valid_vin(self, vin_number):
        # Проверяем тип данных VIN номера
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')

        # Проверяем диапазон VIN номера
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

        return True

        # Приватный метод проверки номеров автомобиля

    def _is_valid_numbers(self, numbers):
        # Проверяем тип данных номера автомобиля
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')

        # Проверяем длину номера автомобиля
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')

        return True

# Пример выполнения программы
try:
    first = Car('Model1', 1000000, 'f123dj')  # Корректные данные
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')  # Некорректный VIN
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')  # Некорректный номер
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')