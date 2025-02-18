# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:  # base case: if n is 0 or 1, return 1
        return 1
    return n * factorial(n - 1)


# Recursive function to calculate the nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  #


# using the functions
fact_result = factorial(5)
fib_result = fibonacci(6)

print(f"Factorial of 5 is {fact_result}.")
print(f"The 6th Fibonacci number is {fib_result}.")
