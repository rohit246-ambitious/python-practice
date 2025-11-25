#Q6.Convert a float 3.5 into an integer.
v1 = 3.5
print(type(round(v1)))

#Q7. Write a program to check if a variable is of type integer.

v2= 45
v3 = 45.8
print(isinstance(v2, int))
print(isinstance(v3,int))

#Q.8 Use a single line of code to assign the same value to three variables a, b, c.

a=b=c= 45
print(f'a ={a}, b = {b}, c ={c} ')

#Q9. Create a variable name and store your name in it. Print a message like "Hello, [name]!".

name = 'rohit'
print(f'my name is {name}!')

#Q10. Take input from the user and print the entered value.

input1 = int(input('enter value here : '))
print(input1)