#tuple with a movie, song, and book
my_collection = ("The Gorge", "Not Like US", "The Alchemist")
#Printing the tuple
print("Favorite things:", my_collection)
#trying to change an element in the tuple
try:
    my_collection[1] = "The Power of Now"
except TypeError as e:
    print("Oops! Tuples cannot be changed.")
    print(f"Error: {e}")
#printing the len of the tuple
print("Length of tuple:", len(my_collection))