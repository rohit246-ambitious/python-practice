#Q1. Write a program to concatenate two strings.
str1 = "rohit"
str2 = "rasik"

print(str1 +" "+ str2)

#Q2. Reverse a string using slicing.
str3 = "rohit"

print(str3[::-1])

#Q3. Check if a string is a palindrome.

str5 = "rohit"
str6 = "level"

print(str5 == str5[::-1])
print(str6 == str6[::-1])

#Q4. Count the number of vowels in a string

vowels = "aeiouAEIOU"
str7 = "rohit rasik"

count = 0
for char in str7:
    print(char)
    if char in vowels:
        count += 1
print(count)

#Q5. Replace all spaces in a string with underscores (_).
str8 = "rohit rasik is a good boy"

str8 = str8.replace(" ", "_")
print(str8)
