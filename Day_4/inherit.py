#Inheritance
#single inheritance 
class Rectangle:
    def rec_are(self,height,width):
        area = height*width
        print(area)
class Square(Rectangle):
    def squ_area(self,side):
        area = side*side
        print(area)
obj= Square()
obj.rec_are(10,20)
obj.squ_area(10)

#multiple inheritance 
class demo:
    def student(self,name):
        print("Name",name)
class demo1:
    def studata(self, email):
        print("Email",email)
class demo2(demo,demo1):

    def age(self, age):
     print("age",age)
obj = demo2()
obj.student("Pooja")
obj.studata("Pooja@1210")
obj.age(20)


