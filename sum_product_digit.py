num = int(input("ENTER NUMBER="))

sum = 0
product  = 1
while num > 0:

    digit = num % 10
    sum = sum + digit
    product = product * digit

    num = num // 10
print("sumit kumar")


print("sum of the digit is=",sum)
print("product of the digit is=",product)