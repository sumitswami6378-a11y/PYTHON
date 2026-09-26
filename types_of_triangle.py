def triangle(side1,side2,side3):

    if(side1 == side2 == side3):
        print("EQUILATERAL TRIANGLE")

    elif(side1 != side2 != side3):
        print("SCALENE TRIANGLE")

    else:
        print("ISOCELES TRIANGLE")

triangle(side1=52,side2=52,side3=52)
triangle(45,48,41)