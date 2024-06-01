class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        if not self.grades:
            average_grade = 0
        else:
            total_grades = 0
            count_grades = 0
            for course, grades in self.grades.items():
                total_grades += sum(grades)
                count_grades += len(grades)
            average_grade = total_grades / count_grades
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade:.1f}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Нельзя сравнивать студента')
        if not self.grades:
            average_grade_self = 0
        else:
            total_grades_self = 0
            count_grades_self = 0
            for course, grades in self.grades.items():
                total_grades_self += sum(grades)
                count_grades_self += len(grades)
            average_grade_self = total_grades_self / count_grades_self

        if not other.grades:
            average_grade_other = 0
        else:
            total_grades_other = 0
            count_grades_other = 0
            for course, grades in other.grades.items():
                total_grades_other += sum(grades)
                count_grades_other += len(grades)
            average_grade_other = total_grades_other / count_grades_other

        return average_grade_self < average_grade_other

    def __le__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Нельзя сравнивать студента')
        if not self.grades:
            average_grade_self = 0
        else:
            total_grades_self = 0
            count_grades_self = 0
            for course, grades in self.grades.items():
                total_grades_self += sum(grades)
                count_grades_self += len(grades)
            average_grade_self = total_grades_self / count_grades_self

        if not other.grades:
            average_grade_other = 0
        else:
            total_grades_other = 0
            count_grades_other = 0
            for course, grades in other.grades.items():
                total_grades_other += sum(grades)
                count_grades_other += len(grades)
            average_grade_other = total_grades_other / count_grades_other

        return average_grade_self <= average_grade_other

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Нельзя сравнивать студента')
        if not self.grades:
            average_grade_self = 0
        else:
            total_grades_self = 0
            count_grades_self = 0
            for course, grades in self.grades.items():
                total_grades_self += sum(grades)
                count_grades_self += len(grades)
            average_grade_self = total_grades_self / count_grades_self

        if not other.grades:
            average_grade_other = 0
        else:
            total_grades_other = 0
            count_grades_other = 0
            for course, grades in other.grades.items():
                total_grades_other += sum(grades)
                count_grades_other += len(grades)
            average_grade_other = total_grades_other / count_grades_other

        return average_grade_self == average_grade_other

    def __ne__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Нельзя сравнивать студента')
        if not self.grades:
            average_grade_self = 0
        else:
            total_grades_self = 0
            count_grades_self = 0
            for course, grades in self.grades.items():
                total_grades_self += sum(grades)
                count_grades_self += len(grades)
            average_grade_self = total_grades_self / count_grades_self

        if not other.grades:
            average_grade_other = 0
        else:
            total_grades_other = 0
            count_grades_other = 0
            for course, grades in other.grades.items():
                total_grades_other += sum(grades)
                count_grades_other += len(grades)
            average_grade_other = total_grades_other / count_grades_other

        return average_grade_self != average_grade_other

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Нельзя сравнивать студента')
        if not self.grades:
            average_grade_self = 0
        else:
            total_grades_self = 0
            count_grades_self = 0
            for course, grades in self.grades.items():
                total_grades_self += sum(grades)
                count_grades_self += len(grades)
            average_grade_self = total_grades_self / count_grades_self

        if not other.grades:
            average_grade_other = 0
        else:
            total_grades_other = 0
            count_grades_other = 0
            for course, grades in other.grades.items():
                total_grades_other += sum(grades)
                count_grades_other += len(grades)
            average_grade_other = total_grades_other / count_grades_other

        return average_grade_self > average_grade_other

    def __ge__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Нельзя сравнивать студента')
        if not self.grades:
            average_grade_self = 0
        else:
            total_grades_self = 0
            count_grades_self = 0
            for course, grades in self.grades.items():
                total_grades_self += sum(grades)
                count_grades_self += len(grades)
            average_grade_self = total_grades_self / count_grades_self

        if not other.grades:
            average_grade_other = 0
        else:
            total_grades_other = 0
            count_grades_other = 0
            for course, grades in other.grades.items():
                total_grades_other += sum(grades)
                count_grades_other += len(grades)
            average_grade_other = total_grades_other / count_grades_other

        return average_grade_self >= average_grade_other

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        if not self.grades:
            average_grade = 0
        else:
            total_grades = 0
            count_grades = 0
            for course, grades in self.grades.items():
                total_grades += sum(grades)
                count_grades += len(grades)
            average_grade = total_grades / count_grades
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Нельзя сравнивать лектора')
        if not self.grades:
            average_grade_self = 0
        else:
            total_grades_self = 0
            count_grades_self = 0
            for course, grades in self.grades.items():
                total_grades_self += sum(grades)
                count_grades_self += len(grades)
            average_grade_self = total_grades_self / count_grades_self

        if not other.grades:
            average_grade_other = 0
        else:
            total_grades_other = 0
            count_grades_other = 0
            for course, grades in other.grades.items():
                total_grades_other += sum(grades)
                count_grades_other += len(grades)
            average_grade_other = total_grades_other / count_grades_other

        return average_grade_self < average_grade_other

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Нельзя сравнивать лектора')
        if not self.grades:
            average_grade_self = 0
        else:
            total_grades_self = 0
            count_grades_self = 0
            for course, grades in self.grades.items():
                total_grades_self += sum(grades)
                count_grades_self += len(grades)
            average_grade_self = total_grades_self / count_grades_self

        if not other.grades:
            average_grade_other = 0
        else:
            total_grades_other = 0
            count_grades_other = 0
            for course, grades in other.grades.items():
                total_grades_other += sum(grades)
                count_grades_other += len(grades)
            average_grade_other = total_grades_other / count_grades_other

        return average_grade_self <= average_grade_other

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Нельзя сравнивать лектора')
        if not self.grades:
            average_grade_self = 0
        else:
            total_grades_self = 0
            count_grades_self = 0
            for course, grades in self.grades.items():
                total_grades_self += sum(grades)
                count_grades_self += len(grades)
            average_grade_self = total_grades_self / count_grades_self

        if not other.grades:
            average_grade_other = 0
        else:
            total_grades_other = 0
            count_grades_other = 0
            for course, grades in other.grades.items():
                total_grades_other += sum(grades)
                count_grades_other += len(grades)
            average_grade_other = total_grades_other / count_grades_other

        return average_grade_self == average_grade_other

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Нельзя сравнивать лектора')
        if not self.grades:
            average_grade_self = 0
        else:
            total_grades_self = 0
            count_grades_self = 0
            for course, grades in self.grades.items():
                total_grades_self += sum(grades)
                count_grades_self += len(grades)
            average_grade_self = total_grades_self / count_grades_self

        if not other.grades:
            average_grade_other = 0
        else:
            total_grades_other = 0
            count_grades_other = 0
            for course, grades in other.grades.items():
                total_grades_other += sum(grades)
                count_grades_other += len(grades)
            average_grade_other = total_grades_other / count_grades_other

        return average_grade_self != average_grade_other

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Нельзя сравнивать лектора')
        if not self.grades:
            average_grade_self = 0
        else:
            total_grades_self = 0
            count_grades_self = 0
            for course, grades in self.grades.items():
                total_grades_self += sum(grades)
                count_grades_self += len(grades)
            average_grade_self = total_grades_self / count_grades_self

        if not other.grades:
            average_grade_other = 0
        else:
            total_grades_other = 0
            count_grades_other = 0
            for course, grades in other.grades.items():
                total_grades_other += sum(grades)
                count_grades_other += len(grades)
            average_grade_other = total_grades_other / count_grades_other

        return average_grade_self > average_grade_other

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Нельзя сравнивать лектора')
        if not self.grades:
            average_grade_self = 0
        else:
            total_grades_self = 0
            count_grades_self = 0
            for course, grades in self.grades.items():
                total_grades_self += sum(grades)
                count_grades_self += len(grades)
            average_grade_self = total_grades_self / count_grades_self

        if not other.grades:
            average_grade_other = 0
        else:
            total_grades_other = 0
            count_grades_other = 0
            for course, grades in other.grades.items():
                total_grades_other += sum(grades)
                count_grades_other += len(grades)
            average_grade_other = total_grades_other / count_grades_other

        return average_grade_self >= average_grade_other

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']
best_student.grades = {'Python': [9.9, 9.9, 9.9, 9.9, 9.9], 'Git': [9.9, 9.9, 9.9, 9.9, 9.9]}

