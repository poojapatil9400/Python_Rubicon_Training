#Logical and Relational operators
x=int(input("Enter a  first number: "))
y=int(input("Enter second number: "))
z=int(input("Enter a third number: "))
if x>y and x>z:
    print(x," is greater")  
if y>x and y>z:
    print(y,"is greater")
if z>x and z>y:
    print(z ,"is greater")

#Assignment Operator

x1 =19
y1 =4
x1+= y1
print(x1)

x2 =19
y2 =4
x2/= y2
print(x2)

x3 =19
y3 =4
x3-= y3
print(x3)

x4 =19
y4 =4
x4*= y4
print(x4)

x5 =19
y5 =4
x5%= y5
print(x5)

#bitwise
x6=6
x7=3
print("x&y =",x6&x7)
print("x|y =",x6|x7)
print("x>>y =",x6>>x7)
print("x<<y =",x6<<x7)
print("x^y =",x6^x7)

#membership operator

list=['raj','jiya','tina','pihu']
print("raj" in list)
print("mitu" in list)

print("raj" not in list)
print("mitu"  not in list)

#identity operator
a=10
b=10
c=20
print(a is b)
print(a is not b)
print(a is c)
print(a is not c)


print("  ")
list ="raj","demo","jiya"
print("raj" in list)

# Comparison and Conditional Statements 

m = int (input("Enter a number 1 :"))
n = int (input("Enter a number 2 :"))
if m>n:
    print(m, "is greater than ", n) 
else:
    print(m , "is less than ", n)    
print("  ")

no = int (input("Enter your marks: "))
if no>60:
    print("first class")
elif no>50:
    print("second class")
elif no>40:
    print("third class")
else:
    print("fail")
print("  ")


# Nested if statements
num = 5
if num > 2:
    if num < 3:
        print("Hello")
    print("Hi")




    