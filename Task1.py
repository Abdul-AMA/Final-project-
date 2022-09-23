import random

courses_list = []
student_list = []

def search_studint():
    number = int(input("Enter student number to search: "))
    if number in student_list:
        print(number, " exist")
    else:
        print(number, " doesn't exist")


def search_course():
        name = input("Enter course name to search: ")
        if name in courses_list:
            print(name, " exist")
        else:
            print(name, " doesn't exist")


class Course:
    def __init__(self,name,class_n):
        self.__course_name = name
        self.__course_class = class_n
        courses_list.append(self.get_course_name())

    def get_course_name(self):
        return self.__course_name

    def set_course_name(self, name):
        self.__course_name = name

    def get_course_class(self):
        return self.__course_class

    def set_course_class(self, class_num):
        self.__course_class = class_num



class Student:
    def __init__(self,name,class_n):
        self.__student_num = random.randint(100,200)
        self.__student_name = name
        self.__student_class = class_n
        self.courses_list = []
        student_list.append(self.get_student_num())


    def get_student_num(self):
        return self.__student_num


    def get_student_name(self):
        return self.__student_name

    def set_student_name(self, name):
        self.__student_name = name

    def get_student_class(self):
        return self.__student_class

    def set_student_class(self, class_num):
        self.__student_class = class_num

    def add_course(self,course_name):
        self.courses_list.append(course_name)


course1 = Course("Java" , "A")
course2 = Course("Python" , "B")
course3 = Course("HTML", "C")

student1 = Student("ali","B")
student2 = Student("hani","A")
student3 = Student("mohamed","B")
student4 = Student("alex" , "C")

print(student_list)
print(courses_list)

search_studint()
search_studint()
search_course()
search_course()