class Cars:
  
   brand = "mahindra"

   def __init__(self,name,color,model): # THIS IS PARAMETERIZED CONSTRUCTOR
      
      self.name = name
      self.color = color
      self.model = model


car1 = Cars("thar" , "black" ,2019)

car2 = Cars("scorpio","black" , 2025)

car3 = Cars("camper" , "white" , 2023)

print(car1.name ,car2.name ,car3.name)
print(car1.color ,car2.color ,car3.color)
print(car1.model ,car2.model ,car3.model)
print(car1.brand ,car2.brand ,car3.brand)
