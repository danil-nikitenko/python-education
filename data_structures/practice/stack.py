"""
Stack realization
"""
from linked_list import LinkedList


class Stack:
    """
    Represents stack
    """
    def __init__(self, *items):
        self.stack = LinkedList()
        for item in items:
            self.push(item)

    def push(self, item):
        """
        push(item)

        Inserts an item at the top of the stack
        """
        self.stack.prepend(item)

    def pop(self):
        """
        pop()

        Removes and returns the item at the top of the stack.
        Raises ValueError if stack is empty
        """
        if len(self.stack) == 0:
            raise ValueError('Stack is empty')
        item = self.stack[0]
        self.stack.delete(0)
        return item

    def peek(self):
        """
        peek()

        Returns the item at the top of the stack without removing it.
        Raises ValueError if stack is empty
        """
        if len(self.stack) == 0:
            raise ValueError('Stack is empty')
        return self.stack[0]


def main():
    """
    main()

    Main function to demonstrate program functionality
    """
    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.push('c')
    print('peek():')
    print(stack.peek())
    print('\npop():')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


if __name__ == "__main__":
    main()
