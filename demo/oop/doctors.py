class Doctor:
    def __init__(self, name, dept):
        self.__name = name
        self.__dept = dept

    def show(self):
        print("Name: ", self.__name)
        print("Dept: ", self.__dept)


class Resident(Doctor):
    def __init__(self, name, dept, salary):
        super().__init__(name, dept)
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def show(self):
        super().show()
        print("Salary : ", self.__salary)


class Consultant(Doctor):
    def __init__(self, name, dept, visit, rate):
        super().__init__(name, dept)
        self.__visit = visit
        self.__rate = rate

    def show(self):
        super().show()
        print("Visit: ", self.__visit)
        print("Rate: ", self.__rate)

    def get_salary(self):
        return self.__visit * self.__rate


r = Resident("John", "Dentist", 70000)
r.show()
print("Net Salary:", r.get_salary())

c = Consultant("Mike", "Cardiologist", 20, 2000)
c.show()
print("Net Salary:", c.get_salary())
