student = {

"name" : "sumit",

"ROLL NO. " : 56 ,

"SECTION" : "g2a",

"MARKS" : [89,56,78,96,48,65],

"SUBJECT" : ("COA", "MATH", "PHYSICS")

}

print(student)

print(student["name"])
student["name"] = "kartik"

print(student["SUBJECT"])

print(student)

# IF WE ADD SURNAME 

student["surname"] = "swami"

print(student["surname"])