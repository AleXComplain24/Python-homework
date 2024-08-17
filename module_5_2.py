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

# Пример использования:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__ метод
print(h1)  # Выведет: Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Выведет: Название: ЖК Акация, кол-во этажей: 20

# __len__ метод
print(len(h1))  # Выведет: 10
print(len(h2))  # Выведет: 20