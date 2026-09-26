def div(num):

    if num % 3 == 0:
        print("num is divide by 3")

    elif num % 5 == 0:
        print("num is divisible by 5")

    elif num % 3 and num % 5:
        print("num is divisible by both 3 and 5")

    else:
        print("num is not divisible by none")


div(55)
div(15)
div(45)
div(78)