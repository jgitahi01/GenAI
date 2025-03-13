import turtle


# Factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Fibonacci function
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Recursive fractal pattern (Tree)
def draw_tree(branch_length):
    if branch_length > 5:
        turtle.forward(branch_length)
        turtle.right(20)
        draw_tree(branch_length - 15)
        turtle.left(40)
        draw_tree(branch_length - 15)
        turtle.right(20)
        turtle.backward(branch_length)


# Menu function
def main_menu():
    while True:
        print("\nWelcome to the Recursive Artistry Program!")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci")
        print("3. Draw a Recursive Fractal")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            try:
                num = int(input("Enter a positive integer to find its factorial: "))
                if num < 0:
                    print("Please enter a non-negative integer.")
                else:
                    print(f"The factorial of {num} is {factorial(num)}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        elif choice == "2":
            try:
                num = int(input("Enter the position of the Fibonacci number: "))
                if num <= 0:
                    print("Please enter a positive integer.")
                else:
                    print(f"The {num}th Fibonacci number is {fibonacci(num)}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        elif choice == "3":
            print(
                "Drawing a recursive fractal tree... (close the window to return to the menu)"
            )
            turtle.speed(0)
            turtle.left(90)
            turtle.up()
            turtle.backward(100)
            turtle.down()
            turtle.color("green")
            draw_tree(100)
            turtle.done()

        elif choice == "4":
            print("Goodbye! Thanks for exploring recursion with me!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Run the program
if __name__ == "__main__":
    main_menu()
