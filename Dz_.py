class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = sum(sum(grades) / len(grades) for grades in self.grades.values()) / len(self.grades)
        return (f"Средняя оценка за домашние задания: {avg_grade}\nИмя: {self.name}\nФамилия: {self.surname}\nКурсы в "
                f"процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные"
                f" курсы: {', '.join(self.finished_courses)}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        avg_grade = sum(sum(grades) / len(grades) for grades in self.grades.values()) / len(self.grades)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}"

    def __lt__(self, other):
        return sum(sum(grades) / len(grades) for grades in self.grades.values()) < sum(
            sum(other.grades) / len(other.grades) for other.grades in other.grades.values())


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Создание экземпляров классов
student1 = Student("Иван", "Иванов", "м")
student2 = Student("Мария", "Петрова", "ж")

lecturer1 = Lecturer("Петр", "Сидоров")
lecturer2 = Lecturer("Анна", "Козлова")

reviewer1 = Reviewer("Елена", "Смирнова")
reviewer2 = Reviewer("Сергей", "Павлов")

course = "Python"

# Вызов методов
student1.courses_in_progress.append(course)
student2.courses_in_progress.append(course)

lecturer1.courses_attached.append(course)
lecturer2.courses_attached.append(course)

reviewer1.courses_attached.append(course)
reviewer2.courses_attached.append(course)

student1.rate_lecturer(lecturer1, course, 8)
student1.rate_lecturer(lecturer2, course, 9)
student2.rate_lecturer(lecturer1, course, 7)
student2.rate_lecturer(lecturer2, course, 8)

reviewer1.rate_hw(student1, course, 7)
reviewer1.rate_hw(student2, course, 9)
reviewer2.rate_hw(student1, course, 6)
reviewer2.rate_hw(student2, course, 8)


# Реализация функций для подсчета средних оценок
def avg_hw_grade(students, course):
    grades_sum = 0
    students_count = 0
    for student in students:
        if course in student.grades:
            grades_sum += sum(student.grades[course])
            students_count += len(student.grades[course])
    return grades_sum / students_count if students_count > 0 else 0


def avg_lecture_grade(lecturers, course):
    grades_sum = 0
    lecturers_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades_sum += sum(lecturer.grades[course])
            lecturers_count += len(lecturer.grades[course])
    return grades_sum / lecturers_count if lecturers_count > 0 else 0


# Вызов функций для подсчета средних оценок
avg_hw_grade_course = avg_hw_grade([student1, student2], course)
avg_lecture_grade_course = avg_lecture_grade([lecturer1, lecturer2], course)

print(f"Средняя оценка за домашние задания по курсу {course}: {avg_hw_grade_course}")
print(f"Средняя оценка за лекции по курсу {course}: {avg_lecture_grade_course}")

print(reviewer1)
print(reviewer2)

print(lecturer1)
print(lecturer2)

print(student1)
print(student2)
