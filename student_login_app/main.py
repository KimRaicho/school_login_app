from classes import student as s


def create_student():
    print('Enter student name: ')
    student_name = input()
    print('Enter student age: ')
    student_age = int(input())
    print('Enter student id: ')
    student_id = int(input())

    student = s.Student(student_name, student_age, student_id)

    student.display()


if __name__ == '__main__':
    create_student()
