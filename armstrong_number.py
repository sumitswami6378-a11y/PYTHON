num = int(input("ENTER THE NUMBER = "))
original = num

digits = len(str(num))
print("digits in the number = ",digits)

reverse = 0
while num > 0:
    last_digit = num % 10
    reverse = reverse + last_digit**digits
    num = num//10
print("sumit kumar")
if reverse == original:
    print("number is armstrong",original)
else:
    print("number is not armstrong",original)
