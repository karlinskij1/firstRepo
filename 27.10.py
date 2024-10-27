class NameSurname:
    def __init__ (self, name, surname):
        self.name = name
        self.surname = surname

class Student:
    student_amount = 0
    def __init__ (self,name, surname , age, height=160):
        self.ns = NameSurname(name, surname)
        self.age = age
        self.height = height
        Student.student_amount += 1

    def printStudent(self):
        print(f'Name: {self.ns.name}')
        print(f'Surname: {self.ns.surname}')
        print(f'Age: {self.age}')
        print(f'Height: {self.height}')

    def Birthday(self):
        self.age += 1
        print(f'Happy Birthday to {self.ns.name}. Now you {self.age}!')

print(f'before creating Student object {Student.student_amount}')
first_student = Student("vlad", "karlinskij", 12)
first_student.printStudent()
print(f'after creating Student object {Student.student_amount}')


first_student.Birthday()
