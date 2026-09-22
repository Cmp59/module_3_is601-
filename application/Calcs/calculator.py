"""Command-line calculator."""

from ..ops.operations import Operations


def calculator():
    """Run the calculator until the user chooses to quit."""
    operations = {
        "+": Operations.addition,
        "-": Operations.subtraction,
        "*": Operations.multiplication,
        "/": Operations.division,
    }

    print("Calculator: enter q at any prompt to quit.")

    while True:
        first_input = input("First number: ").strip()
        if first_input.lower() == "q":
            break

        operator = input("Operation (+, -, *, /): ").strip()
        if operator.lower() == "q":
            break
        if operator not in operations:
            print("Please choose +, -, *, or /.")
            continue

        second_input = input("Second number: ").strip()
        if second_input.lower() == "q":
            break

        try:
            first_number = float(first_input)
            second_number = float(second_input)
            result = operations[operator](first_number, second_number)
        except ValueError as error:
            print(f"Error: {error}")
            continue

        print(f"Result: {result}")


if __name__ == "__main__":
    calculator()