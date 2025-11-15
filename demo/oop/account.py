class Account:
    def __init__(self, acno, customer, balance):
        self.acno = acno
        self.customer = customer
        self.__balance = balance

    def getbalance(self):
        return self.__balance


a = Account(1, 'Andy', 10000)
print(a.getbalance())
#print(a.customer, a.__balance)

print(a.__dict__)
#print(a._Account__balance)  #?

