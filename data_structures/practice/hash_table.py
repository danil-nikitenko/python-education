"""
Hash table realization
"""
from linked_list import LinkedListNode, LinkedList


class HashTableNode(LinkedListNode):
    """
    Represents hash table node.
    Stores node key, value and next node
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_item = None


class HashTableLinkedList:
    """
    A linked list variation to work with hash tables
    """
    def __init__(self, items=None):
        self.head = None
        self.tail = None
        if items:
            for key in items:
                self.append(key, items[key])

    def __getitem__(self, key):
        current = self.head
        while True:
            if current.key == key:
                return current.value
            if current.next_item is None:
                raise KeyError(key)
            current = current.next_item

    def __setitem__(self, key, value):
        index = self.delete(key)
        self.insert(index, key, value)

    def __contains__(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return True
            current = current.next_item
        return False

    def __str__(self):
        item = self.head
        lst = []
        while item is not None:
            lst.append((item.key, item.value))
            item = item.next_item
        return str(lst)

    def prepend(self, key, value):
        """
        prepend(key, value)

        Adds an item to list head
        """
        item = HashTableNode(key, value)
        item.next(self.head)
        self.head = item

    def append(self, key, value):
        """
        append(key, value)

        Adds an item to list tail
        """
        item = HashTableNode(key, value)
        if self.head is None:
            self.head = item
        if self.tail is not None:
            self.tail.next(item)
        self.tail = item

    def lookup(self, key):
        """
        lookup(key) -> int

        Returns item index by key.
        Raises KeyError if key is not in hash table
        """
        count = 0
        current = self.head
        while current is not None:
            if current.key == key:
                return count
            current = current.next_item
            count += 1
        raise KeyError(f'{key} is not in hash table')

    def insert(self, index, key, value):
        """
        insert(index: int, key, value) -> None

        Inserts an item to list by index
        """
        item = HashTableNode(key, value)
        current = self.head
        for _ in range(index - 1):
            current = current.next_item
            if current.next_item is None:
                self.append(item.key, item.value)
                return
        item.next(current.next_item)
        current.next(item)

    def delete(self, key):
        """
        delete(key) -> int

        Deletes an item from list by key and returns its index.
        Raises KeyError if key is not in list
        """
        if self.head.key == key:
            self.head = self.head.next_item
            return 0

        current = self.head.next_item
        prev = self.head
        count = 0
        while current is not None:
            if current.key == key:
                prev.next(current.next_item)
                break
            prev = current
            current = current.next_item
            count += 1
        else:
            raise KeyError(f'{key}: key is not in list')

        if current == self.tail:
            self.tail = prev
        return count


class HashTable:
    """
    Represents a hash table.
    Stores list of hash table items
    """
    def __init__(self, size, items=None):
        self.list = LinkedList()
        self.list.expand(size)
        if items:
            for key in items:
                self.insert(key, items[key])

    def hash_function(self, key):
        """
        hash_function(key) -> int

        Returns a hash value of a key.
        Raises TypeError if key type is wrong
        """
        if isinstance(key, int):
            return key % len(self.list)

        if isinstance(key, str):
            result = 0
            for char in key:
                result += ord(char)
            return result % len(self.list)

        raise TypeError(f'Wrong type {key}: {type(key)}')

    def insert(self, key, value):
        """
        insert(key, value) -> None

        Inserts an item in hash table
        """
        index = self.hash_function(key)
        if isinstance(self.list[index], HashTableLinkedList):
            if key in self.list[index]:
                self.list[index][key] = value
            else:
                self.list[index].prepend(key, value)
            return
        item = HashTableLinkedList()
        item.prepend(key, value)
        self.list.delete(index)
        self.list.insert(index, item)

    def lookup(self, key):
        """
        lookup(key)

        Returns a value by key.
        Raises KeyError if key is not in hash table
        """
        index = self.hash_function(key)
        if key not in self.list[index]:
            raise KeyError(f'{key}: key is not in hash table')
        return self.list[index][key]

    def delete(self, key):
        """
        delete(key)

        Deletes an item from hash table by key.
        Raises KeyError if key is not in hash table
        """
        index = self.hash_function(key)
        if key not in self.list[index]:
            raise KeyError(f'{key}: key is not in hash table')
        self.list[index].delete(key)


def main():
    """
    main()

    Main function to demonstrate program functionality
    """
    hash_table = HashTable(10)
    hash_table.insert(1, 12)
    hash_table.insert(2, 31)
    hash_table.insert(3, 14)
    hash_table.insert('lies', 1)
    hash_table.insert('foes', 2)
    print('lookup():\n')
    print('1: ', hash_table.lookup(1))
    print('2: ', hash_table.lookup(2))
    print('3: ', hash_table.lookup(3))
    print('\'lies\': ', hash_table.lookup('lies'))
    print('\'foes\': ', hash_table.lookup('foes'))
    print('\ndelete(2): \n')
    hash_table.delete(2)
    try:
        print(hash_table.lookup(2))
    except KeyError as ex:
        print(ex)


if __name__ == "__main__":
    main()
