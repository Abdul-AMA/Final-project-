import random

courses_list = []
students_list = []
students_IDs_list = []
courses_names_list = []

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
        self.student_courses_list = []

    def add_course(self, course_name):

        for i in courses_list:
            if course_name == i.course_name:
                if self.student_class == i.course_class:
                    self.student_courses_list.append(i.course_name)
                else:
                    print("class is not the same")


    def student_details(self):

        print("  ",self.student_ID, "\t\t\t\t", self.student_name, "\t\t\t\t   ", self.student_class, "\t\t\t\t", self.student_courses_list)
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
        print("student", student_name, "saved successfully")
        print("-----------------")

        print("-----------------")
        print("Student ID \t\t Student name \t\t Student class \t\t Student courses")



        student.student_details()
    elif choice == 2:
        while True:

            if len(students_IDs_list) == 0:
                print("there are no students to search")
                break

            try:
                student_ID_check_remove = int(input("Enter student ID ( enter 0 to exit): "))
            except Exception:
                print("Please Enter ID number :D")
                continue

            if student_ID_check_remove in students_IDs_list:
                index_del = students_IDs_list.index(student_ID_check_remove)
                del students_list[index_del]
                students_IDs_list.remove(student_ID_check_remove)
                print("student with ID", student_ID_check_remove, "is deleted successfully ")
                break
            elif student_ID_check_remove ==0:
                break
            print("ID doesn't exist")
    elif choice == 3:
        while True:

            if len(students_IDs_list) == 0:
                print("there are no students to search")
                break

            try:
                student_ID_check_edit = int(input("Enter student ID ( enter 0 to exit): "))
            except Exception:
                print("Please Enter ID number :D")
                continue

            if student_ID_check_edit in students_IDs_list:
                index_edit = students_IDs_list.index(student_ID_check_edit)

                students_list[index_edit].student_name = input("Enter new student name: ")
                while True:
                    new_class = input("Enter student class from (A, B, C): ")
                    if new_class in ['A', 'B', 'C']:
                        students_list[index_edit].student_class = new_class
                        break
                print("Data of student with ID", student_ID_check_edit, "is edited successfully ")
                break
            elif student_ID_check_edit == 0:
                break
            print("ID doesn't exist")
    elif choice == 4:
        while True:
            if len(students_IDs_list) == 0:
                print("there are no students to search")
                break
            print("-----------------")
            print("Student ID \t\t Student name \t\t Student class \t\t Student courses")
            for i in  students_list:
                i.student_details()
            break
    elif choice == 5:
        course_name = input("Enter course name: ")
        while True:
            course_class = input("Enter course class from (A, B, C): ")
            if course_class in ['A', 'B', 'C']:
                break
        course = Course(course_name, course_class)
        courses_list.append(course)
        courses_names_list.append(course_name)
        print("Course", course_name, "saved successfully in class", course_class)
    elif choice == 6:
        while True:

            if len(students_IDs_list) == 0:
                print("there are no students")
                break
            if len(courses_list) == 0:
                print("there are no courses to add")
                break


            try:
                student_ID_check_add = int(input("Enter student ID ( enter 0 to exit): "))
            except Exception:
                print("Please Enter ID number :D")
                continue

            if student_ID_check_add in students_IDs_list:
                index_add_s = students_IDs_list.index(student_ID_check_add)
                while True:
                    course_add = input("Enter course name (enter 0 to exit): ")
                    if course_add in students_list[index_add_s].student_courses_list:
                        print("Course already exist!")
                        break
                    if course_add in courses_names_list:
                        index_add_c = courses_names_list.index(course_add)
                        if courses_list[index_add_c].course_class == students_list[index_add_s].student_class :
                            students_list[index_add_s].student_courses_list.append(course_add)
                            print("course",course_add,"is added successfully to student with ID",student_ID_check_add)
                            break
                        else:
                            print("course class is different than student class")
                    elif course_add == str(0):
                        break
                    else:
                        print("course doesn't exist")
                break
            elif student_ID_check_add == 0:
                break
            else:
                print("ID doesn't exist")
    elif choice == 0:
        exit()
    else:
        print("Please Enter number from the list :D")