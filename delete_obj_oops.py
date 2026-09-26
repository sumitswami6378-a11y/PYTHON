class Mem :
    def __init__(self , name):

        self.name = name

s1 = Mem("sumit kumar")

del s1.name
print(s1.name)