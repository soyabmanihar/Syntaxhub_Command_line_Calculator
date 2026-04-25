"""
Command-line Calculator Application
Supports basic arithmetic operations with input validation and error handling.
"""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b with zero-division check."""
    if b == 0:
        raise ValueError("Error: Cannot divide by zero!")
    return a / b


def is_valid_number(value):
    """Validate if a string can be converted to a number."""
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_valid_operator(operator):
    """Validate if the operator is supported."""
    valid_operators = ['+', '-', '×', '÷', '*', '/', 'clear']
    return operator in valid_operators


def parse_input(user_input):
    """
    Parse user input to extract first number, operator, and second number.
    Returns tuple: (num1, operator, num2) or (None, None, None) if invalid.
    """
    user_input = user_input.strip()
    
    # Handle clear command
    if user_input.lower() == 'clear':
        return None, 'clear', None
    
    # Split input by spaces
    parts = user_input.split()
    
    if len(parts) != 3:
        return None, None, None
    
    num1_str, operator, num2_str = parts
    
    # Validate numbers
    if not is_valid_number(num1_str) or not is_valid_number(num2_str):
        return None, None, None
    
    # Validate operator
    if not is_valid_operator(operator):
        return None, None, None
    
    return float(num1_str), operator, float(num2_str)


def perform_calculation(num1, operator, num2):
    """
    Perform calculation based on operator.
    Returns result or None if operation fails.
    """
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
    """Display the calculator menu and instructions."""
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
    """Main calculator loop."""
    display_menu()
    calculation_history = []
    
    while True:
        try:
            user_input = input("Enter calculation: ").strip()
            
            # Check for exit command
            if user_input.lower() == 'exit':
                print("\nThank you for using the calculator! Goodbye!")
                break
            
            # Check for empty input
            if not user_input:
                print("Invalid input. Please try again.\n")
                continue
            
            # Parse input
            num1, operator, num2 = parse_input(user_input)
            
            # Handle clear command
            if operator == 'clear':
                calculation_history = []
                print("✓ History cleared. Ready for new calculations.\n")
                continue
            
            # Validate parsed input
            if num1 is None or operator is None or num2 is None:
                print("Invalid input format. Use: <number> <operator> <number>")
                print("Supported operators: +, -, ×, ÷\n")
                continue
            
            # Perform calculation
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
