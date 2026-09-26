class Car:

    color = "black"
    model = 2019
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")


class Toyoto(Car):
    def __init__(self,name):
        self.name = name

class Top(Toyoto) :

    def __init__(self,type,drive):
        self.type = type
      


c1 = Toyoto("fortuner","petrol","4wd",59)
c2 = Toyoto("enova","diesel","4wd",55)

c1.start()

