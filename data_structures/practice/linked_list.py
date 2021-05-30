from itertools import count


class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next_item = None

    def next(self, next_item):
        self.next_item = next_item


class LinkedList:

    def __init__(self, *items):
        self.head = None
        self.tail = None
        self.size = 0
        for item in items:
            self.append(item)

    def __contains__(self, item):
        current = self.head
        while current is not None:
            if type(current) != type(item):
                if current.data == item:
                    return True
            if current == item:
                return True
            current = current.next_item
        return False

    def __getitem__(self, index):
        if index == 0:
            return self.head.data
        current = self.head
        for _ in range(index):
            if current.next_item is None:
                raise ValueError(f'{index}: index out of range')
            current = current.next_item
        return current.data

    def __str__(self):
        item = self.head
        list = []
        while item is not None:
            list.append(item.data)
            item = item.next_item
        return str(list)

    def __len__(self):
        return self.size

    def prepend(self, item):
        item = LinkedListNode(item)
        item.next(self.head)
        self.head = item
        self.size += 1

    def append(self, item):
        item = LinkedListNode(item)
        if self.head is None:
            self.head = item
        if self.tail is not None:
            self.tail.next(item)
        self.tail = item
        self.size += 1

    def lookup(self, item):
        count = 0
        current = self.head
        while current is not None:
            if current.data == item:
                return count
            current = current.next_item
            count += 1
        raise ValueError(f'{item} is not in list')

    def insert(self, index, item):
        item = LinkedListNode(item)
        if index == 0:
            item.next(self.head)
            self.head = item
            self.size += 1
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next_item
            if current.next_item is None:
                self.append(item.data)
                return
        self.size += 1
        item.next(current.next_item)
        current.next(item)

    def delete(self, index):
        if index == 0:
            self.head = self.head.next_item
            self.size -= 1
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next_item
            if self.tail == current:
                raise IndexError('Index out of range')

        self.size -= 1
        if current.next_item == self.tail:
            self.tail = current
            current.next_item = None
            return
        current.next_item = current.next_item.next_item

    def expand(self, size):
        if isinstance(size, int):
            for _ in range(size):
                self.append(0)


def main():

    a = LinkedList(0, 1, 2)
    a.prepend(10)
    a.delete(0)
    a.insert(0, 10)
    #a.append(0)
    # a.append(1)
    # a.append(6)
    #a.delete(5)
    print(a)
    print(len(a))
    lst = [0, 1, 3, 4]
    lst.insert(10, 2)
    #lst.remove(5)
    #lst.pop(5)
    #print(lst)



if __name__ == "__main__":
    main()

# if index == 0:
#     return self.head.data
# current = self.head
# for _ in range(index):
#     if current.next_item is None:
#         raise ValueError(f'{index}: index out of range')
#     current = current.next_item
# return current.data