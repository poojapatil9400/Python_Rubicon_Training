#Factorial of a number using recursion
def factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  
print(factorial(0))  