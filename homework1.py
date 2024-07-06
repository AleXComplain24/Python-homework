# Запись строки в переменную example
example = "Топинамбур"

# Вывод первого символа строки
print("Первый символ строки:", example[0])

# Вывод последнего символа строки (с использованием отрицательного индекса)
print("Последний символ строки:", example[-1])

# Вывод второй половины строки (учитывая, что длина строки нечётная)
middle_index = len(example) // 2
second_half = example[middle_index:]
print("Вторая половина строки:", second_half)

# Вывод строки наоборот
reversed_example = example[::-1]
print("Строка наоборот:", reversed_example)

# Вывод каждого второго символа строки
every_second_char = example[1::2]
print("Каждый второй символ строки:", every_second_char)
