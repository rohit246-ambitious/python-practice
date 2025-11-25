#Q16. Use the pop() method to remove a key from a dictionary

my_dict2 = {'name':'rohit', 'city' : 'dom', 'pincode': 421202, 'other': {'language':'python', 'yerex':2, 'projects':2}}
my_dict2.pop('other')
print(my_dict2)

#Q17. Convert a dictionary to a list of tuples.
my_dict3 = {'name':'rohit', 'city' : 'dom', 'pincode': 421202, 'other': {'language':'python', 'yerex':2, 'projects':2}}
touple_list = list(my_dict3.items())
print(touple_list)

#other way

tuple_list = [(key, value) for key, value in my_dict3.items()]
print("List of tuples:", tuple_list)

#Q18. Create a dictionary from two lists using zip()

# Define two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

# Use zip() to combine the lists into a dictionary
my_dict = dict(zip(keys, values))

# Print the resulting dictionary
print("Created dictionary:", my_dict)

#Q19. Find all keys in a dictionary that have a specific value.
# Define a dictionary
my_dict6 = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 10}

# Specify the value to search for
target_value = 10

# Find all keys with the specific value
keys_with_value = [key for key, value in my_dict6.items() if value == target_value]

# Print the result
print(f"Keys with value {target_value}:", keys_with_value)

#Q20. Write a program to reverse a dictionary (keys become values and vice versa).
my_dict5 = {"a": 10, "b": 25, "c": 10}

reversed_dict = {value: key for key, value in my_dict5.items()}
print(reversed_dict)





    

