"""Test for math_operations function
"""

import pytest
from mathgrid import solver


def test_addition():
    assert solver.math_operations(1, solver.Operator.ADDITION, 1) == 2


def test_substraction():
    assert solver.math_operations(5.6, solver.Operator.SUBSTRACTION, 2) == 5.6 - 2


def test_product():
    assert solver.math_operations(5, solver.Operator.PRODUCT, 3) == 15


def test_division():
    assert solver.math_operations(5, solver.Operator.DIVISION, 2) == 2.5


def test_power():
    assert solver.math_operations(5, solver.Operator.POWER, 3) == 125


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        solver.math_operations(5, solver.Operator.DIVISION, 0)


def test_not_numbers1():
    with pytest.raises(TypeError):
        solver.math_operations('5', solver.Operator.ADDITION, 0)


def test_not_numbers2():
    with pytest.raises(TypeError):
        solver.math_operations('5', solver.Operator.POWER, 'm')


def test_operator_not_supported():
    with pytest.raises(ValueError):
        solver.math_operations(5, '+', 2)
