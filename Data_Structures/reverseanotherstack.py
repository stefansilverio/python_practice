class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def load_stack(self, item):
        self.items.append(item)

    def unload_stack(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)


stack = Stack()
for c in "Hello":
    stack.load_stack(c)

reverse = ""

for i in range(len(stack.items)):
    reverse += stack.unload_stack()

print(reverse)
