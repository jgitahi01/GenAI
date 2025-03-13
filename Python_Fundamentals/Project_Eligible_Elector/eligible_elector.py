#voter eligibility checker
try: 
    age = int(input("How old are you?:"))
# check if the user is eligible to vote
    if age<0: # check if the user entered a negative
        print("Hmm... Are you a time traveller? Please enter a valid age!")
    elif age>=18: # check if the user is 18 years or older
        print("Congratulations! You are eligible to vote. Go make a difference!")
    else: # if the user is younger than 18 
        years_left = 18 - age # calculate the number of years left until the user is eligible to vote
        print("Oops! You're not eligible yet. But hey, only", years_left,"more years to go!")
except ValueError: # check if the user entered a valid number
    print("Oops! This doesn't look like a number. Please enter a valid age!")