"""
Linked list realization
"""


class LinkedListNode:
    """
    Represents a linked list node.
    Stores node data and reference to next list node
    """
    def __init__(self, data):
        self.data = data
        self.next_item = None

    def next(self, next_item):
        """
        next(next_item: LinkedListNode)

        Sets a reference to next node
        """
        self.next_item = next_item


class LinkedList:
    """
    Represents linked list.
    Stores list head, tail, size
    """
    def __init__(self, *items):
        self.head = None
        self.tail = None
        self.size = 0
        for item in items:
            self.append(item)

    def __contains__(self, item):
        current = self.head
        while current is not None:
            if not isinstance(current, type(item)):
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
        lst = []
        while item is not None:
            lst.append(item.data)
            item = item.next_item
        return str(lst)

    def __len__(self):
        return self.size

    def prepend(self, item):
        """
        prepend(item)

        Adds an item at the beginning of the list
        """
        item = LinkedListNode(item)
        item.next(self.head)
        self.head = item
        self.size += 1

    def append(self, item):
        """
        append(item)

        Adds an item at the end of the list
        """
        item = LinkedListNode(item)
        if self.head is None:
            self.head = item
        if self.tail is not None:
            self.tail.next(item)
        self.tail = item
        self.size += 1

    def lookup(self, item):
        """
        lookup(item) -> int

        Returns the node index by value.
        Raises ValueError if there is no node with this value in the list
        """
        count = 0
        current = self.head
        while current is not None:
            if current.data == item:
                return count
            current = current.next_item
            count += 1
        raise ValueError(f'{item} is not in list')

    def insert(self, index, item):
        """
        insert(index: int, item) -> None

        Inserts an item to the list by index
        """
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
        """
        delete(index: int) -> None

        Deletes an item from the list by index.
        Raises IndexError if index is out of range
        """
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
        """
        expand(size: int)

        Expands a list by given value.
        Used to implement the hash table
        """
        if isinstance(size, int):
            for _ in range(size):
                self.append(0)


def main():
    """
    main()

    Main function to demonstrate program functionality
    """
    lst = LinkedList(0, 1, 2)
    print('list:')
    print(lst)
    print('\nprepend(10):')
    lst.prepend(10)
    print(lst)
    print('\nappend(3):')
    lst.append(3)
    print(lst)
    print('\nlookup(2):')
    print(lst.lookup(2))
    print('\ninsert(2, 5):')
    lst.insert(2, 5)
    print(lst)
    print('\ndelete(1):')
    lst.delete(1)
    print(lst)


if __name__ == "__main__":
    main()
