num = int(input("ENTER NUMBER = "))
largest = 0
while num >0 :

    digit = num % 10
    if(digit > largest):
        largest = digit
    num = num // 10

print("LARGEST VALUE OF THE DIGIT IS =",largest)