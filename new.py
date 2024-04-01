class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
        
    def rate_lr(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def average_grade(self):
        total_sum = 0
        total_count = 0
        for total_list in self.grades.values():
            total_sum += sum(total_list)
            total_count += len(total_list)
        return total_sum / total_count
    
    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за домашние задания: {self.average_grade()}\n' f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' f'Завершенные курсы: {", ".join(self.finished_courses)}'
    
    def __lt__(self, other):
        return self.average_grade() < other.average_grade()       
 
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
    
    def average_grade(self):
        total_sum = 0
        total_count = 0
        for total_list in self.grades.values():
            total_sum += sum(total_list)
            total_count += len(total_list)
        return total_sum / total_count
        
    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за лекции: {self.average_grade()}'
    
    def __lt__(self, other):
        return self.average_grade() < other.average_grade() 
    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}'

def average_rate_student(student_list, course):
    total_sum = 0
    total_count = 0
    for student in student_list:
        if course in student.courses_in_progress:
            for total_list in student.grades.values():
                total_sum += sum(total_list)
                total_count += len(total_list)
    return total_sum / total_count

def average_rate_lecturer(lecturer_list, course):
    total_sum = 0
    total_count = 0
    for lector in lecturer_list:
        if course in lector.courses_attached:
            for total_list in lector.grades.values():
                total_sum += sum(total_list)
                total_count += len(total_list)
    return total_sum / total_count

student1 = Student('Максим', 'Омельянюк', 'male')
student1.finished_courses += ['Введение в программирование']
student1.courses_in_progress += ['Git', 'Python']
student2 = Student('Ирина', 'Пахнян', 'female')
student2.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['Git', 'Python']

mentor1 = Mentor('Владимир','Клейман')
mentor1.courses_attached += ['Git', 'Python']
mentor2 = Mentor('Рафаэль', 'Арутюнян')
mentor2.courses_attached += ['Git', 'Python']

lecturer1 = Lecturer('Ольга', 'Апенина')
lecturer1.courses_attached += ['Git', 'Python']
lecturer2 = Lecturer('Анастасия', 'Рубежанская')
lecturer2.courses_attached += ['Git', 'Python']

reviewer1 = Reviewer('Владислав', 'Руденко')
reviewer1.courses_attached += ['Git', 'Python']
reviewer2 = Reviewer('Михаил', 'Ивлев')
reviewer2.courses_attached += ['Git', 'Python']

student1.rate_lr(lecturer1, 'Git', 10)
student1.rate_lr(lecturer1, 'Python', 10)
student1.rate_lr(lecturer2, 'Git', 9)
student1.rate_lr(lecturer2, 'Python', 9)
student2.rate_lr(lecturer1, 'Git', 10)
student2.rate_lr(lecturer1, 'Python', 10)
student2.rate_lr(lecturer2, 'Git', 9)
student2.rate_lr(lecturer2, 'Python', 9)

reviewer1.rate_hw(student1, 'Git', 1)
reviewer1.rate_hw(student1, 'Python', 1)
reviewer1.rate_hw(student2, 'Git', 2)
reviewer1.rate_hw(student2, 'Python', 2)
reviewer2.rate_hw(student1, 'Git', 1)
reviewer2.rate_hw(student1, 'Python', 1)
reviewer2.rate_hw(student2, 'Git', 2)
reviewer2.rate_hw(student2, 'Python', 2)

print(student1)
print(student2)
print(reviewer1)
print(reviewer2)
print(student1.average_grade())
print(student2.average_grade())
print(lecturer1.average_grade())
print(lecturer2.average_grade())

print(student1 < student2)
print(lecturer1 < lecturer2)

print(average_rate_student([student1, student2], 'Git'))
print(average_rate_student([student1, student2], 'Python'))

print(average_rate_lecturer([lecturer1, lecturer2], 'Git'))
print(average_rate_lecturer([lecturer1, lecturer2], 'Python'))