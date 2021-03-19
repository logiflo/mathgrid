"""Tests for converters module
"""

# from mathgrid import solver
import pytest
from mathgrid import solver


def test_item_str_to_number_int():
    assert solver.item_str_to_number('6') == 6


def test_item_str_to_number_float():
    assert solver.item_str_to_number('7.8') == 7.8


def test_item_str_to_number_negative():
    assert solver.item_str_to_number('-.2') == -0.2


def test_item_str_to_number_not_number():
    with pytest.raises(ValueError):
        solver.item_str_to_number('(')


def test_exp_str_to_list_01():
    assert solver.exp_str_to_list('=(1.5 +7- 8)*-8') == ['=', '(', '1.5', '+', '7', '-', '8', ')', '*', '-8']


def test_exp_str_to_list_02():
    assert solver.exp_str_to_list('=hola') == ['=', 'h', 'o', 'l', 'a']


def test_exp_str_to_list_03():
    assert solver.exp_str_to_list(' =(.5 +7..8)') == ['=', '(', '.5', '+', '7.', '.', '8', ')']
