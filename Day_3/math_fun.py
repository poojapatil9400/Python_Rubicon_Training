#math functions using import math
import math
def square_root(x):
    return math.sqrt(x)
print(square_root(16))  # Output: 4.0

def power(base, exponent):
    return math.pow(base, exponent)
print(power(2, 3))  # Output: 8.0

def logarithm(x, base=10):
    return math.log(x, base)
print(logarithm(100))  # Output: 2.0 (base 10)

def factorial(n):
    return math.factorial(n)   
print(factorial(5))  # Output: 120

#sine
def sine(angle):
    return math.sin(math.radians(angle))
print(sine(30))  # Output: 0.49999999999999994 (sin(30 degrees))

s3=math.tan(45)
print(s3)  # Output: 1.0 (tan(45 degrees))

s4 =math.cos(60)
print(s4)  # Output: 0.5000000000000001 (cos(60 degrees))

s5 = math.asin(0.5)
print(s5)  # Output: 0.5235987755982989 (asin

s6 = math.acos(0.5)
print(s6) 

s7=math.sqrt(5.4)
print(s7)  # Output: 2.3166041405695605 (sqrt(5.4))

s8=math.ceil(5.4)
print(s8)  # Output: 6 (ceil(5.4))


s9=math.floor(5.4)
print(s9)  # Output: 5 (floor(5.4))

s10=math.pi(4.5)
print(s10)

s11=math.sin(4.5)
print(s11)  # Output: 3.141592653589793 (pi)

