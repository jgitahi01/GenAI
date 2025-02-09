#program to calculate the factorial of a number entered by the user 
#1.ask user for a number
#2.use a for loop to calculate the factorial of the number
#3.print the factorial
num = int(input("Enter a number: "))

factorial = 1 #initialize the factorial variable to 1
for i in range(1, num+1): #loop through the numbers from 1 to the number entered by the user
    factorial *= i #multiply the factorial by the current number
print(f"The factorial of {num} is {factorial}") #print the factorial