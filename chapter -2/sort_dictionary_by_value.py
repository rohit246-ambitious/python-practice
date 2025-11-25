d = {"apple": 3, "banana": 1, "cherry": 2}
sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_d)