num = int(input("ENTER THE NUMBER = "))
sum = 0
for i in range (1,num-1,1):

   if(num % i == 0):
    sum = sum + i
    print(i)

print(sum,"is sum of digits digits")

if(sum == num):
    print(num,"is palindrome")

else:
   print(num," is not palindrome")


print("sumit kumar")