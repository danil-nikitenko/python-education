"""
Binary search tree realization
"""


class BinarySearchTreeNode:
    """
    Represents a tree node.
    Stores node data, value to compare with other nodes,
    left child, right child and parent
    """
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
        """
        set_left(left: BinarySearchTreeNode)

        Sets left child
        """
        self.left = left

    def set_right(self, right):
        """
        set_right(right: BinarySearchTreeNode)

        Sets right child
        """
        self.right = right

    def set_parent(self, parent):
        """
        set_parent(parent: BinarySearchTreeNode)

        Sets parent
        """
        self.parent = parent

    def set_new_child(self, old_child_data, new_child):
        """
        set_new_child(old_child_data, new_child: BinarySearchTreeNode)

        Sets a new child
        """
        if self.left is not None and self.left.data == old_child_data:
            self.set_left(new_child)
        if self.right is not None and self.right.data == old_child_data:
            self.set_right(new_child)

    def delete_child(self, value):
        """
        delete_child(value)

        Deletes a child by value
        """
        if self.left is not None and self.left.data == value:
            self.left = None
        elif self.right is not None and self.right.data == value:
            self.right = None

    @staticmethod
    def get_value(data):
        """
        get_value(data)

        Returns a value to compare nodes
        """
        if isinstance(data, str):
            result = 0
            for char in data:
                result += ord(char)
            return result

        return data


class BinarySearchTree:
    """
    Represents binary search tree
    """
    def __init__(self, *items):
        self.root = None
        for item in items:
            self.insert(item)

    def insert(self, item):
        """
        insert(item)

        Inserts a node in tree
        """
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
        """
        lookup(item) -> BinarySearchTreeNode

        Searches a node by value.
        Raises ValueError if node is not in tree
        """
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
        """
        delete(item)

        Deletes a node by value
        """
        node = self.lookup(item)
        if node.left == node.right is None:
            node.parent.delete_child(item)
        elif node.left is not None and node.right is None:
            node.parent.set_new_child(item, node.left)
        elif node.right is not None and node.left is None:
            node.parent.set_new_child(item, node.right)
        else:
            min_right = self.search_min(node.right)
            self.delete(min_right.data)
            node.data = min_right.data
            node.value = min_right.value

    def print_tree(self, root, space):
        """
        print_tree(root: BinarySearchTreeNode, space: int) -> None

        Prints a tree to console
        """
        if root is None:
            return

        space += 10

        self.print_tree(root.right, space)

        print()
        for _ in range(10, space):
            print(end=" ")
        print(root.data)

        self.print_tree(root.left, space)

    @staticmethod
    def search_min(node):
        """
        search_min(node: BinarySearchTreeNode) ->  BinarySearchTreeNode

        Searches for node with minimal value in subtree
        """
        while True:
            if node.left is None:
                return node
            node = node.left


def main():
    """
    main()

    Main function to demonstrate program functionality
    """
    tree = BinarySearchTree(50, 40, 30, 35, 55)
    tree.insert('str')
    print('tree:\n')
    tree.print_tree(tree.root, 0)
    print('\nlookup(\'str\')\n')
    print(tree.lookup('str'), ': ', tree.lookup('str').data)
    tree.delete(50)
    print('\ntree.delete(50)')
    tree.print_tree(tree.root, 0)


if __name__ == "__main__":
    main()
