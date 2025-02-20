def handle_exceptions():
    # Handling IndexError
    try:
        my_list = [1, 2, 3]
        print(my_list[5])  # Accessing an invalid index
    except IndexError:
        print("IndexError occurred! List index out of range.")
    
    # Handling KeyError
    try:
        my_dict = {"a": 1, "b": 2}
        print(my_dict["c"])  # Accessing a non-existent key
    except KeyError:
        print("KeyError occurred! Key not found in the dictionary.")
    
    # Handling TypeError
    try:
        result = "Hello" + 5  # Adding a string and an integer
    except TypeError:
        print("TypeError occurred! Unsupported operand types.")

# Running the function
handle_exceptions()
