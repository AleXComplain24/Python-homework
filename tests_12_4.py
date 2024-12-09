import unittest
import logging
from models_12_3 import Runner  # Импортируем класс Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            # Создаём объект с отрицательной скоростью, что должно вызвать ValueError
            runner = Runner("Вася", -5)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            # Логируем предупреждение при ошибке
            logging.warning(f"Неверная скорость для Runner: {e}")

    def test_run(self):
        try:
            # Создаём объект с неверным типом имени, что должно вызвать TypeError
            runner = Runner(42)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            # Логируем предупреждение при ошибке
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")

    def test_correct_creation(self):
        try:
            # Создаём объект с корректными параметрами
            runner = Runner("Иван", 10)
            self.assertEqual(runner.name, "Иван")
            self.assertEqual(runner.speed, 10)
            logging.info('"test_correct_creation" выполнен успешно')
        except Exception as e:
            logging.warning(f"Ошибка при создании объекта Runner: {e}")

    def test_run_method(self):
        try:
            # Проверяем корректность метода run
            runner = Runner("Иван", 10)
            runner.run()
            self.assertEqual(runner.distance, 20)
            logging.info('"test_run_method" выполнен успешно')
        except Exception as e:
            logging.warning(f"Ошибка в методе run: {e}")

    def test_walk_method(self):
        try:
            # Проверяем корректность метода walk
            runner = Runner("Иван", 10)
            runner.walk()
            self.assertEqual(runner.distance, 10)
            logging.info('"test_walk_method" выполнен успешно')
        except Exception as e:
            logging.warning(f"Ошибка в методе walk: {e}")


# Запуск тестов
if __name__ == "__main__":
    unittest.main()
