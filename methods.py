class Student :
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def hello(self):
        print("hello ", self.name)

    def marks(self):
        print(self.marks)

s1 = Student("sumit swami ", 97)

s1.hello()

s1.marks()
    