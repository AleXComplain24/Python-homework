import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()

                # Удаляем пунктуацию
                for p in punctuation:
                    content = content.replace(p, '')

                words = content.split()
                all_words[file_name] = words

        return all_words

# Пример использования:
# finder = WordsFinder('test_file.txt')
# print(finder.get_all_words())

    def find(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            if word in words:
                results[name] = words.index(word)

        return results

# Пример использования:
# finder = WordsFinder('test_file.txt')
# print(finder.find('TEXT'))

    def count(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            results[name] = words.count(word)

        return results

# Пример использования:
# finder = WordsFinder('test_file.txt')
# print(finder.count('teXT'))


finder = WordsFinder('test_file.txt')
print(finder.get_all_words())  # Все слова
print(finder.find('TEXT'))     # Найти первое вхождение слова
print(finder.count('teXT'))    # Подсчитать количество вхождений слова