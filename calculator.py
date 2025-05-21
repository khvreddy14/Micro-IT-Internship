def calculate(expression):
    try:
        # Evaluate the expression and return the result
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def calculator():
    print("Welcome to the Calculator!")
    print("You can perform calculations using +, -, *, / and parentheses.")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("Enter your expression: ")
        if user_input.lower() == 'exit':
            print("Exiting the calculator.")
            break
        
        result = calculate(user_input)
        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()