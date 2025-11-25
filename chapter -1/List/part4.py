#Q16.Create a list of squares of numbers from 1 to 5.

#after Loop learn

#Q17.Check if a list is empty.

list2 = [10,11,12,13,14,15,16,17]
print()
#after conditions learn


#Q18.Convert a string to a list of words.

# Define the string
input_string = "Convert this string to a list of words"

# Convert string to a list of words
word_list = input_string.split()

# Print the result
print("List of words:", word_list)

#Q19.Write a program to print the second largest number in a list.

list2 = [10,11,12,13,14,15,16,17]
list2Max = max(list2)
#templist = llist2Max -> its create reference of the main list that further issue if you make chnages in templist same chnages done in main list
templist = list2.copy() #this is correct way to do that make a copy of main list
templist.remove(list2Max)
print(max(templist))

#Q20.Slice a list to get the first 3 elements.
list2 = [10,11,12,13,14,15,16,17]
print(list2[:3]) #in slice index start from 1 not 0 

