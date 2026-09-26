student = {

    "name" : "sumit",
    "roll no." : 2501921690056 ,
    "age" : 20 ,
    "branch" : "cse-h"

}

details = {

    "section" : "cseh2a"
}

empty ={ }

print(student)

print(empty)

print(len(student))
print(len(empty))

# .get returns none if the key is not exist


print(student["name"])
print(student["age"])
print(student["branch"])


# using get method

print(student.get("name"))

student["city"] = "RJ18"
print(student)

student["village"] = "swami sehi"

#delete

del student["branch"]
print(student)


print(student)

print(student)

details.clear()
print(details)

print("\n\n\n")
print(student.keys())
print(student.values())
print(student.items())

#using for loop

for keys in student:
    print(keys)

print("\n\n")
for key in student.keys():
    print(key)

for valus in student:
    print(student.values())

student["name"] = "karan"
print("name")