another_student = Student('Another', 'Student', 'another_gender')
another_student.courses_in_progress += ['Python', 'Git']
another_student.finished_courses += ['Введение в программирование']
another_student.grades = {'Python': [9.8, 9.8, 9.8, 9.8, 9.8], 'Git': [9.8, 9.8, 9.8, 9.8, 9.8]}

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.grades = {'Python': [9.9, 9.9, 9.9, 9.9, 9.9], 'Git': [9.9, 9.9, 9.9, 9.9, 9.9]}

another_lecturer = Lecturer('Another', 'Lecturer')
another_lecturer.grades = {'Python': [9.8, 9.8, 9.8, 9.8, 9.8], 'Git': [9.8, 9.8, 9.8, 9.8, 9.8]}

print(best_student)
print(another_student)
print(cool_lecturer)
print(another_lecturer)

print("Сравнение студентов:")
print(best_student < another_student)
print(best_student <= another_student)
print(best_student == another_student)
print(best_student != another_student)
print(best_student > another_student)
print(best_student >= another_student)

print("\nСравнение лекторов:")
print(cool_lecturer < another_lecturer)
print(cool_lecturer <= another_lecturer)
print(cool_lecturer == another_lecturer)
print(cool_lecturer != another_lecturer)
print(cool_lecturer > another_lecturer)
print(cool_lecturer >= another_lecturer)