import math

class Figure:
    sides_count = 0  # Атрибут класса для хранения количества сторон

    def __init__(self, color, *sides):
        self._sides = list(sides) if len(sides) == self.sides_count \
        else [1] * self.sides_count
        self._color = color if self._is_valid_color(*color) \
        else [0, 0, 0]
        self.filled = False

    def _is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in [r, g, b])

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self._color = [r, g, b]

    def get_color(self):
        return self._color

    def _is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int)
        and side > 0 for side in new_sides)

    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            self._sides = list(new_sides)

    def get_sides(self):
        return self._sides

    def __len__(self):
        return sum(self._sides)  # Возвращает периметр, как сумму всех сторон

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides) # Вызов конструктора родительского класса Figure
        self.__radius = self.__calculate_radius() # Дополнительная инициализация в Circle

    def __calculate_radius(self):
        # Радиус круга, исходя из длины окружности (длина = 2 * pi * r)
        return self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        # Площадь круга: π * r^2
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        # Используем формулу Герона для расчета площади
        a, b, c = self.get_sides()
        s = (a + b + c) / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        side = sides[0] if len(sides) == 1 else 1
        super().__init__(color, *([side] * self.sides_count))

    def get_volume(self):
        # Объем куба: сторона^3
        side = self.get_sides()[0]
        return side ** 3

circle1 = Circle((200, 200, 100), 10)  # Создаем круг с цветом и одной стороной
cube1 = Cube((222, 35, 130), 6)  # Создаем куб с цветом и одной стороной

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # [55, 66, 77]

cube1.set_color(300, 70, 15)  # Не изменится, так как 300 вне диапазона
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится, т.к. сторон должно быть 12
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # [15]

# Проверка периметра (длины окружности):
print(len(circle1))  # 15

# Проверка объёма куба:
print(cube1.get_volume())  # 216