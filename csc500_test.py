# Part 2
'''
The CSU Global Bookstore has a book club that awards points to its students
based on the number of books purchased each month.
The points are awarded as follows:
--If a customer purchases 0 books, they earn 0 points.
--If a customer purchases 2 books, they earn 5 points.
--If a customer purchases 4 books, they earn 15 points.
--If a customer purchases 6 books, they earn 30 points.
--If a customer purchases 8 or more books, they earn 60 points.
Write a program that asks the user to enter the number of books that they have
purchased this month and then display the number of points awarded.'''

# get the number of books purchased
books = int(input("Enter the number of books purchased: "))
points = 0

# odd number of books purchased creates a bug
# adust inpput to round down to nearest even number
if books % 2 != 0:  # if books/2 has a non-0 remainder (it's odd) &
    books -= 1 # then subtract 1 from the number of books.

if books == 0: points = 0
elif books <= 2: points = 5 #
elif books <= 4: points = 15
elif books <= 6: points = 30
elif books >= 8: points = 60
# display the number of books purchased and points awarded
print(f"Qualifying Books Purchased: {books}")
print(f"Points awarded: {points}")
