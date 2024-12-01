import time
from multiprocessing import Pool

# Функция считывания данных из файла
def read_info(name):
    all_data = [] # Список для данных
    with open (name, 'r') as file:
        while True:
            line = file.readline()  # Исправлено здесь
            if not line:  # Если строк больше нет
                break
            all_data.append(line)  # Добавляем строку в список

# Основная часть программы
if __name__ == '__main__':
    # Список имен файлов
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    # Пример файлов file_1.txt, file_2.txt, и т.д.

# Линейный вызов
start_time = time.time()
for filename in filenames:
    read_info(filename)
print(f"Линейный вызов: {time.time() - start_time:.6f} секунд")

# Многопроцессный вызов
start_time = time.time()
with Pool() as pool:
    pool.map(read_info, filenames)
print(f"Многопроцессный вызов: {time.time() - start_time:.6f} секунд")