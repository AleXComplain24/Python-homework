def all_variants(text):
    # Внешний цикл по длине подпоследовательностей
    for length in range(1, len(text) + 1):
        # Внутренний цикл по всем возможным стартовым позициям
        for start in range(len(text) - length + 1):
            # Возвращаем подпоследовательность от start длиной length
            yield text[start:start + length]

# Пример использования
a = all_variants("abc")
for variant in a:
    print(variant)

