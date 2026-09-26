num = int(input("ENTER NUM = "))

smallest = 9
while num > 0 :
    digit = num % 10
    if(smallest > digit):
        smallest = digit
    num = num // 10

print(smallest," is the smallest digit of the number ")