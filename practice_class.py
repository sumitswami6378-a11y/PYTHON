class Student :
    def __init__(self,name ,physics, chemistry ,maths):
        self.name = name
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths

    def average(self):

        avg = (self.physics + self.maths + self.chemistry)/3
        print(avg)
    
s1 = Student("sumit swami" , 98, 89 ,85)

s1.average()
  
       