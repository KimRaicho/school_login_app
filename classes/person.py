class Person:
    def __init__(self, name: str, age: int = 0):
        assert age >= 0, f"Age {age} should be greater or equal to 0"

        self.name = name
        self.age = age

    def person_details_printer(self):
        print(f"""
Name: {self.name}
Age:  {self.age} """)



