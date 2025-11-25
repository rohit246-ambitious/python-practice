str1 = input("Enter a string: ")
words = str1.split() # Split the string into words based on spaces creating a list of words
word_count = {}  # Initialize an empty dictionary to store word frequencies
for word in words:  # Iterate through each word in the list
    word = word.lower()  #Convert the word to lowercase to ensure case-insensitivity
    if word in word_count:  
        word_count[word] += 1  #Increment its count by 1
    else:  
        word_count[word] = 1  # Initialize its count to 1 
print("Word frequencies:")  # Print a header for the output
for word, count in word_count.items():  
    print(f"{word}: {count}")  # Print each word along with its frequency