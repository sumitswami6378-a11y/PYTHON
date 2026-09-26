def leap_year(year):
   if(year %4 == 0):
       print(year,"is leap year")

   elif(year % 100 and year % 400 == 0):
       print(year,"is leap year")

   else:
       print(year,"is not leap year")

print("SUMIT KUMAR")
leap_year(2016)
