import string 

def check_password_strength(password):
    score = 0 # Initializing score meter to 0
    errors = [] # empty list to store errors

    # Check length
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    else:
        score += 2 
    # Contain at least one uppercase letter, one lowercase letter, one digit, and one special character (like @, #, $).
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if has_upper:
        score += 2
    else:
        errors.append(" at least one uppercase letter.")
    if has_lower:
        score += 2
    else:
        errors.append(" at least one lowercase letter.")
    if has_digit:
        score += 2
    else:
        errors.append(" at least one digit.")
    if has_special:
        score += 2
    else:
        errors.append(" at least one special character.")
    if not errors:
        print("Your password is strong!")
        print(f"Your Password Strength: {score}/10")
    else:
        print("Your password needs"+"and".join(errors))

        print(f"Your Password Srength: {score}/10") # strength meter

while True: 
    password = input("Enter a password (or type 'exit' to quit): ")# ask user for a password
    if password.lower() == 'exit':
        break
    check_password_strength(password)
    print()