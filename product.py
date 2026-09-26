num = int(input("ENTER NUMBER = "))
product = 1

while num > 0 :
    digit = num % 10
    product = product*digit
    num = num // 10

print(product)