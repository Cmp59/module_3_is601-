"""Basic calculator operations."""


def addition(first_number, second_number):
    return first_number + second_number


def subtraction(first_number, second_number):
    return first_number - second_number


def multiplication(first_number, second_number):
    return first_number * second_number


def division(first_number, second_number):
    if second_number == 0:
        raise ValueError("You cannot divide by zero.")
    return first_number / second_number