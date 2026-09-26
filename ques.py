list = (1,4,9,16,25,36,49,56,81,100)
x = int(input("ENTER NUMBER : "))
i = 0
for el in list:
    if(el == x):
        print(x,"is found at",i)
        break
    else:
        print(el)
        i=i+1
print("END OF THE LOOP")