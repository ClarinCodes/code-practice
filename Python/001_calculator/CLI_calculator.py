
"""
Calculator:
1. Support arithmetic operations.
2. Validate input and operations.
3. Has basic unit converters.
"""


def add(input_1, input_2):
    return input_1 + input_2


def sub(input_1, input_2):
    return input_1 - input_2


def mul(input_1, input_2):
    return input_1 * input_2


def div(input_1, input_2):
    if input_2 == 0:
        raise ValueError("Cannot divide by zero.")
    return input_1 / input_2


def get_option():
    while True:
        try:
            option = int(input("Enter option: "))

            if option in (1, 2, 3):
                return option

            print("!!! Enter a valid option !!!")

        except ValueError:
            print("!!! Enter a valid number !!!")


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("!!! Enter a valid number !!!")


def arithmetic():
    print("\nArithmetic Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        try:
            operation = int(input("Enter operation: "))

            if operation not in (1, 2, 3, 4):
                print("!!! Enter a valid operation !!!")
                continue

            break

        except ValueError:
            print("!!! Enter a valid number !!!")

    input_1 = get_number("Enter first number: ")
    input_2 = get_number("Enter second number: ")

    try:
        if operation == 1:
            result = add(input_1, input_2)

        elif operation == 2:
            result = sub(input_1, input_2)

        elif operation == 3:
            result = mul(input_1, input_2)

        elif operation == 4:
            result = div(input_1, input_2)

        print("Result:", result)

    except ValueError as error:
        print("Error:", error)


def unit_converter():
    print("\nUnit Converters")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")

    while True:
        try:
            operation = int(input("Enter conversion: "))

            if operation not in (1, 2, 3, 4):
                print("!!! Enter a valid conversion !!!")
                continue

            break

        except ValueError:
            print("!!! Enter a valid number !!!")

    value = get_number("Enter value: ")

    if operation == 1:
        result = value * 0.621371
        print(f"{value} km = {result:.2f} miles")

    elif operation == 2:
        result = value * 1.60934
        print(f"{value} miles = {result:.2f} km")

    elif operation == 3:
        result = (value * 9 / 5) + 32
        print(f"{value}°C = {result:.2f}°F")

    elif operation == 4:
        result = (value - 32) * 5 / 9
        print(f"{value}°F = {result:.2f}°C")


def main():
    while True:
        print("\n===== Calculator =====")
        print("1. Arithmetic operations")
        print("2. Unit conversion")
        print("3. Exit")

        option = get_option()

        if option == 1:
            arithmetic()

        elif option == 2:
            unit_converter()

        elif option == 3:
            print("Goodbye!")
            break


main()
