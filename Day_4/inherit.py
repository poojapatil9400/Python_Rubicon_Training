#Inheritance
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
