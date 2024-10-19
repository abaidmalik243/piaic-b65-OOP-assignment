class Universaty:
    def __init__(self, name):
        self.uniName = name


class Person:
    def __init__(self, name):
        self.personName = name

class Teacher(Person):
    def __init__(self, name):
        Person.__init__(self, name)


class Student(Person):
    def __init__(self, name):
        Person.__init__(self, name)

class Faculty(Teacher, Student):
    def __init__(self, name):
        Person.__init__(self, name)


class Class(Teacher, Student):
    def __init__(self, name):
        Person.__init__(self, name)



universaty = Universaty("GCUF")
teacher = Teacher("Sir Zia")
student = Student("Abaidullah")


print(f"Universaty Name is: {universaty.uniName}")
print(f"Teacher Name is: {teacher.personName}")
print(f"Student Name is: {student.personName}")

    

    