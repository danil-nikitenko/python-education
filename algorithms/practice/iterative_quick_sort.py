"""
Iterative quick sort
"""


def partition(lst, start, end):
    """
    partition(lst: list, start: int, end: int) -> int

    Rearranges the elements in list so that all elements that are less
    than pivot are to its left and all elements that are greater than or
    equal to pivot are to its right.
    Returns the pivot index
    """
    pivot = lst[end]
    index = start
    for i in range(start, end):
        if lst[i] < pivot:
            lst[i], lst[index] = lst[index], lst[i]
            index += 1
    lst[index], lst[end] = lst[end], lst[index]
    return index


def iterative_quick_sort(lst):
    """
    iterative_quick_sort(lst: list)

    Iterative implementation of quick sort
    """
    stack = []
    stack.append(0)
    stack.append(len(lst) - 1)

    while len(stack) > 0:
        end = stack.pop()
        start = stack.pop()
        while end - start >= 1:
            pivot_index = partition(lst, start, end)
            stack.append(pivot_index + 1)
            stack.append(end)
            end = pivot_index - 1


def main():
    """
    main()

    Main function to demonstrate program functionality
    """
    lst = [4, 3, 12, 1, 2, 7, 11, 34]
    iterative_quick_sort(lst)
    print(lst)


if __name__ == '__main__':
    main()
