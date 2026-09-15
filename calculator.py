def choose_operation():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    return int(input("Choose an operation: "))


def enter_operand(operand_number):
    return int(input("Enter your " + operand_number + " operand: "))


def get_division_type():
    print("1. Regular division")
    print("2. Integer division")
    division_type = int(input("Choose a division type: "))
    return division_type


def perform_operation(operation, operand1, operand2):
    result = 0
    if operation == 1:
        result = operand1 + operand2
    elif operation == 2:
        result = operand1 - operand2
    elif operation == 3:
        result = operand1 * operand2
    elif operation == 4:
        division_type = get_division_type()
        if division_type == 1:
            result = operand1 / operand2
        else:
            result = operand1 // operand2
    return result


def main():
    operation = choose_operation()
    operand1 = enter_operand("first")
    operand2 = enter_operand("second")
    result = perform_operation(operation, operand1, operand2)
    print(result)


main()