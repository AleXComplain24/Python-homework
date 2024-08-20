# Класс Horse
class Horse:
    def __init__(self):
        self.x_distance = 0  # Пройденный путь
        self.sound = 'Frrr'  # Звук лошади

    def run(self, dx):
        self.x_distance +=dx  # Увеличиваем пройденный путь

# Класс Eagle
class Eagle:
    def __init__(self):
        self.y_distance = 0  # Высота полета
        self.sound = 'I train, eat, sleep and repeat' #Звук орла

    def fly(self, dy):
        self.y_distance += dy  # Увеличиваем высоту полета

# Класс Pegasus, наследующий от Horse и Eagle
class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)  # Инициализация класса Horse
        Eagle.__init__(self)  # Инициализация класса Eagle
        # Атрибут sound будет взят из последнего по порядку класса (Eagle)

    def move(self, dx, dy):
        self.run(dx) # Запуск метода run из Horse
        self.fly(dy) # Запуск метода fly из Eagle

    def get_pos(self):
        return (self.x_distance, self.y_distance) # Возвращаем кортеж координат

    def voice(self):
        print(self.sound) # Выводим звук от последнего класса в наследовании

# Пример использования
p1 = Pegasus()

print(p1.get_pos())  # (0, 0)
p1.move(10, 15)
print(p1.get_pos())  # (10, 15)
p1.move(-5, 20)
print(p1.get_pos())  # (5, 35)

p1.voice() # I train, eat, sleep, and repeat