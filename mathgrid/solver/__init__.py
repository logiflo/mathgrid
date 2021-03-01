"""Solver module
"""
from enum import Enum

class Operator(Enum):
    """Operator enumerate
    """
    ADDITION = 1
    SUBSTRACTION = 2
    PRODUCT = 3
    DIVISION = 4
    POWER = 5


def math_operations(num1: int or float, operator: Operator, num2: int or float) -> int or float:
    """Solve a basic math operation.

    Args:
        num1 (int or float): Left value.
        operator (str): a string operator, which can be: addition (+),
            substraction (-), product (*), division(/), power(^).
        num2 (int or float): Right value.

    Raises:
        TypeError: If one or both values aren't a integer or float.
        ZeroDivisionError: If in a division the divider is 0.
        ValueError: Operation not supported.

    Returns:
        int or float: The result of the operation.
    """

    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Not an integer or float")

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
    else:
        raise ValueError("Operation not supported")

    return solution


print(math_operations(6, Operator.ADDITION, 2))
