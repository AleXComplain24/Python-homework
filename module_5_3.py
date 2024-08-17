from module_5.module_5_1 import House


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

# Методы сравнения
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True

# Методы для работы с арифметическими операциями
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

# Пример использования:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Название: ЖК Акация, кол-во этажей: 20

# Сравнение __eq__
print(h1 == h2)  # False

# Увеличение количества этажей с помощью __add__
h1 = h1 + 10
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 20

# Сравнение после увеличения этажей
print(h1 == h2)  # True

# Использование __iadd__
h1 += 10
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 30

# Использование __radd__
h2 = 10 + h2
print(h2)  # Название: ЖК Акация, кол-во этажей: 30

# Сравнения
print(h1 > h2)   # False
print(h1 >= h2)  # True
print(h1 < h2)   # False
print(h1 <= h2)  # True
print(h1 != h2)  # False