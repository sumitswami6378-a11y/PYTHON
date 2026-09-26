def largest (num1,num2,num3):

    if(num1 > num2 and num1 > num3):
        print(num1,"is largest")

    elif(num2 > num1 and num2 > num3):
        print(num2,"is greater")

    else:
        print(num3,"is largest")

        return largest


large = largest(2,1,9)
print(largest)

large = largest(5,6,0)
print(largest)

large = largest(4,3,0)
print(largest)

large = largest(7,33,44)
print(largest)