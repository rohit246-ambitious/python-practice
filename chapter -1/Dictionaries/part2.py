#Q6. Iterate through a dictionary and print all values.

my_dict = {'name':'rohit', 'city' : 'dom', 'pincode': 421202}

for value in my_dict:
    print(my_dict[value])

#Q7. Check if a key exists in a dictionary.
my_dict = {'name':'rohit', 'city' : 'dom', 'pincode': 421202}
key_check = 'age'

if key_check in my_dict:
    print(f'"{key_check}" key exist in dict')
else:
    print(f'"{key_check}" key not exist in the dict')

#Q8. Get the value of a key using the get() method.

my_dict = {'name':'rohit', 'city' : 'dom', 'pincode': 421202}
print(my_dict.get('name'))

#Q9. Merge two dictionaries.

my_dict = {'name':'rohit', 'city' : 'dom', 'pincode': 421202}
my_dict2 = {'age':25, 'department' : 'IT', 'possion': 'developer'}

#muiltiple way to do that
#1st 

#usinsg update method

my_dict.update(my_dict2)

print(my_dict) #the update method modifiy the origin dict

#2nd 
my_dict = {'name':'rohit', 'city' : 'dom', 'pincode': 421202}
my_dict2 = {'age':25, 'department' : 'IT', 'possion': 'developer'}

mergerDict = my_dict | my_dict2

print(mergerDict)

#3rd
my_dict = {'name':'rohit', 'city' : 'dom', 'pincode': 421202}
my_dict2 = {'age':25, 'department' : 'IT', 'possion': 'developer'}

mergerDict2 = {**my_dict, **my_dict2}

print(mergerDict2)

#4th
from itertools import chain
my_dict = {'name':'rohit', 'city' : 'dom', 'pincode': 421202}
my_dict2 = {'age':25, 'department' : 'IT', 'possion': 'developer'}

mergerDict3 = dict(chain(my_dict.items(),my_dict2.items()))

print(mergerDict3)

#Q10 . Write a program to count the frequency of elements in a list using a dictionary.
#two way of doint this 

#1st 

my_list = [1,2,3,2,3,1,4,5,3,4,6,7,8,6,5,7,3,1,5,2,2]

frq_list = {}

for element in my_list:
    frq_list[element] = frq_list.get(element,0) +1

print(frq_list)

#2nd

from collections import Counter

frq_list2 = Counter(my_list)

print(dict(frq_list2))


