"""Calculator module."""


class Calculator:
    """Calculator class.

    Provides methods for addition, subtraction, multiplication and division of two numbers."""

    @staticmethod
    def addition(arg1, arg2):
        """addition(arg1, arg2)

        Returns the sum of numbers arg1 and arg2."""
        return arg1 + arg2

    @staticmethod
    def subtraction(arg1, arg2):
        """subtraction(arg1, arg2)

        Returns the difference of numbers arg1 and arg2."""
        return arg1 - arg2

    @staticmethod
    def multiplication(arg1, arg2):
        """multiplication(arg1, arg2)

        Returns the product of numbers arg1 and arg2."""
        return arg1 * arg2

    @staticmethod
    def division(arg1, arg2):
        """division(arg1, arg2)

        Returns the quotient of numbers arg1 and arg2."""
        return arg1 / arg2
