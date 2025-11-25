#Q6. Concatenate two tuples.

t1 = (1,2,3,4,5,6,78)
t2 = (5,3,6,5,9,0,7,8)

print(t1 + t2)

#Q7. Write a program to find the index of an element in a tuple.
t3 = (1,2,3,4,5,6,78)
element_input = int(input('enter the element that you want to know the index :: '))
print(t3.index(element_input))

#Q8. Use slicing to extract a portion of a tuple.

t4 =(6,7,3,5,9,1,90,56,34,45,78)
print(t4[:5])

#Q9. Create a nested tuple and access its elements.
t5 = ((1,3,5,7,9,11,13,15), (4,6,8,10,12,14,16))
print(t5[1])

#Q10. Unpack a tuple into separate variables.
# Define a tuple
my_tuple = (10, 20, 30)

# Unpack the tuple into variables
a, b, c = my_tuple

# Print the variables
print("a:", a)
print("b:", b)
print("c:", c)


