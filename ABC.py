class Student :

    def __init__(self,name,math , chem , physics):

        self.name = name
        self.math = math
        self.chem = chem
        self.physics = physics

    def avg(self):

        average = (self.math +self.chem +self.physics)/2
        print("average of the student is = ",average)

    @staticmethod 
    def college():
       
     print("GL BAJAJ")


s1 = Student("sumit ", 8.77,9.21,0)
s2 = Student("karan", 84,87,81)

print(s1.name)
s1.avg()
print(s2.name)
s2.avg()

s1.college()