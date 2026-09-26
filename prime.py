num = int(input("ENTER THE NUM = "))
if(num ==0):
     print("not Prime")

     if(num > 1):
      for i in range(2,num,1):

       if(num % i ==0):
         print("not prime")

     else:
            print(" prime")

