"""Converters module
"""

from mathgrid.solver.checker import is_number


def item_str_to_number(item: str) -> int or float:
    """Convert a string into a integer or float when it is a number, ValueError otherwise.
    """
    try:
        int(item)
        return int(item)
    except ValueError:
        return float(item)


def exp_str_to_list(expression: str) -> list:
    """Convert the expression string into a list, deleting white spaces.
    """
    exp_list = []
    auxiliar = ''
    for item in expression:
        if is_number(item):
            auxiliar += item
        elif item in '.' and '.' not in auxiliar:
            auxiliar += item
        elif item == '-' and len(auxiliar) == 0:
            auxiliar += item
        elif item == ' ':
            continue
        else:
            if len(auxiliar) != 0:
                exp_list.append(auxiliar)
                auxiliar = ''
            exp_list.append(item)
    if len(auxiliar) != 0:
        exp_list.append(auxiliar)

    return exp_list
