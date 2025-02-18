# Function to make a sandwich with variable ingredients
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

#using the function
make_sandwich("Lettuce", "Tomato", "Cheese")
make_sandwich("Turkey", "Mayo", "Pickles", "Onions")
