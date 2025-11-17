class A:
    def __init__(self):
        self.name = 'A'

    def process(self):
        # print(type(self))
        print("Process in A")
        print(self.name)   # Access name from C


class B:
    def process(self):
        print("Process in B")


class C(A, B):
    def __init__(self):
        self.name = 'C'

    def process(self):
        # super().process()
        A.process(self)
        B.process(self)


obj = C()
obj.process()
