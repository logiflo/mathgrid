"""Tests for basic_operations module
"""

# from mathgrid import solver
import pytest
from mathgrid import solver


def test_addition():
    assert solver.basic_operation(1, 1, solver.Operator.ADDITION) == 2


def test_substraction():
    assert solver.basic_operation(
        5.6, 2, solver.Operator.SUBSTRACTION) == 5.6 - 2


def test_product():
    assert solver.basic_operation(5, 3, solver.Operator.PRODUCT) == 15


def test_division():
    assert solver.basic_operation(5, 2, solver.Operator.DIVISION) == 2.5


def test_power():
    assert solver.basic_operation(5, 3, solver.Operator.POWER) == 125


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        solver.basic_operation(5, 0, solver.Operator.DIVISION)


def test_not_numbers1():
    with pytest.raises(TypeError):
        solver.basic_operation('5', 0, solver.Operator.ADDITION)


def test_not_numbers2():
    with pytest.raises(TypeError):
        solver.basic_operation('5', 'm', solver.Operator.POWER)
