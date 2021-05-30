from linked_list import LinkedList


class Stack:

    def __init__(self, *items):
        self.stack = LinkedList()
        for item in items:
            self.push(item)

    def push(self, item):
        self.stack.prepend(item)

    def pop(self):
        if len(self.stack) == 0:
            raise ValueError('Stack is empty')
        item = self.stack.lookup(0)
        self.stack.delete(0)
        return item

    def peek(self):
        if len(self.stack) == 0:
            raise ValueError('Stack is empty')
        return self.stack.lookup(0)


stack = Stack()
stack.push('a')
stack.push('b')
stack.push('c')
print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.pop())
