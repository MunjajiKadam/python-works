class Student:

    college = "ABC College"

    # Instance method
    def show_student(self ):
        print("Student method after creating object")

    # Class method
    @classmethod
    def show_college(cls):
        print("College name method before creating object:", cls.college)


# Calling classmethod using class name
Student.show_college()

# Calling classmethod using object
s1 = Student()
s1.show_college()