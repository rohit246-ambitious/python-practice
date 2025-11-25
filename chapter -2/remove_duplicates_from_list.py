li1 = [1, 2, 2, 3, 4, 4, 5]
li2 = []
for i in li1:
    if i not in li2:
        li2.append(i)
print(f"list after removing dublicates:{li2}")