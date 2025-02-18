def greet_user(name): # function defining 
    return f"Hello,{name}! Welcome aboard."


def add_numbers(x, y):
    return x + y


# using the functions
greetings = greet_user("John Doe")
sum = add_numbers(15,25)
print(f"{greetings} The sum of 15 and 25 is {sum}")
