import random

# список сотрудников
employees = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "John"]

# список дней недели
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# список часов работы
hours = ["9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]

# создаем пустое расписание
schedule = {}

# заполняем расписание случайными данными
for day in days:
    schedule[day] = {}
    for hour in hours:
        schedule[day][hour] = random.choice(employees)

# выводим расписание на экран
for day in days:
    print(day)
    for hour in hours:
        print(hour + ": " + schedule[day][hour])
    print("")