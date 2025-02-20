def divide_by_number():
    while True:
        try:
            num = input("Enter a number: ")
            num = float(num)  # Convert input to a number
            result = 100 / num
            print(f"100 divided by {num} is {result}.")
            break  # Exit loop if successful
        except ZeroDivisionError:
            print("Oops! You cannot divide by zero.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Running the function
divide_by_number()
