def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            # Определяем текущую позицию в файле перед записью строки
            byte_position = file.tell()
            # Записываем строку в файл
            file.write(string + '\n')
            # Сохраняем номер строки, позицию байта и саму строку в словарь
            strings_positions[(line_number, byte_position)] = string

    return strings_positions

# Пример использования функции:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)