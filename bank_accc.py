class Bank:

    branch = "state bank of india"

    def __init__(self , balance ,acc):

        self.balance = balance
        self.acc = acc

    def debit(self,amount):

        self.debit = amount
        self.balance -= amount

        print(amount,"should be debit")
        print(self.balance,"remaining")

    def credit(self,amount):
        self.credit = amount
        self.balance +=  amount
        print(amount,"is credited")
        print(self.balance,"remain")

a1 = Bank(50000 , 25115665)
a2 = Bank(14000 , 5646456546)
print(a1.balance , a1.acc)

a1.credit(10000)


a1.debit(40000)


a2.debit(10000)
