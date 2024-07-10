# 1. Задаем переменные разных типов данных:

# Создаем переменную immutable_var и присваиваем ей кортеж из нескольких элементов разных типов данных
immutable_var = (1, 2, 'a', 'b')

# Выводим кортеж immutable_var на экран
print("Immutable tuple:", immutable_var)

# 2. Изменение значений переменных:

# Попытка изменить элементы кортежа immutable_var
try:
    immutable_var[0] = 100
except TypeError as e:
    print("Ошибка при попытке изменить элемент кортежа:", e)

# Объяснение, почему нельзя изменить значения элементов кортежа:
# Кортежи (tuples) в Python являются неизменяемыми объектами. Это означает, что после их создания,
# их содержимое не может быть изменено. Попытка изменить элемент кортежа приведет к ошибке TypeError.

# 3. Создание изменяемых структур данных:

# Создаем переменную mutable_list и присваиваем ей список из нескольких элементов
mutable_list = [1, 2, 'a', 'b']

# Изменяем элементы списка mutable_list
mutable_list[0] = 100
mutable_list.append('Modified')

# Выводим на экран измененный список mutable_list
print("Mutable list:", mutable_list)