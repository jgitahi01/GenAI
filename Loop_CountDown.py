#countdowwn timer 
#1.ask user for starting number
#2.use a while loop to print numbers from the number down to 1 
# when the count ends, print "Blast off!"
start_num = int(input("Enter the starting number: "))
while start_num > 0:
    print(start_num, end="  ")
    start_num -= 1
print("Blast off!")
