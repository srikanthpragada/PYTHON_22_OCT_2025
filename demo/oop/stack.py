class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def isempty(self):
        return len(self.data) == 0

    @property
    def lastvalue(self):
        return  self.data[-1]

    @property
    def length(self):
        return len(self.data)

    def clear(self):
        self.data.clear()


s = Stack()
s.push(10)
s.push(20)

print(s.pop())
print(s.peek())

print(s.length)  # Property
print(s.lastvalue)   # Property

#print(Stack.__dict__)