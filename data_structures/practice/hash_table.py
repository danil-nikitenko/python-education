from linked_list import LinkedListNode, LinkedList


class HashTableNode(LinkedListNode):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_item = None


class HashTableLinkedList(LinkedList):

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
        list = []
        while item is not None:
            list.append((item.key, item.value))
            item = item.next_item
        return str(list)

    def prepend(self, key, value):
        item = HashTableNode(key, value)
        item.next(self.head)
        self.head = item

    def append(self, key, value):
        item = HashTableNode(key, value)
        if self.head is None:
            self.head = item
        if self.tail is not None:
            self.tail.next(item)
        self.tail = item

    def lookup(self, key):
        count = 0
        current = self.head
        while current is not None:
            if current.key == key:
                return count
            current = current.next_item
            count += 1
        raise ValueError(f'{item} is not in list')

    def insert(self, index, key, value):
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
            raise KeyError(key)

        if current == self.tail:
            self.tail = prev
        return count


class HashTable:

    def __init__(self, size, items=None):
        self.list = LinkedList()
        self.list.expand(size)
        if items:
            for key in items:
                self.insert(key, items[key])

    def hash_function(self, key):

        if isinstance(key, int):
            return key % len(self.list)

        if isinstance(key, str):
            sum = 0
            for char in key:
                sum += ord(char)
            return sum % len(self.list)

        raise ValueError(f'Wrong type {key}: {type(key)}')

    def insert(self, key, value):
        index = self.hash_function(key)
        if type(self.list[index]) == HashTableLinkedList:
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
        index = self.hash_function(key)
        if key not in self.list[index]:
            raise KeyError(key)
        return self.list[index][key]

    def delete(self, key):
        index = self.hash_function(key)
        if key not in self.list[index]:
            raise KeyError(key)
        self.list[index].delete(key)


def main():
    hash_table = HashTable(3)
    hash_table.insert(1, 1)
    hash_table.insert(2, 2)
    hash_table.insert(3, 15)
    #hash_table.insert(4, 4)
    #print(len(hash_table.list))
    print(hash_table.lookup(3))
    #print(3%3)
    #hash_table.delete(2)
    #print(hash_table.lookup(1))


if __name__ == "__main__":
    main()
