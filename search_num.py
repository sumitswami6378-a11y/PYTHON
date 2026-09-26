list = range( 1,10+1,1)
i=0
for el in list:
    if(el % 7 == 0):
        print(el,"is found at index ",i)
        break
    else:
     print(el)
     i=i+1