# program takes a number from the user and tells them wether it's positive , negative, or zero
# ask the user to enter a number
user_input = float(input("Enter a number: "))
# check if the number is positive
if user_input > 0:
    print("This number is positive. Awesome!")
# check if the number is less than zero
elif user_input < 0:
    print("This number is negative. Better luck next time!")
# if the number is neither positive nor negative, it must be zero
else:
    print("Zero it is. A perfect balance!")