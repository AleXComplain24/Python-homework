# Декоратор для проверки, простое число или составное
def is_prime(func):
    def wrapper(*args, **kwargs):
        # Получаем результат функции
        result = func(*args, **kwargs)

        # Проверка, простое число или нет
        if result < 2:
            print("Составное")
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")

        # Возвращаем результат выполнения основной функции
        return result

    return wrapper


# Функция, которая складывает три числа
@is_prime  # Применение декоратора
def sum_three(a, b, c):
    return a + b + c


# Пример использования
result = sum_three(2, 3, 6)
print(result)
