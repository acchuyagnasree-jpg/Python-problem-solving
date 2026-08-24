class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if not self.items:
            return "Stack is empty"
        return self.items[-1]

    def display(self):
        print("Stack:", self.items)


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

print("Top:", stack.peek())
print("Removed:", stack.pop())

stack.display()
