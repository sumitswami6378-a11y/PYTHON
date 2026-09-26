class Cars() :

    def __init__(self , brand, model, type ):
        self.brand = brand
        self.model = model
        self.type = type

c1 = Cars("mahindra" , 2026 , "petrol")

c2 = Cars("toyoto" , 2011 , "diesel")

c3 = Cars("mercedes" , 2009 , "petrol")

print(c1.type,c1.model,c1.brand)

print(c2.type,c2.model,c2.brand)

print(c3.type,c3.model,c3.brand)