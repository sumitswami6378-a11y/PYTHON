
num = int(input("Enter a number: "))

smallest = 1

while num > 0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num = num // 10

print("Smallest digit is:", smallest)