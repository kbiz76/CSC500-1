#####
#Part 2: Book Club
#Pseudocode
#1. Ask the user for the number of books they purchased this month.
#2. Intialize points
#3. Use if-elif-else statements to determine the points based on the number of books purchased.
#4. Display the number of points awarded
#####
#number of books purchased in the month
num_books = int(input("How many books did you purchase this month? "))

if num_books == 0:
    points = 0
elif num_books == 2:
    points = 5
elif num_books == 4:
    points = 15
elif num_books == 6:
    points = 30
elif num_books >= 8:
    points = 60
else:
    points = 0

#points awarded for books purchased
print(f"{points} points awarded")
