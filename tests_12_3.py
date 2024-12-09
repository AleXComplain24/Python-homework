import unittest
from models_12_3 import Runner, Tournament  # Импортируем классы

# Декоратор для пропуска тестов
def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Usain")
        runner.run()
        self.assertEqual(runner.distance, 10)

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Usain")
        runner.walk()
        self.assertEqual(runner.distance, 5)

    @skip_if_frozen
    def test_str(self):
        runner = Runner("Usain")
        self.assertEqual(str(runner), "Usain")


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_tournament(self):
        runner1 = Runner("Usain", speed=10)
        runner2 = Runner("Bolt", speed=15)
        tournament = Tournament(50, runner1, runner2)
        results = tournament.start()
        self.assertEqual(results[1], runner2)  # Bolt finishes first
        self.assertEqual(results[2], runner1)  # Usain finishes second

    @skip_if_frozen
    def test_empty_tournament(self):
        tournament = Tournament(100)
        results = tournament.start()
        self.assertEqual(results, {})
