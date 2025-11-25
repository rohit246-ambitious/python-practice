#Q1.Write a Python program to declare a variable x and assign it the value 10. Print its value.

x = 10
print(x)

#Q2.Change the value of a variable from 5 to 15
x1 = 5
x1=15
print(x1)

#Q3. Identify the data types of the following: 10, "Hello", 3.14, True.
x2 = 10
str1= 'Hello'
x3 = 3.14
x4 = True

print(f'type of x2 = {type(x2)}')
print(f'type of str1 = {type(str1)}')
print(f'type of x3 = {type(x3)}')
print(f'type of x4= {type(x4)}')


#Q4. Create variables of different data types (int, float, string, bool) and print their types using type().

x2 = 333
str1= 'Hello rohit'
x3 = 45.45
x4 = False

print(f'type of x2 = {type(x2)}')
print(f'type of str1 = {type(str1)}')
print(f'type of x3 = {type(x3)}')
print(f'type of x4= {type(x4)}')

#Q5. Swap the values of two variables without using a third variable.

v1 = 12
v2 = 34
v1 = v1 + v2
v2 = v1 - v2
v1 = v1 - v2
print(v1)
print(v2)