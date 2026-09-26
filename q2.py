tup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("ENTER THE NMBER TO BE SEARCHED : "))

for el in tup :
    if(el == x):
        print(x,"element found at index")
        break
    
else:
    print("element is not present")

    print(el)