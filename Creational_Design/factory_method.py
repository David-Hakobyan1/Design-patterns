from abc import ABCMeta, abstractstaticmethod

class iperson(metaclass=ABCMeta):
    @abstractstaticmethod
    def person_method():
        """interface method"""

class Student(iperson):
    def __init__(self):
        self.name = "basic student name"

    def person_method(self):
        print("i am a student")

class Teacher(iperson):
    def __init__(self):
        self.name = "basic teacher name"

    def person_method(self):
        print("i am a teacher")

class personfactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "student":
            return Student()
        elif person_type == "teacher":
            return Teacher()
        print("invalid type")
        return -1

if __name__=="__main__":
    choice = input("what type of person do you want to create?\n")
    person = personfactory.build_person(choice)
    person.person_method()
