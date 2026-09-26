class Account:
    def __init__(self, balance , acc):

        self.balance = balance
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("the amount of",amount,"is debit")
        #self.balance = balance
        print("balance",self.balance)

    def credit(self,amount):
        self.balance += amount
        print("the amount", amount,"is credited account")
        print("balance",self.balance)

    def balance(self):
        print(self.balance)
        
    
p1 = Account(20000 , 101)

print(p1.balance,p1.account_no)

p1.credit(1000)
p1.debit(100000)
p1.credit(40000)
p1.credit(1000000)