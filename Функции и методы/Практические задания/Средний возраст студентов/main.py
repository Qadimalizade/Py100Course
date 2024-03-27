def calculate_average_age(student_grades):
    average = sum(student_grades.values()) / len(student_grades)
    return average


students_dict = {
    'Саша': 27,
    'Кирилл': 52, 
    'Маша': 14, 
    'Петя': 36, 
    'Оля': 43, 
}
print(f"Средний возраст студентов: {calculate_average_age(students_dict)}")  # TODO Распечатайте средний возраст студентов
