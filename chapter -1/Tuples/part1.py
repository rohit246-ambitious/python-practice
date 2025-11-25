#Q1. Create a tuple with 5 elements and print it

t1= (1,2,3,4,5,6,7)
print(t1)
print(f'type of t1 is {type(t1)}')

#Q2. Access the second element of a tuple.

t2 = (9,2,3,4,5,6,7)
element_want = int(input('enter a index element you want :: '))
second_ele = t2[element_want]
print(f'index {element_want} present element {second_ele} ')

#Q3.Check if an element exists in a tuple.

t3 = (4,5,6,3,4,2,8,9)
element_want = int(input('enter element that you want to check if present or not in the tuple :: '))
if element_want in t3:
    print(f'{element_want} element4 present in tuple')
else:
    print(f'{element_want} element not present in tuple')

#Q4.Write a program to find the length of a tuple.
t4 = (4,5,6,3,4,2,8,9)
print(len(t4))

#Q5.Convert a list to a tuple and vice versa.
list1 = [1,3,5,7,9,10,12,14,16]
t5 = tuple(list1)
print(f'type of {type(t5)}')
list4= list(t5)
print(f'type of {type(list4)}')
