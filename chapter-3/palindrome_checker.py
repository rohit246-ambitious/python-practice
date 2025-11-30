str1 = input("Enter a string to check if it's a palindrome: ").strip()
str2 = str1[::-1] # Reverse the string using slicing
print(f"The reverse of the string is: {str2}")
if str1 == str2:
    print(f'"{str1}" is a palindrome.')
else:
    print(f'"{str1}" is not a palindrome.')