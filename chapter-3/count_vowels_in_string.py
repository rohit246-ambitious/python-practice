str1 = input("Enter a string to count vowels: ").strip()
vowels = "aeiouAEIOU"
count = sum(1 for char in str1 if char in vowels)
print(f"The number of vowels in the string is: {count}")


str1 = input("enter a string :: ")
vowels = ['a','e','i','o','u','A','E','I','O','U']
count = 0
for i in str1:
    if i in vowels:
        count+=1
print(f"The number of vowels in the string is: {count}")