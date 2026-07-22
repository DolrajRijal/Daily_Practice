# Stack implementation using Python list

class Stack:
    def __init__(self):
        self.stack = []

    # Add element
    def push(self, item):
        self.stack.append(item)
        print(item, "pushed into stack")

    # Remove element
    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
            return

        item = self.stack.pop()
        print(item, "popped from stack")

    # Show top element
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return

        print("Top element:", self.stack[-1])

    # Display stack
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return

        print("Stack elements:", self.stack[::-1])


# Driver code
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

s.peek()

s.pop()

s.display()