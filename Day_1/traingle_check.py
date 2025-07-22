#take three angle of traingle and check whether it can form a triangle or not
angle1 = int(input("Enter the first angle of triangle: "))  
angle2 = int(input("Enter the second angle of triangle: "))
angle3 = int(input("Enter the third angle of triangle: "))
if angle1 + angle2 + angle3 == 180:
    print("The angles can form a triangle") 
else:
    print("The angles cannot form a triangle")
