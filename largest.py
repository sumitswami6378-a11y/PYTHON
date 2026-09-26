num = int(input("Enter a number: "))
largest = 0

while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    num = num // 10

print("largest digit is:", largest)