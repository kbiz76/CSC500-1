num_books = int(input("Enter the number of books purchased this month: "))

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

print(f"Number of points awarded: {points}")
