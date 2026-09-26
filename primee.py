num = int(input("ENTER THE NUMBER = "))
count = 0
for i in range(2,num):
    if num % i == 0 :
        count = 1

print("sumit kumar")

if count == 1 :
    print(num,"is prime")

else:
    print("not prime")

