num = int(input("ENTER THE NUM="))

original = num
reverse = 0

while num >0 :
    digit = num % 10
    reverse = reverse*10 + digit
    num = num // 10

print("sumit kumar")

if(reverse == original):
    print("NUMBER IS PALINDROME",original)

else:
    print("NUMBER IS NOT PALLINDROME",original)