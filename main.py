import random

courses_list = []
students_list = []
students_IDs_list = []

class Course:
    def __init__(self, course_name, course_class):
        self.course_ID = 1 + len(courses_list)
        self.course_name = course_name
        self.course_class = course_class


class Student:
    def __init__(self, student_ID, student_name, student_class):
        self.student_ID = student_ID
        self.student_name = student_name
        self.student_class = student_class
        self.Student_courses_list = []

    def add_course(self, course_name):

        for i in courses_list:
            if course_name == i.course_name:
                if self.student_class == i.course_class:
                    self.Student_courses_list.append(i.course_name)
                else:
                    print("class is not the same")
            else:

                print("course doesn't exist")

    def student_details(self):
        print("-----------------")
        print("Student ID \t\t Student name \t\t Studnet class \t\t Student courses")

        print(self.student_ID, "\t\t", self.student_name, "\t\t", self.student_class, "\t\t", self.Student_courses_list)


while True:
    try:
        choice = int(input("----------------------------\n"
                           "1)Add new student\n2)Remove Student\n3)Edit student\n"
                           "4)Display all students\n5)Create new course"
                           "\n6)Add course to student\n0)Exit\n----------------------------\nSelect choice please: "))
    except Exception:
        print("Please Enter number from the list :D")
        continue

    if choice == 1:
        student_name = input("Enter student name: ")
        while True:
            student_class = input("Enter student class from (A, B, C): ")
            if student_class in ['A', 'B', 'C']:
                break
        student_ID = random.randint(100, 101)
        while student_ID in students_IDs_list:
            student_ID = random.randint(100, 200)

        students_IDs_list.append(student_ID)
        student = Student(student_ID, student_name, student_class)
        students_list.append(student)
        print("-----------------")
        print("student ", student_name, "saved successfully")
        print("-----------------")

        student.student_details()
        print(students_IDs_list)


    elif choice == 2:
        x = True
        while x==True:

            if len(students_IDs_list) == 0:
                print("there are no students to search")
                break

            try:
                student_ID_check = int(input("Enter student ID (0 to exit): "))
            except Exception:
                print("Please Enter ID number :D")
                continue

            if student_ID_check in students_IDs_list:
                index_del = students_IDs_list.index(student_ID_check)
                del students_list[index_del]
                students_IDs_list.remove(student_ID_check)
                print("student with ID", student_ID_check, "is deleted successfully ")
                break
            elif student_ID_check ==0:
                break
            print("ID doesn't exist")



    elif choice == 3:
        print(choice)
    elif choice == 4:
        print(choice)


    elif choice == 5:
        course_name = input("Enter course name: ")
        while True:
            course_class = input("Enter course class from (A, B, C): ")
            if course_class in ['A', 'B', 'C']:
                break
        Course = Course(course_name, course_class)
        courses_list.append(Course)
        print("Course", course_name, "saved successfully in class", course_class)


    elif choice == 6:
        print(choice)


    elif choice == 0:
        print(students_IDs_list)
        exit()
    else:
        print("Please Enter number from the list :D")

