def get_multiplied_digits(number):
# Преобразуем число в строку для облегчения обработки цифр
    str_number = str(number)


# Основное условие: если длина строки числа равна 1, возвращаем эту цифру
    if len(str_number) == 1:
        return int(str_number)


 # Берем первую цифру и преобразуем ее в целое число
    first = int(str_number[0])


# Возвращаем произведение первой цифры и результата рекурсивного вызова
    # для оставшейся части числа
    return first * get_multiplied_digits(int(str_number[1:]))


# Пример вызова функции
result = get_multiplied_digits(40203)
print(result)