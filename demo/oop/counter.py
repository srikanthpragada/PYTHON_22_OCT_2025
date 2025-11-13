class Counter:
    #constructor
    def __init__(self, value = 0):
        # Object attributes
        self.init_value = value
        self.value = value

    # Methods
    def increment(self, step = 1):
        self.value += step

    def decrement(self, step = 1):
        self.value -= step

    def getvalue(self):
        return self.value

    def reset(self):
        self.value = self.init_value

    @classmethod
    def create_counter(cls, value):
        return cls(value)

nc = Counter.create_counter(10)
print(nc.getvalue())

# Create an object
c = Counter()
# call methods
c.increment()
c.increment(5)
#print(c.value)  # not a good practice
print(c.getvalue())

c2 = Counter(100)
c2.increment(10)
print(c2.getvalue())
c2.reset()
print(c2.getvalue())


