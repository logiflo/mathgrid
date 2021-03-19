"""Tests for checker module
"""

# from mathgrid import solver
from mathgrid.solver.basic_operations import Operator
import pytest
from mathgrid import solver


def test_is_operator_01():
    for item in '+-*/^':
        assert solver.is_operator(item) == True


def test_is_operator_02():
    assert solver.is_operator('h') == False
    assert solver.is_operator('·') == False
    assert solver.is_operator('0') == False


def test_is_expression_01():
    assert solver.is_expression(['=', '(', '1', '+', '2', ')']) == True


def test_is_expression_02():
    assert solver.is_expression(['(', '1', '+', '2', ')']) == False


def test_is_number_01():
    for item in ['1', '-8', '2.2', '.6']:
        assert solver.is_number(item) == True


def test_is_number_02():
    assert solver.is_number('h') == False
    assert solver.is_number('+') == False
    assert solver.is_number(Operator.ADDITION) == False


def test_valid_num_brackets_01():
    test_example = ['=', '(', '(', '8', '+', '3', ')',
                    '*', '2', ')', '/', '(', '5', '-', '1', ')']
    assert solver.valid_num_brackets(test_example) == True


def test_valid_num_brackets_02():
    test_example = ['=', ')', '(', '8', '+', '3',
                    ')', '*', '2', '(', '/', '(', '5', '-', '1', ')']
    assert solver.valid_num_brackets(test_example) == False


def test_check_expression_01():
    test_example = ['=', '(', '(', '8', '+', '3', ')',
                    '*', '2', ')', '/', '(', '5', '-', '1', ')']
    assert solver.check_expression(test_example) == True

    test_example = ['=', '(', '(', 'h', '+', '3', ')',
                    '*', '2', ')', '/', '(', '5', '-', '1', ')']
    assert solver.check_expression(test_example) == False

    test_example = ['=', '(', '(', '8', '9', '+', '3', ')',
                    '*', '2', ')', '/', '(', '5', '-', '1', ')']
    assert solver.check_expression(test_example) == False

    test_example = ['=', '(', '(', '8', '+', '+', '3', ')',
                    '*', '2', ')', '/', '(', '5', '-', '1', ')']
    assert solver.check_expression(test_example) == False

