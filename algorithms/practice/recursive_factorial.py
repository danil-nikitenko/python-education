"""
Recursive factorial
"""


def factorial(number):
    """
    factorial(number: int) -> int

    Finds the factorial of a number in a recursive way
    """
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)


def main():
    """
    main()

    Main function to demonstrate program functionality
    """
    print(factorial(5))


if __name__ == '__main__':
    main()
