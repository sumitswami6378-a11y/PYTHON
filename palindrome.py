num = int(input("ENTER NUM = "))
reverse = 0
original = num
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if(original == reverse):
     print("palindrome")
else :
      print("not palindrome")