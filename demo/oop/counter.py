class Counter:
    #constructor
    def __init__(self, value = 0):
        # Object attributes
        self.value = value

    # Methods
    def increment(self, step = 1):
        self.value += step

    def getvalue(self):
        return self.value


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

