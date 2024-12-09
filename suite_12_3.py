import unittest
from tests_12_3 import RunnerTest, TournamentTest  # Импорт тестов

# Создание TestSuite и добавление тестов
def create_test_suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
    return suite

# Запуск тестов
if __name__ == "__main__":
    suite = create_test_suite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
