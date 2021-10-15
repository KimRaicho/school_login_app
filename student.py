import person as p


class Student(p.Person):

    def __init__(self, name: str, age: int, student_id):
        super().__init__(name, age)
        self.id = student_id

    def display(self):
        print("====================STUDENT DETAILS=======================")
        p.Person.person_details_printer(self)
        print(f"Id: {self.id}")
