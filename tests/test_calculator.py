from unittest.mock import patch
import runpy

import pytest

from application.Calcs.calculator import calculator


@pytest.mark.parametrize(
    "first_number, operator, second_number, expected_result",
    [
        ("2", "+", "3", "Result: 5.0"),
        ("5", "-", "3", "Result: 2.0"),
        ("2", "*", "3", "Result: 6.0"),
        ("6", "/", "3", "Result: 2.0"),
    ],
)
def test_calculator_performs_operations(
    first_number, operator, second_number, expected_result, capsys
):
    with patch(
        "builtins.input",
        side_effect=[first_number, operator, second_number, "q"],
    ):
        calculator()

    assert expected_result in capsys.readouterr().out


def test_calculator_quits_at_first_number(capsys):
    with patch("builtins.input", return_value="q"):
        calculator()

    assert "Calculator: enter q at any prompt to quit." in capsys.readouterr().out


def test_calculator_quits_at_operator():
    with patch("builtins.input", side_effect=["2", "q"]):
        calculator()


def test_calculator_quits_at_second_number():
    with patch("builtins.input", side_effect=["2", "+", "q"]):
        calculator()


def test_calculator_rejects_unsupported_operation(capsys):
    with patch("builtins.input", side_effect=["2", "%", "q"]):
        calculator()

    assert "Please choose +, -, *, or /." in capsys.readouterr().out


def test_calculator_rejects_non_numeric_first_number(capsys):
    with patch("builtins.input", side_effect=["abc", "+", "2", "q"]):
        calculator()

    assert "could not convert string to float" in capsys.readouterr().out


def test_calculator_rejects_non_numeric_second_number(capsys):
    with patch("builtins.input", side_effect=["2", "+", "abc", "q"]):
        calculator()

    assert "could not convert string to float" in capsys.readouterr().out


def test_calculator_handles_division_by_zero(capsys):
    with patch("builtins.input", side_effect=["2", "/", "0", "q"]):
        calculator()

    assert "You cannot divide by zero." in capsys.readouterr().out


def test_calculator_module_starts_repl():
    with patch("builtins.input", return_value="q"):
        runpy.run_module("application.Calcs.calculator", run_name="__main__")
