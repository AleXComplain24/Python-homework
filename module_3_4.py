def single_root_words(root_word, *other_words):
    # Приводим root_word к нижнему регистру
    root_word_lower = root_word.lower()
    # Создаем пустой список для хранения подходящих слов
    same_words = []

    # Перебираем все слова в other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()
        # Проверяем, содержится ли root_word в текущем слове или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            # Если условие выполняется, добавляем слово в результирующий список
            same_words.append(word)

    # Возвращаем результирующий список
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)