class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


p1 = Person('Jason', 25)
p2 = Person('Martin', 35)
p3 = Person('Richards', 28)
p4 = Person('Jason', 25)
people = [p1, p2, p3, p4]
print(p1)
print(str(p1))
print(p1.__str__())
print(p1 == p4)  # p1.__eq__(p4)

for p in sorted(people):
    print(p)

