num = int(input("ENTER THE NUMBER ="))

large =0
while num > 0:
    digit = num % 10

    if digit > large:
        large = digit

    num = num // 10

print("sumit kumar")
print("largest digit of the given number is",large)