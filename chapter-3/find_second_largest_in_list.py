# Finding the second largest element in a list
lis = [10, 20, 4, 45, 99]
lis.sort()
print(lis)
print("Second largest element is:", lis[-2])

# Alternative method without using sort() using bubble sort
lis1 = [11,33,22,0,44,55]
for i in range(0,len(lis1),1):
    for j in range(i+1,len(lis1),1):
        if lis1[i] > lis1[j]:
            temp = lis1[i]
            lis1[i] = lis1[j]
            lis1[j] = temp
print(lis1)
print(f"Second largest element is :: {lis1[len(lis1)-2]}")

# Alternative method without using sort() using insertion sort
lis2 = [11,33,22,0,44,55]
for i in range(1,len(lis2)):
    key = lis2[i]
    j=i-1
    
    while j>=0 and lis2[j]>key:
        lis2[j+1] = lis2[j]
        j-=1
        
    lis2[j+1] = key
    
print(lis2)
print(f"Second largest element is :: {lis2[len(lis2)-2]}")