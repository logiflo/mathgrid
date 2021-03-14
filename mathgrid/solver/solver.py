"""Solver module
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


def is_operator(item: str) -> Operator:
    """Return True if the string is an Operator, False otherwise.
    """

    try:
        Operator(item)
    except ValueError:
        return False

    return True


def is_expression(expression: str) -> bool:
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


def str_to_number(item: str) -> int or float:
    """Convert a string into a integer or float.
    """
    try:
        int(item)
        return int(item)
    except ValueError:
        return float(item)


def valid_num_brackets(expression: list) -> int and int:
    """Check the brackets in the expression.

    Returns:
        int and int: number of open brackets and number of close brackets.
    """
    open_brackets, close_brackets = 0, 0
    for item in expression:
        if item == '(':
            open_brackets += 1
        elif item == ')':
            close_brackets += 1
    return open_brackets, close_brackets


def check_expression(expression: list) -> bool:
    """Return True if the expression is valid, False otherwise.
    """
    if not is_expression(expression):
        return False

    open_brackets, close_brackets = valid_num_brackets(expression)
    if open_brackets != close_brackets:
        return False

    for item in expression[1:]:
        if not is_number(item) or not is_operator(item) or item not in '()':
            return False

    return True


def prefix_expression(expression: list) -> list:
    """Converts an infix expression to a prefix expression.

    Args:
        expression (list): infix expression.

    Raises:
        ValueError: if an item of the expression is not a number or Operator.

    Returns:
        list: prefix expression.
    """
    numbers, prefix = list(), list()
    last_operator = Operator('+')

    for index, item in enumerate(expression):
        if is_number(item):
            if last_operator >= Operator.PRODUCT or index == len(expression) - 1:
                prefix.append(str_to_number(item))
            else:
                numbers.append(str_to_number(item))
        elif is_operator(item):
            last_operator = Operator(item)
            if last_operator >= Operator.PRODUCT:
                prefix.append(Operator(item))
            else:
                prefix.insert(0, Operator(item))

            if len(numbers) != 0:
                prefix.append(numbers[-1])
                numbers.pop(-1)
        else:
            raise ValueError("Operator not supported")

    return prefix


def prefix_calculator(prefix: list) -> int or float:
    """Solve the infix expression.

    Args:
        prefix (list).

    Returns:
        int or float: the result of the expression.
    """
    copy_prefix = prefix
    for pos, value in reversed(list(enumerate(copy_prefix))):
        if isinstance(value, Operator):
            copy_prefix[pos] = basic_operation(
                copy_prefix[pos + 1], copy_prefix[pos + 2], value)
            copy_prefix.pop(pos + 1)
            copy_prefix.pop(pos + 1)

    return copy_prefix[0]


def remove_brackets(infix_expression: list, start: int) -> list and int:
    """Recursive function that remove brackets in the expression.

    Args:
        infix_expression (list)
        start (int): position of the open bracket.

    Returns:
        list: infix expression where the brackets are solved.
        int: position of the close bracket.
    """
    infix = []
    pos = start + 1
    while pos != len(infix_expression):
        value = infix_expression[pos]
        if value == ')':
            prefix = prefix_expression(infix)
            res = prefix_calculator(prefix)
            break
        if value == '(':
            res_rec, end = remove_brackets(infix_expression, pos)
            infix_expression[pos:end+1] = [res_rec]
            infix.append(res_rec)
        else:
            infix.append(value)
        pos += 1

    return res, pos


def calculator(expression: list) -> int or float:
    """Solve an infix expression.

    Args:
        infix_expression (list)

    Returns:
        int or float: result of the infix expression.
    """
    if not check_expression(expression):
        return " ".join(expression)

    infix_expression = expression[1:]
    pos = 0
    while pos != len(infix_expression):
        value = infix_expression[pos]
        if value == '(':
            res, end = remove_brackets(infix_expression, pos)
            infix_expression[pos:end+1] = [res]
        pos += 1
    prefix = prefix_expression(infix_expression)
    result = prefix_calculator(prefix)
    return result


# if __name__ == '__main__':
#     infix_expression = input("Introduce an expression: ").split()
#     result = calculator(infix_expression)
#     print(result)
