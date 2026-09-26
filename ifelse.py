a = int(input("ENTER THE VALUE OF A :"))
b=int(input("ENTER THE NUMBER OF B : "))

c=int(input("ENTER THE NUMBER OF C :"))

if(a>b and a>c):
    print(a,"is greater than b and c")

elif(b>a and b>c):
    print(b,"is greater than a and c")

else:
    print(c,"is greater than a and b")