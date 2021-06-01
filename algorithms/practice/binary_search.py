"""
Binary search
"""
from iterative_quick_sort import iterative_quick_sort


def binary_search(lst, element):
    """
    binary_search(lst: list, element) -> int

    Finds an element in sorted list.
    It works by repeatedly dividing in half the portion
    of the list that could contain the item, until it
    narrows down possible locations to one
    """
    start = 0
    end = len(lst)
    while True:
        index = (start + end) // 2
        if lst[index] == element:
            return index
        if lst[index] < element:
            start = index + 1
        elif lst[index] > element:
            end = index - 1


def main():
    """
    main()

    Main function to demonstrate program functionality
    """
    lst = [4, 3, 12, 1, 2, 7, 11, 34]
    iterative_quick_sort(lst)
    print(lst)
    print(binary_search(lst, 11))


if __name__ == '__main__':
    main()
