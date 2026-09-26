list = [55,5,4,5,4,4,54,4]
list_1 = []

for i in list:
    if i not in list_1:
        list_1.append(i)
print(list_1)