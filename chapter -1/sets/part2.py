#Q6. Check if a set is a subset of another set.

s4 = {45,33,56,1,7,9,3,55,67,23}
s5 = {34,45,55,99,89,56,44,67,23}

subset_is = s4.issubset(s5)
print(subset_is)

#Q7. Convert a list with duplicate elements into a set.

l1 = [4,3,5,6,7,2,4,3,9,0,1,1,7,10]

s10 = set(l1)
print( s10)


#Q8. Write a program to check if two sets are disjoint.
s11 = {45,33,56,1,7,9,3,55,67,23}
s12 = {34,45,55,99,89,56,44,67,23}

s13 = s11.isdisjoint(s12)
print(s13)

#Q9. Create a frozen set and try modifying it.
# Create a frozenset
my_frozenset = frozenset([1, 2, 3, 4, 5])

# Try modifying the frozenset
try:
    my_frozenset.add(6)  # Frozenset does not support the add() method
except AttributeError as e:
    print(f"Error: {e}")

try:
    my_frozenset.remove(3)  # Frozenset does not support the remove() method
except AttributeError as e:
    print(f"Error: {e}")

# Print the frozenset
print("Frozenset:", my_frozenset)

#10.Write a program to find the symmetric difference between two sets.

s15 = {45,33,56,1,7,9,3,55,67,23}
s16 = {34,45,55,99,89,56,44,67,23}

s20 = s15.symmetric_difference(s16)
print(s20)