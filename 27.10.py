import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='logs.log',
                    filemode='w',
                    format="%(levelname)s:%(asctime)s - %(message)s")

class NameSurname:
    def __init__(self, name, surname):
        if(type(name) != str):
            raise TypeError(f"Name is not a string ")
        if(type(surname) != str):
            raise TypeError(f"Surname is not a string '{type(surname) }'")
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



try:

    first_student = Student("Vlad", "Karlinskyi", 12)
    logging.info(f'Create new student {first_student.ns.name} {first_student.ns.surname}')
    second_student = Student("Oleg", True, 12)
except Exception as error:
    print(error)
    logging.error(error)

