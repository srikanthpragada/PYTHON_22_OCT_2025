class StackEmptyError(Exception):
    def __str__(self):
        return 'Stack is empty!'

class Stack_Iterator:
    def __init__(self, data):
        self.data = data
        self.pos = len(data) - 1

    def __next__(self):
        if self.pos < 0:
            raise StopIteration

        value = self.data[self.pos]
        self.pos -= 1
        return value


class Stack:
    def __init__(self):
        self.data = []

    def __iter__(self):
        return Stack_Iterator(self.data)

    def push(self, value):
        self.data.append(value)

    def pop(self):
        """
        Returns value at the top of the stack and removes it
        If stack is empty, it raises StackEmptyError exception
        :return: Value that is at the top of the stack
        """
        if self.isempty():
            raise StackEmptyError()

        return self.data.pop()

    def peek(self):
        if self.isempty():
            raise StackEmptyError()

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
#print(s.pop())
s.push(10)
s.push(20)
s.push(100)

#print(s.pop())
print(s.peek())

print(s.length)  # Property
print(s.lastvalue)   # Property

#print(Stack.__dict__)

for n in s:
    print(n)
