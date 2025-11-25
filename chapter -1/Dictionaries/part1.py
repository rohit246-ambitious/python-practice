#Q1. Create a dictionary with 3 key-value pairs.

dct1 = {'key1': '56', 'key2': 'rohit','key3': 'rasik'}
print(dct1)

#Q2.Add a new key-value pair to a dictionary.

# Define a dictionary
my_dict = {"name": "Alice", "age": 25}

my_dict['city'] = 'domb'

print(my_dict)

#Q3.Update the value of an existing key in a dictionary

my_dict2 = {'name': 'Alice', 'age': 25, 'city': 'domb'}

print(my_dict['city'])

#Q4.Delete a key-value pair from a dictionary using del.

my_dict3 = {'name': 'Alice', 'age': 25, 'city': 'domb'}

del my_dict3['city']

print(my_dict3)

#Q5.Write a program to iterate through a dictionary and print all keys.
# Define a dictionary
my_dict4 = {"name": "Alice", "age": 25, "city": "Mumbai"}

# Iterate through the dictionary and print all keys
print("Keys in the dictionary:")
for key in my_dict4:
    print(key)
