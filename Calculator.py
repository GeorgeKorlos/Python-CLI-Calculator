from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calc():
    print(logo)
    num1 = float(input("What is the first number?: "))
    for operation in operations:
        print(operation)

    still_going = True

    while still_going:

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        calc_func = operations[operation_symbol]
        answer = calc_func(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        next_op = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if next_op == 'y':
            num1 = answer
        else:
            still_going = False
            calc()

calc()