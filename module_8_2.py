# Функция для подсчёта суммы с учётом некорректных данных
# Функция для подсчёта суммы с учётом некорректных данных
def personal_sum(numbers):
    result = 0  # Переменная для хранения суммы
    incorrect_data = 0  # Счётчик некорректных данных

    # Перебираем коллекцию numbers
    for item in numbers:
        try:
            # Проверяем, является ли элемент числом
            if isinstance(item, (int, float)):
                result += item  # Увеличиваем сумму
            else:
                # Исключение для некорректного типа данных
                raise TypeError
        except TypeError:
            # Если тип данных некорректен, увеличиваем счётчик
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {item}')

    # Возвращаем кортеж: сумма чисел и количество некорректных данных
    return result, incorrect_data


# Функция для подсчёта среднего арифметического
def calculate_average(numbers):
    try:
        # Проверяем, является ли numbers коллекцией
        if not isinstance(numbers, (list, tuple)):
            raise TypeError

        # Используем функцию personal_sum для подсчёта суммы
        total_sum, incorrect_data = personal_sum(numbers)

        # Количество чисел - это общее количество элементов минус некорректные данные
        count_of_numbers = len(numbers) - incorrect_data

        # Проверка деления на 0 (если чисел нет)
        if count_of_numbers == 0:
            raise ZeroDivisionError

        # Возвращаем среднее арифметическое
        return total_sum / count_of_numbers
    except ZeroDivisionError:
        # Возвращаем 0, если деление на 0
        return 0
    except TypeError:
        # Обрабатываем случай некорректного типа данных
        print('В numbers записан некорректный тип данных')
        return None


# Примеры выполнения программы
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но символы - не числа
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передан не список или кортеж
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать