# Inventory Management Program

inventory = {}  # Initialize an empty dictionary for the inventory

def display_inventory():
    """Displays the current inventory in a user-friendly format."""
    if not inventory:
        print("Inventory is empty.")
        return

    print("Current inventory:")
    for item, (quantity, price) in inventory.items():
        print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")

def add_item():
    """Adds a new item to the inventory."""
    item = input("Enter item name: ")
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory[item] = (quantity, price)
        print(f"{item} added to inventory.")
    except ValueError:
        print("Invalid quantity or price. Please enter numbers.")

def remove_item():
    """Removes an item from the inventory."""
    item = input("Enter item name to remove: ")
    if item in inventory:
        del inventory[item]
        print(f"{item} removed from inventory.")
    else:
        print(f"{item} not found in inventory.")

def update_item():
    """Updates the quantity or price of an existing item."""
    item = input("Enter item name to update: ")
    if item in inventory:
        try:
            quantity = int(input("Enter new quantity (or press Enter to keep current): ") or inventory[item][0])
            price = float(input("Enter new price (or press Enter to keep current): ") or inventory[item][1])
            inventory[item] = (quantity, price)
            print(f"{item} updated.")
        except ValueError:
            print("Invalid quantity or price. Please enter numbers.")

    else:
        print(f"{item} not found in inventory.")

def calculate_total_value():
    """Calculates and displays the total value of the inventory."""
    total_value = 0
    for quantity, price in inventory.values():
        total_value += quantity * price
    print(f"Total value of inventory: ${total_value:.2f}")  # Format to two decimal places


while True:
    print("\nWelcome to the Inventory Manager!")
    display_inventory()

    print("\nOptions:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Update item")
    print("4. Calculate total value")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        update_item()
    elif choice == '4':
        calculate_total_value()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")