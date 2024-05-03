results = [10, 8, 9, 7, 6, 9, 10, 8, 9, 10]

# TODO Вычислите необходимые значения
min_score = min(results)
max_score = max(results)
total = sum(results)
count = len(results)
average = total / count
print("Среднее арифметическое результатов выстрелов:", average)
print("Наименьшее количество очков за выстрел:", min_score)
print("Наибольшее количество очков за выстрел:", max_score)
