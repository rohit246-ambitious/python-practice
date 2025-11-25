#Q1. Create a set with 5 elements.

s1 = {1,2,3,4,5,6}
print(type(s1))

#Q2. Add an element to a set
s2 = {4,5,6,7,8,9,2,3,4}

s2.add(1)
print(s2)

#Q3.Remove an element from a set using remove() and discard().

s3 = {1,2,3,4,5,6,7,8,9,0}

s3.remove(0)
s3.discard(1)
print(s3)

#Q4. Perform union and intersection of two sets.

s4 = {45,33,56,1,7,9,3,55,67,23}
s5 = {34,45,55,99,89,56,44,67,23}

s6 = s4.union(s5)
s7 = s4.intersection(s5)
print(s6)
print(s7)

#Q5. Write a program to find the difference between two sets.
s8 = {45,33,56,1,7,9,3,55,67,23}
s9 = {34,45,55,99,89,56,44,67,23}

s10 = s8.difference(s9)
print(s10)
