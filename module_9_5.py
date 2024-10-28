# Класс исключения StepValueError, наследующий от ValueError
class StepValueError(ValueError):
    pass

# Класс итератора
class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            # Выбрасываем исключение при шаге, равном 0
            raise StepValueError('Шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start  # Устанавливаем указатель на начальное значение

    def __iter__(self):
        # Сбрасываем указатель на старт и возвращаем объект итератора
        self.pointer = self.start
        return self

    def __next__(self):
        # Проверяем условие окончания итерации в зависимости от знака шага
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            # Останавливаем итерацию
            raise StopIteration
        # Сохраняем текущее значение
        current = self.pointer
        # Увеличиваем указатель на шаг
        self.pointer += self.step
        # Возвращаем текущее значение
        return current

# Пример использования
try:
    # Попытка создать итератор с шагом 0, что вызовет исключение
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

# Создание других объектов итератора
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

# Итерации по каждому объекту
for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()
