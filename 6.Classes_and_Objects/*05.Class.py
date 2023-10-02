class Class:
    students = []
    grades = []
    __students_count = 22

    def __init__(self, name):
        self.name = name

    def add_student(self, name: str, grade: float):
        if Class.__students_count > 0:
            Class.__students_count -= 1
            Class.students.append(name)
            Class.grades.append(grade)

    def get_average_grade(self):
        average = sum(Class.grades) / len(Class.students)
        return average

    def __repr__(self):
        string_students = ", ".join(Class.students)
        return f"The students in {self.name}: {string_students}. Average grade: {Class.get_average_grade(self):.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
