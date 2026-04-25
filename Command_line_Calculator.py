def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Error: Cannot divide by zero!")
    return a / b


def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_valid_operator(operator):
    valid_operators = ['+', '-', '×', '÷', '*', '/', 'clear']
    return operator in valid_operators


def parse_input(user_input):
 
    user_input = user_input.strip()
    if user_input.lower() == 'clear':
        return None, 'clear', None
    
    parts = user_input.split()
    
    if len(parts) != 3:
        return None, None, None
    
    num1_str, operator, num2_str = parts
   
    if not is_valid_number(num1_str) or not is_valid_number(num2_str):
        return None, None, None
    
    if not is_valid_operator(operator):
        return None, None, None
    
    return float(num1_str), operator, float(num2_str)


def perform_calculation(num1, operator, num2):

    try:
        if operator == '+':
            return add(num1, num2)
        elif operator == '-':
            return subtract(num1, num2)
        elif operator == '×' or operator == '*':
            return multiply(num1, num2)
        elif operator == '÷' or operator == '/':
            return divide(num1, num2)
        else:
            return None
    except ValueError as e:
        print(f"{e}")
        return None


def display_menu():
    print("\n" + "="*50)
    print("     COMMAND-LINE CALCULATOR")
    print("="*50)
    print("Instructions:")
    print("  - Enter: <number1> <operator> <number2>")
    print("  - Examples: 10 + 5  |  20 × 3  |  15 ÷ 2")
    print("\nSupported operators:")
    print("  +  : Addition")
    print("  -  : Subtraction")
    print("  ×  : Multiplication")
    print("  ÷  : Division")
    print("\nCommands:")
    print("  clear  : Clear calculations and start fresh")
    print("  exit   : Quit the calculator")
    print("="*50 + "\n")


def main():
    display_menu()
    calculation_history = []
    
    while True:
        try:
            user_input = input("Enter calculation: ").strip()
         
            if user_input.lower() == 'exit':
                print("\nThank you for using the calculator! Goodbye!")
                break

            if not user_input:
                print("Invalid input. Please try again.\n")
                continue
            
            num1, operator, num2 = parse_input(user_input)
            
            if operator == 'clear':
                calculation_history = []
                print("✓ History cleared. Ready for new calculations.\n")
                continue
            
            if num1 is None or operator is None or num2 is None:
                print("Invalid input format. Use: <number> <operator> <number>")
                print("Supported operators: +, -, ×, ÷\n")
                continue

            result = perform_calculation(num1, operator, num2)
            
            if result is not None:
                calculation_history.append(f"{num1} {operator} {num2} = {result}")
                print(f"Result: {result}")
                print(f"History: {' | '.join(calculation_history[-3:])}\n")
            else:
                print("Calculation failed. Please try again.\n")
        
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")


if __name__ == "__main__":
    main()
