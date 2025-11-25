list1=[2, 9, 1, 6, 4]
max_value = list1[0]
for num in list1:
    if num > max_value:
        max_value = num
print(f"The maximum value in the list is {max_value}.")