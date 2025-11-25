#Q11. Write a Python program to check if a variable is defined.

#Q12. Perform arithmetic operations (addition, subtraction, multiplication, division) on two variables.

a = 34
b = 16

add = a + b
into= a*b
div = a/b
sub= a-b
print(f'add = {add}, into = {into}, div = {div}, sub = {sub}')

#inbuild methods 
import operator

print(f'add = {operator.add(a,b)}')
print(f'muilti = {operator.mul(a,b)}')
print(f'div = {operator.truediv(a,b)}')
print(f'sub = {operator.sub(a,b)}')
print(f'floor division = {operator.floordiv(a,b)}' )
print(f'Mod of value = {operator.mod(a,b)}')
print(f'Pow = {operator.pow(a,b)}')
print(f'neg of  vslue {a}')
print(f'pos = {operator.pos(a)}')
print(f'abs = {operator.abs(a)}')

#Q13:Assign None to a variable and print its type. 

v4 = None
print(type(v4))

#Q14. . Perform floor division and modulus on two numbers.

p1 = 10
p2 = 6

floorDiv = p1 // p2
modulas = p1 % p2

print(f'floor division {floorDiv} and modulus {modulas}')

#Q15. Print the memory address of a variable using id().

v3 = 5
print(id(v3))

#Q14 : Remove leading and trailing whitespace from a string.

# String with leading and trailing whitespace
text = "   Hello, World!   "
# Remove the whitespace
trimmed_text = text.strip()

# Print the results
print("Original string:", repr(text))  # Use repr() to show whitespace clearly
print("Trimmed string:", repr(trimmed_text))

#anather way

text = "   Hello"
print(text.lstrip())

text = "Hello   "
print(text.rstrip())

#Q15. Replace all occurrences of a substring in a string.

# Original string
text = "I like apples. Apples are tasty."

# Substring to be replaced
target_substring = "Apples"

# Replacement substring
replacement_substring = "oranges"

# Replace all occurrences
result = text.replace(target_substring, replacement_substring)

# Print the result
print("Original string:", text)
print("Modified string:", result)



