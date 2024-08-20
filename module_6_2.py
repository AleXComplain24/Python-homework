# Базовый класс Vehicle
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white' ]

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner # Владелец
        self.__model = model # Модель
        self.__engine_power = engine_power # Мощность двигателя
        if color.lower() in (c.lower() for c in self.__COLOR_VARIANTS):
            self.__color = color # цвет
        else:
            raise ValueError(f"Цвет {color} не доступен для выбора")

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return F"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in (c.lower() for c in self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

# Класс Sedan, наследующий Vehicle
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # Лимит пассажиров

# Пример использования
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()