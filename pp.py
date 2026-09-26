class stu :
    def __int__(self,name,physics,math,chem):
        self.name = name
        self.physics = physics
        self.math = math
        self.chem = chem

    def avg(self,avg):

        self.average= (self.math + self.physics + self.chem)/3

s1 = stu("sumit",56,66,64)

print(s1.name,s1.physics,s1.math,s1.chem)
s1.avg()
        