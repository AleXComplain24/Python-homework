import unittest

# Класс Runner
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 7

    def __str__(self):
        return self.name

# тесты для класса Runner
class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50, "Distance after 10 walks should be 50")

    def test_run(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, "Distance after 10 runs should be 100")

    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance,
                                "Distances after different actions should not be equal")

# Запуск тестов
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))