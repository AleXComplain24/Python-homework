# 1st program
print(9 ** 0.5 * 5)
# 2nd program
result = (9.99 > 9.98) and (1000 != 1000.1)
print(result)
# 3rd program

# Исходные числа
number1 = 1234
number2 = 5678

# Выделение серединных чисел
middle1 = (number1 // 10) % 100  # для 1234: (1234 // 10) % 100 = 123 % 100 = 23
middle2 = (number2 // 10) % 100  # для 5678: (5678 // 10) % 100 = 567 % 100 = 67

# Сумма серединных чисел
sum_middle = middle1 + middle2

# Вывод результата
print(sum_middle)
# 4th program

# Исходные числа
number1 = 13.42
number2 = 42.13

# Получаем целую и дробную части чисел
int_part1 = number1 // 1  # Целая часть числа 1
frac_part1 = number1 % 1   # Дробная часть числа 1

int_part2 = number2 // 1  # Целая часть числа 2
frac_part2 = number2 % 1   # Дробная часть числа 2

# Округляем дробные части до целых чисел и переносим запятую на два знака вправо
rounded_frac_part1 = round(frac_part1 * 100)
rounded_frac_part2 = round(frac_part2 * 100)

# Вывод значений переменных для проверки
print(f"number1 = {number1}")
print(f"number2 = {number2}")
print(f"int_part1 = {int_part1}")
print(f"rounded_frac_part1 = {rounded_frac_part1}")
print(f"int_part2 = {int_part2}")
print(f"rounded_frac_part2 = {rounded_frac_part2}")

# Проверяем условие
result = (int_part1 == rounded_frac_part2) or (int_part2 == rounded_frac_part1)

# Вывод результата
print(f"Результат проверки: {result}")