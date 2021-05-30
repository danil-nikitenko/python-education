from linked_list import LinkedList


class Queue:

    def __init__(self, *items):
        self.queue = LinkedList()
        for item in items:
            self.enqueue(item)

    def __len__(self):
        return len(self.queue)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) == 0:
            raise ValueError('Queue is empty')
        item = self.queue[0]
        self.queue.delete(0)
        return item

    def peek(self):
        if len(self.queue) == 0:
            raise ValueError('Queue is empty')
        return self.queue[0]


def main():
    queue = Queue(1, 2, 3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())


if __name__ == "__main__":
    main()
