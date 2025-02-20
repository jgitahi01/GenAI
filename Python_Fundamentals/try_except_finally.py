def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input! Please enter numeric values.")
    else:
        print(f"The result is {result}.")
    finally:
        print("This block always executes.")

# Running the function
divide_numbers()
