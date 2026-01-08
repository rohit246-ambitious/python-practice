def addition(a, b):
    """Returns the sum of two numbers."""
    return a + b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))    
result = addition(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")