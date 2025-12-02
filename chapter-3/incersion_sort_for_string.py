list1 = ['rohit','utkarsh','sambha','ram','shankar','anju','ru','a']

for i in range(1,len(list1),1):
    key = list1[i]
    j=i-1
    
    while j>=0 and len(list1[j]) > len(key):
        list1[j+1] = list1[j]
        j-=1
        
    list1[j+1] = key
    
print(list1)