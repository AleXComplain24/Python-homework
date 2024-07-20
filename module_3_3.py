def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции с разным количеством аргументов
print_params()                # Вывод: 1 строка True
print_params(b=25)            # Вывод: 1 25 True
print_params(c=[1, 2, 3])    # Вывод: 1 строка [1, 2, 3]

# Распаковка параметров
values_list = [3.14, 'текст', False]
values_dict = {'a': 10, 'b': 'новая строка', 'c': [4, 5, 6]}

print_params(*values_list)    # Вывод: 3.14 текст False
print_params(**values_dict)   # Вывод: 10 новая строка [4, 5, 6]

# Распаковка списка и отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)   # Вывод: 54.32 Строка 42

