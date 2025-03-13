# Function to describe a pet
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

#using the function
describe_pet("Buddy")  # Uses default value "dog"
describe_pet("Whiskers", "cat")  # Specifies "cat"
