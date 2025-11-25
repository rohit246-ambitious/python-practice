#Q11.Use a dictionary comprehension to create a dictionary of squares.
my_squere_dict = {x:x**2 for x in range(1,11)}
print(my_squere_dict)


#Q12. Write a program to find the maximum value in a dictionary
# Define a dictionary
my_dict = {"a": 10, "b": 25, "c": 18, "d": 42}

higherval = max(my_dict.values())
print(higherval)

#Q13.Create a nested dictionary and access its elements.

my_dict2 = {'name':'rohit', 'city' : 'dom', 'pincode': 421202, 'other': {'language':'python', 'yerex':2, 'projects':2}}
print(my_dict2['other']['language'])

#Q14. Sort a dictionary by its keys
my_dict4 = {"a": 10, "b": 25, "c": 18, "d": 42}

sorted_dict = dict(sorted(my_dict4.items()))

print(sorted_dict)

sorted_dict_re = dict(sorted(my_dict4.items(), reverse=True))
print("Dictionary sorted by keys (descending):", sorted_dict_re)


#Q15 Write a program to find the sum of all values in a dictionary.

my_dict5 = {"a": 10, "b": 25, "c": 18, "d": 42}
val = 0
for key in my_dict5:
    val += my_dict5[key]

print(val)

#another way

sum_val = sum(my_dict5.values()) #using inbuild function
print(sum_val)

