class bikes :
    def __int__(self,name,year,model):

        self.name = name
        self.year = year
        self.model = model
    def __int__(self):
        self.type = type

        print("type is", self.type)
    
b1 = bikes("apache", 2000, 2016)
b2 = bikes("splendor", 3313 , 6666)
b1.type = "sfdgsdf"
print(b1.name,b1.model,b1.year,)

print(b2.name,b2.model,b2.year)

print(b1.type)