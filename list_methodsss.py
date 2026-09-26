list = [1,5,6,7,8,9,71]

list.append(4)
print(list)
list.append(56)
list.append(45)

print(list)

list.extend([41,5,3,78,6,46,64])
print(list)

#insert at specific position
list.insert(2,100)
print(list)

#remove of an element  

list.remove(78)
list.remove(5)
print(list)

#pop

list.pop()
print(list)
list.pop()
print(list)
list.pop()
print(list)

#clear all elements

#list.clear()
#print(list)

#index of an element 
index = list.index(4)
print("index of an element=",index)

#count
count = list.count(3)
print(count)

#sorting

print(list.sort())

#reverse
list = [1,5,6,7,8,9,71]
list.reverse()
print(list)

#len

print("length=",len(list))

#maximum of the list

max = max(list)
print(max)

#minimum of the list

min = min(list)
print(min)


