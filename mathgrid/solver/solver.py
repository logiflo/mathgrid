"""Solver module
"""

from .basic_operations import *
from .checker import *
from .converters import *

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
                prefix.append(item_str_to_number(item))
            else:
                numbers.append(item_str_to_number(item))
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


def calculator(string_expression: str) -> int or float:
    """Solve an infix expression.

    Args:
        infix_expression (list)

    Returns:
        int or float: result of the infix expression.
    """

    expression = exp_str_to_list(string_expression)

    if is_expression(expression):
        if not check_expression(expression):
            return string_expression[1:]
    else:
        return string_expression

    infix_expression = expression[1:]
    pos = 0
    while pos != len(infix_expression):
        value = infix_expression[pos]
        if value == '(':
            res, end = remove_brackets(infix_expression, pos)
            infix_expression[pos:end+1] = [res]
        pos += 1
    prefix = prefix_expression(infix_expression)
    return prefix_calculator(prefix)
