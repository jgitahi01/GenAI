import logging

# Configure logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculator():
    while True:
        print("\nWelcome to the Error-Free Calculator!")
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("> ")
        
        if choice == '5':
            print("Goodbye!")
            break
        
        if choice in ('1', '2', '3', '4'):
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            
            try:
                if choice == '1':
                    result = num1 + num2
                elif choice == '2':
                    result = num1 - num2
                elif choice == '3':
                    result = num1 * num2
                elif choice == '4':
                    result = num1 / num2
            except ZeroDivisionError:
                print("Oops! Division by zero is not allowed.")
                logging.error("ZeroDivisionError occurred: division by zero.")
            else:
                print(f"The result is {result}.")
            finally:
                print("Operation complete.")
        else:
            print("Invalid selection. Please choose a valid option.")

# Running the calculator
calculator()
