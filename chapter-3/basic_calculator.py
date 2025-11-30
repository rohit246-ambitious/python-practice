# Basic Calculator
def basic_calculator():
    print("Basic Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input")


# Advanced Calculator with Loop and Error Handling
def add(a,b):
    return a+b
    
def mul(a,b):
    return a*b

def minus(a,b):
    return a-b

def div(a,b):
    return a/b
    
while True:
    
    try:
        int1 = float(input("Enter 1st No.:: "))
        int2 = float(input("Enter 2st No.:: "))
    except ValueError:
        print("Please enter valid Number!")
        continue
    
    action = input("Which action you want to perform(+ - * /) :: ")
    try:
        if action == "+":
            print(f" {int1} + {int2} = {add(int1,int2)}")
        elif action == "-":
            print(f" {int1} - {int2} = {minus(int1,int2)}")
        elif action == "*":
            print(f" {int1} * {int2} = {mul(int1,int2)}")
        elif action == "/":
            if int2 == 0:
                raise ZeroDivisionError
            print(f"{int1} / {int2} = {div(int1,int2)}")
        else:
            print("❌ Please select right operator!")
    except ZeroDivisionError:
        print("❌ Error: Division by ZERO is not allowed!")
        continue
    except Exception as e:
        print("❌ Unexpected error:", e)
        continue

    toContune = input("Do you want to continue (yes/no): ").lower()
    if toContune != "yes" :
        print("Thank you for using the calculator!")
        break


