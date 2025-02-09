#progam genertes multiplication for any number provided by the user
#1.ask user for a number
#2.use for loop to print the multiplication table for that number (from 1 to 10)
num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num} x {i} = {num * i}", end="\n")
print()