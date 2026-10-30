class Student:

    college = "ABC College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Instance method
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    # Class method
    @classmethod
    def show_college(cls):
        print("College:", cls.college)

    # Static method
    @staticmethod
    def is_pass(marks):
        return marks >= 40


s1 = Student("MK", 85)

s1.display()

Student.show_college()

print("Pass:", Student.is_pass(s1.marks))