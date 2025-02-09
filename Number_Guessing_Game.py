# generate random number between 1 and 100
import random
number_to_guess = random.randint(1, 100)
# using while loop to keep the user guessing until they the correct number 
#If the guess is too high, print: "Too high! Try again."
#If the guess is too low, print: "Too low! Try again."
#If the guess is correct, print: "Congratulations! You guessed it!
#Keep track of how many guesses the user has made and display the total number of attempts when they win.
attempts = 0
max_attempts = 10

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

while attempts < max_attempts:
    try:
        guess = int(input("Guess the number: "))
        attempts += 1 #increment attempt counter 

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break   
    except ValueError:
        print("Please enter a valid number.")

#if user runs out attemps 
if attempts == max_attempts and guess != number_to_guess:
    print(f"Sorry, you ran out of attempts. The number was {number_to_guess}. Better luck next time!")