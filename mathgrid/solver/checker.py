from .basic_operations import Operator


def is_operator(item: str) -> Operator:
    """Return True if the string is an Operator, False otherwise.
    """

    try:
        Operator(item)
    except ValueError:
        return False

    return True


def is_expression(expression: list) -> bool:
    """Return True if the string is an expression, False otherwise.

    A string is an expression if it starts with the "=" symbol.

    Raises:
        ValueError: Empty expression raises when the string is empty.
    """
    if len(expression) == 0:
        raise ValueError("Empty expression")
    return expression[0] == '='


def is_number(item: str) -> bool:
    """Return True if the string is a number, False otherwise.
    """
    try:
        float(item)
        return True
    except TypeError:
        return False
    except ValueError:
        return False


def valid_num_brackets(expression: list) -> int and int:
    """Check the brackets in the expression.

    Returns:
        int and int: number of open brackets and number of close brackets.
    """
    brackets = 0
    for item in expression:
        if item == '(':
            brackets += 1
        elif item == ')':
            brackets -= 1
            if brackets < 0:
                return False
    return brackets == 0


def check_expression(expression: list) -> bool:
    """Return True if the expression is valid, False otherwise.
    """

    if not valid_num_brackets(expression):
        return False

    for index, item in enumerate(expression[1:], 1):
        if not is_number(item) and not is_operator(item) and item not in '()':
            return False
        if index < len(expression[1:]) - 1:
            if (is_number(item) and is_number(expression[index + 1])) or (is_operator(item) and is_operator(expression[index + 1])) :
                return False

    return True
