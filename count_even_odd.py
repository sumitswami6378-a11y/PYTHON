list = [1,5,5,5,2,1,7,5,4,6,44,6]
even = 0
odd = 0

for num in list:

    if num % 2 == 0 :
        even = even + 1 
    else :
        odd = odd + 1
print("even no. is", even)
print("odd no. is",odd)