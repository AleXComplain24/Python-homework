# Использование %:

team1_num = 5
print("В команде Мастера кода участников: %d !" % team1_num)

# Форматирование с 2-мя переменными:

team1_num = 5
team2_num = 6
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

# Использование format():

score_2 = 42
print("Команда Волшебники данных решила задач: {} !".format(score_2))

# Форматирование с плавающей точкой:

team2_time = 18015.2
print("Волшебники данных решили задачи за {:.1f} с !".format(team2_time))

# Использование f-строк:

score_1 = 40
score_2 = 42
print(f"Команды решили {score_1} и {score_2} задач.")

# Форматирование результата соревнования:

challenge_result = "Победа команды Мастера кода!"
print(f"Результат битвы: {challenge_result}")

# Форматирование с двумя переменными (общее количество задач и среднее время):

tasks_total = 82
time_avg = 350.4
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!")

# Логика для определения результата соревнования:

team1_time = 1552.512
team2_time = 2153.31451
score_1 = 40
score_2 = 42

if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

print(f"Результат битвы: {challenge_result}")


# Пример всех переменных:

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 350.4

# Форматирование с использованием %
print("В команде Мастера кода участников: %d !" % team1_num)
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

# Форматирование с использованием format()
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {:.1f} с !".format(team2_time))

# Форматирование с использованием f-строк
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!")
