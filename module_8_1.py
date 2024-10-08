def add_everything_up(a, b):
    try:
        # Проверяем, если типы одинаковые
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b  # Сумма чисел
        elif isinstance(a, str) and isinstance(b, str):
            return a + b  # Конкатенация строк
        else:
            # Если типы разные, выбрасываем TypeError
            raise TypeError(f"Cannot add {type(a).__name__} "
                            f"and {type(b).__name__}")
    except TypeError:
        # Возвращаем строковое представление аргументов
        return str(a) + str(b)

# Примеры использования
print(add_everything_up(123.456, 'строка'))   # 123.456строка
print(add_everything_up('яблоко', 4215))      # яблоко4215
print(add_everything_up(123.456, 7))          # 130.456
