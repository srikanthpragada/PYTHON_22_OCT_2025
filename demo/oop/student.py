class Student:
    def __init__(self, admno : int, name : str, totalfee : int, feepaid : int = 0):
        self.admno = admno
        self.name = name
        self.totalfee = totalfee
        self.feepaid = feepaid

    def getdue(self):
        return self.totalfee  - self.feepaid

    def payment(self, amount : int):
        self.feepaid += amount

s1 = Student(1, "Scott", 10000)
s1.payment(5000)
print(s1.getdue())

s2 = Student(2, "Andy", 15000, 5000)
s2.payment(10000)
print(s2.getdue())


