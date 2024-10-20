def apply_all_func(int_list, *functions):
    # Создаем пустой словарь для хранения результатов
    results = {}

    # Перебираем каждую переданную функцию
    for func in functions:
        # Применяем функцию к списку чисел
        try:
            # Записываем результат работы функции под её именем
            results[func.__name__] = func(int_list)
        except Exception as e:
            # На случай ошибки при выполнении функции выводим сообщение
            results[func.__name__] = f"Error: {e}"

    # Возвращаем словарь с результатами
    return results


# Пример использования функции
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
