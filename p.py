student = {

}


math = float(input("math marks = "))
physics = float(input("physics marks = "))
chemistry = float(input("chemistry marks = "))



print(student)
student.update({"math" : math})
student.update({"physics" : physics})
student.update({"chemistry": chemistry})

print(student)