# 1. Работа со словарями:

# Создаем переменную my_dict и присваиваем ей словарь из нескольких пар ключ-значение
my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}

# Выводим на экран словарь my_dict
print("Dict:", my_dict)

# Выводим на экран одно значение по существующему ключу
print("Existing value:", my_dict['Masha'])

# Выводим на экран одно значение по отсутствующему ключу без ошибки
print("Not existing value:", my_dict.get('Ivan', None))

# Добавляем ещё две произвольные пары того же формата в словарь my_dict
my_dict['Kamila'] = 1981
my_dict['Artem'] = 1915

# Удаляем одну из пар в словаре по существующему ключу и выводим значение из этой пары на экран
deleted_value = my_dict.pop('Egor', None)
print("Deleted value:", deleted_value)

# Выводим на экран измененный словарь my_dict
print("Modified dictionary:", my_dict)

# 2. Работа с множествами:

# Создаем переменную my_set и присваиваем ей множество, состоящее из разных типов данных с повторяющимися значениями
my_set = {1, 'Яблоко', 42.314, 1, 'Яблоко'}

# Выводим на экран множество my_set (должны отобразиться только уникальные значения)
print("Set:", my_set)

# Добавляем 2 произвольных элемента в множество my_set, которых ещё нет
my_set.add(13)
my_set.add((5, 6, 1.6))

# Удаляем один любой элемент из множества my_set
my_set.remove(1)  # Удаляем элемент '1'

# Выводим на экран измененное множество my_set
print("Modified set:", my_set)