class MyClass:

    course = "Python for Everybody"

    def __init__(self, students):
        self.students = students

    def get_total_students(self):
        print(f"The total number of students is {self.students}")

    def add_student(self):
        self.students = self.students + 1

    def thing(self, param1="Thing"):
        print(param1)


new_class = MyClass(100_000)

new_class.thing()

new_class.thing("Something else")

new_class.add_student()

new_class.get_total_students()
