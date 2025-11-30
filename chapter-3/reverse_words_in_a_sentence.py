str1 = input("Enter a sentence to reverse its words: ").strip()
words = str1.split()
reversed_words = " ".join(words[::-1])
print(f"The sentence with words reversed is: {reversed_words}")

str1_a = input("enter a string :: ")
str2 = str1_a.split()
str3 = ""
for i in range(len(str2) - 1,-1,-1):
    str3 = str3 + str2[i]+" "
print(str3)