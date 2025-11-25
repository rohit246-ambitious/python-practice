#Q6.Reverse a list using slicing.
list1 = [1,2,3,4,5,6,7,8,9]
print(list1[::-1])

#Q7.Find the length of a list using len().

list2 = [1,2,3,4,5,6,7,8,9]
print(len(list2))

#Q8.Check if an element exists in a list.
element = 5
my_list = [1, 2, 3, 4, 5]

# Using the 'in' operator
exists = element in my_list
print(exists)  # Output: True

#Q9. Create a list of numbers from 1 to 10 using range().

list4 = list(range(1,11)) #here 1 is start number and 11 is a index
print(list4)

#Q10.Sort a list in ascending and descending order.

list5 = [5,6,3,7,8,1,67,54,33,90,100,88,2,9]
list5.sort()
print(list5)
list5.sort(reverse=True)
print(list5)

#alternative way of doing 
list6 = [5,6,3,7,8,1,67,54,33,90,100,88,2,9]

assendingList = sorted(list6)
print(assendingList)
desendingList = sorted(list6, reverse=True)
print(desendingList)





