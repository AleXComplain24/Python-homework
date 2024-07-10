# Получаем три целых числа от пользователя
first = int(input())
second = int(input())
third = int(input())

# Проверяем равенство чисел и выводим соответствующий результат
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
