run = 'y'


def choose_operation():
    operator = input("Choose operation (+, -, /, *): ")
    while operator not in ('+', '-', '/', '*'):
        operator = input("Please use one of the following: +, -, /, *")
    return operator


def adding(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        print("Error: Cannot divide by zero!")
        return a  # Cannot divide by zero!
    return a / b


while run == 'y':
    result = float(input("Enter first number (a): "))
    run = 'n'
    while run == 'n':

        number = float(input("Enter second number (b): "))

        user_choice = choose_operation()
        if user_choice == '+':
            result = adding(result, number)
        elif user_choice == '-':
            result = subtraction(result, number)
        elif user_choice == '*':
            result = multiplication(result, number)
        elif user_choice == '/':
            result = division(result, number)

        print(f"Result: {result}")
        run = input('Do you want to restart? (y/n): ').lower()
        if run != 'y':
            print("Exiting calculator.")
            break
