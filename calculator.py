def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def calculate(a, operator, b):
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    if operator not in operations:
        raise ValueError("Invalid operator.")

    return operations[operator](a, b)


def main():
    print("Python Calculator")
    print("-" * 20)

    try:
        first_number = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        second_number = float(input("Enter second number: "))

        result = calculate(first_number, operator, second_number)
        print(f"Result: {result}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()









