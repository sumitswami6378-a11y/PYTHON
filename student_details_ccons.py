class Student :
    college = "GL BAJAJ" 
    def __init__(self,name,marks,rollno):
        self.name = name
        self.marks = marks
        self.rollno = rollno

Student_1 = Student("sumit kumar", 9.21 , 2501921690056)
Student_2 = Student("kartik poonia", 9.00 , 14654654)
Student_3 = Student("yatin lamba",9.11,4546546)

print(Student_1.name , Student_1.marks , Student_1.rollno)

print(Student_2.name,Student_2.marks,Student_2.rollno)

print(Student_3.name,Student_3.marks,Student_3.rollno,Student_3.college)