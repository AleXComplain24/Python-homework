# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создание пустых списков для простых и непростых чисел
primes = []
not_primes = []

# Перебор чисел из исходного списка
for num in numbers:
    # Пропускаем число 1, так как оно не является ни простым, ни составным
    if num < 2:
        not_primes.append(num)
        continue

    # Переменная для отметки простоты числа
    is_prime = True

    # Проверка на простоту
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    # Запись числа в соответствующий список
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Вывод списков на экран
print("Primes:", primes)
print("Not Primes:", not_primes)