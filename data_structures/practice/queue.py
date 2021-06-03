"""
Queue realization
"""
from linked_list import LinkedList


class Queue:
    """
    Represents queue
    """
    def __init__(self, *items):
        self.queue = LinkedList()
        for item in items:
            self.enqueue(item)

    def __len__(self):
        return len(self.queue)

    def qsize(self):
        return len(self.queue)

    def enqueue(self, item):
        """
        enqueue(item)

        Adds an item to the end of the queue
        """
        self.queue.append(item)

    def dequeue(self):
        """
        dequeue()

        Removes and returns the item at the beginning of the queue.
        Raises ValueError if queue is empty
        """
        if len(self.queue) == 0:
            raise ValueError('Queue is empty')
        item = self.queue[0]
        self.queue.delete(0)
        return item

    def peek(self):
        """
        peek()

        Returns the item at the beginning of the queue without removing it.
        Raises ValueError if queue is empty
        """
        if len(self.queue) == 0:
            raise ValueError('Queue is empty')
        return self.queue[0]


def main():
    """
    main()

    Main function to demonstrate program functionality
    """
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print('peek():')
    print(queue.peek())
    print('\ndequeue():')
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())


if __name__ == "__main__":
    main()
