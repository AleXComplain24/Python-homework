# Базовый класс для всех животных
class Animal:
    def __init__(self, name):
        self.alive = True  # Живой
        self.fed = False  # Не накормлен
        self.name = name  # Имя животного

    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


# Базовый класс для всех растений
class Plant:
    def __init__(self, name):
        self.edible = False  # По умолчанию несъедобное
        self.name = name  # Имя растения


# Класс млекопитающих, наследующий от Animal
class Mammal(Animal):
    pass  # Дополнительного поведения пока не требуется


# Класс хищников, наследующий от Animal
class Predator(Animal):
    pass  # Дополнительного поведения пока не требуется


# Класс цветка, наследующий от Plant
class Flower(Plant):
    pass  # Цветок по умолчанию несъедобный


# Класс фруктов, наследующий от Plant
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Фрукты съедобные


# Создаем объекты
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Выводим имена
print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик

# Проверяем начальное состояние
print(a1.alive)  # True
print(a2.fed)  # False

# Кормим животных
a1.eat(p1)  # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)  # Хатико съел Заводной апельсин

# Проверяем конечное состояние
print(a1.alive)  # False
print(a2.fed)  # True
