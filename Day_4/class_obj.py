#class and object in python
class Student:
    name = "Pooja"
    age = 20
    roll_no = 101
    college = "MIT"
    def showInfo(self):
        print(s1.name)
        print(s1.age)
        print(s1.roll_no)
        print(s1.college)
# Create an instance of the Student class
s1 = Student()
s1.showInfo()

class Student2:
    def __init__(self, name, age,roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        # Constructor to initialize the attributes
        print("Constructor called")
        print("Name:", self.name)
        print("Age:", self.age)  
        print("Roll No:", roll_no)


class Student3:
    def __init__(self):
        print("hii i am non parameterized constructor")
    def Info(self):
        print("This is a method of Student class")
        print("Pooja")
        print("20")
s3 = Student3()  # Create an instance of the Student class
s3.Info()  # Call the Info method
