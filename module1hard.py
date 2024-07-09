# Список оценок для каждого ученика в алфавитном порядке
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

# Множество имен учеников
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество студентов в отсортированный список
sorted_students = sorted(students)

# Создаем пустой словарь для хранения среднего балла каждого ученика
student_grades = {}

# Заполняем словарь
for i, student in enumerate(sorted_students):
    average_grade = sum(grades[i]) / len(grades[i])
    student_grades[student] = average_grade

# Выводим результат на экран
print(student_grades)