list = [-6,5,0,56,-54,4,6,44,-4,6,-66]
positive = []
negative = []
zero = []

for num in list:
    
    if num > 0:
     positive.append(num)
     

    elif num < 0 :
        negative.append(num)
     
    else:
        zero.append(num)
   

print(positive)
print(negative)
print(zero)
