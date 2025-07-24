#basic calculator 
print("Welcome to the basic calculator!")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Please select an operation (1-4): ")
if choice in ['1', '2', '3', '4']:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if choice == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please select a valid operation (1-4).")
# --- IGNORE ---
# This code is a basic calculator that performs addition, subtraction, multiplication, and division.
# It prompts the user to select an operation and input two numbers, then displays the result.
