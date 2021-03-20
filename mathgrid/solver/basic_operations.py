"""Basic operations module
"""

from ordered_enum import OrderedEnum


class Operator(OrderedEnum):
    """Operator ordered enumerate.
    """
    ADDITION = '+'
    SUBSTRACTION = '-'
    PRODUCT = '*'
    DIVISION = '/'
    POWER = '^'


def basic_operation(num1, num2, operator):
    """Solve a basic math operation.

    Raises:
        ZeroDivisionError: If in a division the divider is 0.

    Returns:
        int or float: result of the operation.
    """
    if operator == Operator.ADDITION:
        solution = num1 + num2
    elif operator == Operator.SUBSTRACTION:
        solution = num1 - num2
    elif operator == Operator.PRODUCT:
        solution = num1 * num2
    elif operator == Operator.DIVISION:
        if num2 == 0:
            raise ZeroDivisionError
        solution = num1 / num2
    elif operator == Operator.POWER:
        solution = num1 ** num2

    return solution
