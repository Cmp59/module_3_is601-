import pytest

from application.ops.operations import (
    addition,
    division,
    multiplication,
    subtraction,
)


def test_addition():
    assert addition(2, 3) == 5


def test_subtraction():
    assert subtraction(5, 3) == 2


def test_multiplication():
    assert multiplication(2, 3) == 6


def test_division():
    assert division(6, 3) == 2


def test_division_by_zero():
    with pytest.raises(ValueError, match="divide by zero"):
        division(6, 0)
