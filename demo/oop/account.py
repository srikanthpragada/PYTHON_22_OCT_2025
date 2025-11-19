class Account:
    def __init__(self, acno, customer, balance):
        self.acno = acno
        self.customer = customer
        self.__balance = balance

    def getbalance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError(f'Invalid Amount [{amount}] for Deposit. ')


a = Account(1, 'Andy', 10000)
try:
    a.deposit(-10000)
except ValueError as ex:
    print("Error :", ex)

print(a.getbalance())
# print(a.customer, a.__balance)

print(a.__dict__)
# print(a._Account__balance)  #?
