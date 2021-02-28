"""Solver module
"""


def math_operations(num1: int or float, operator: str, num2: int or float) -> int or float:
    """Solve a basic math operation.

    Args:
        num1 (int or float): Left value.
        operator (str): a string operator, which can be: addition (+),
            substraction (-), product (*), division(/), power(^).
        num2 (int or float): Right value.

    Raises:
        ValueError: If the operator is not supported or in a division the divider
            is 0.
        TypeError: If one or both values aren't a integer or float.

    Returns:
        int or float: The result of the operation.
    """

    all_operators = "+-*/^"
    if operator not in all_operators:
        raise ValueError("Wrong operator")
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Not an integer or float")

    if operator == '+':
        solution = num1 + num2
    elif operator == '-':
        solution = num1 - num2
    elif operator == '*':
        solution = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Not divisible by 0")
        solution = num1 / num2
    elif operator == '^':
        solution = num1 ** num2

    return solution


print(math_operations(6, '+', 2))
