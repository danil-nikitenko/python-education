
class BinarySearchTreeNode:

    def __init__(self, data):
        if isinstance(data, (int, float, str)):
            self.data = data
            self.value = self.get_value(self.data)
            self.left = None
            self.right = None
            self.parent = None
        else:
            raise TypeError(f'Wrong type {data}: {type(data)}')

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_parent(self, parent):
        self.parent = parent

    def set_new_child(self, old_child_data, new_child):
        if self.left is not None and self.left.data == old_child_data:
            self.set_left(new_child)
        if self.right is not None and self.right.data == old_child_data:
            self.set_right(new_child)

    def delete_child(self, value):
        if self.left is not None and self.left.data == value:
            self.left = None
        elif self.right is not None and self.right.data == value:
            self.right = None

    @staticmethod
    def get_value(data):

        if isinstance(data, (int, float)):
            return data
        if isinstance(data, str):
            sum = 0
            for char in data:
                sum += ord(char)
            return sum


class BinarySearchTree:

    def __init__(self, *items):
        self.root = None
        for item in items:
            self.insert(item)

    def insert(self, item):
        item = BinarySearchTreeNode(item)
        if self.root is None:
            self.root = item
        else:
            current = self.root
            while True:
                if item.value < current.value:
                    if current.left is None:
                        current.set_left(item)
                        item.set_parent(current)
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.set_right(item)
                        item.set_parent(current)
                        break
                    current = current.right

    def lookup(self, item):
        value = BinarySearchTreeNode.get_value(item)
        current = self.root
        while True:
            if current.data == item:
                return current
            if value < current.value:
                if current.left is None:
                    raise ValueError(f'{item} not in tree')
                current = current.left
            else:
                if current.right is None:
                    raise ValueError(f'{item} not in tree')
                current = current.right

    def delete(self, item):
        node = self.lookup(item)
        if node.left == node.right is None:
            node.parent.delete_child(item)
        elif node.left is not None and node.right is None:
            node.parent.set_new_child(item, node.left)
        elif node.right is not None and node.left is None:
            node.parent.set_new_child(item, node.right)
        else:
            min_right = self.search_min(node.right)
            node.data = min_right.data
            node.value = min_right.value
            min_right.parent.delete_child(min_right.data)

    def print_tree(self, root, space):
        # Base case
        if root is None:
            return

        # Increase distance between levels
        space += 10

        # Process right child first
        self.print_tree(root.right, space)

        # Print current node after space
        # count
        print()
        for _ in range(10, space):
            print(end=" ")
        print(root.data)

        # Process left child
        self.print_tree(root.left, space)

    @staticmethod
    def search_min(node):
        while True:
            if node.left is None:
                return node
            node = node.left



tree = BinarySearchTree(50, 40, 30, 35, 55)
print(tree.lookup(50))
tree.delete(50)
tree.print_tree(tree.root, 0)
#tree.delete(50)
#print(tree.lookup(50))
a = [None, None]
if a[0] == a[1] is None:
    print('yes')


