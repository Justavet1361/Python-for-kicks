# Designed by Tamara Lynch: Week 4 In Class Assignment #2 22 September 2022.

# Create a Python program that asks the user for a month as a number between 1 and 12. 
# The program should display a message indicating whether the month is in the first quarter, 
# the second quarter, the third quarter, or the fourth quarter of the year. 
# Following are the guidelines:
#   If the user enters either 1, 2, or 3, the month is in the "first quarter".
#   If the user enters a number between 4 and 6, the month is in the "second quarter".
#   If the number is either 7, 8, or 9, the month is in the "third quarter".
#   If the month is between 10 and 12, the month is in the "fourth quarter".
#   If the number is not between 1 and 12, the program should display an error

# Request User Input
month = int(input("Please enter a number between 1 and 12 to indicate the month you are interested in: "))

# Name the month, and determine and indicate its quarter.
if month == 1 or month == 2 or month == 3:
    if month == 1:
        month_title = 'January'
    elif month == 2:
        month_title = 'February'
    else:
        month_title = 'March'
    print(month_title + ' falls in the First quarter')
elif month == 4 or month == 5 or month == 6:
    if month == 4:
        month_title = 'April'
    elif month == 5:
        month_title = 'May'
    else: 
        month_title = 'June'
    print(month_title + ' falls in the Second quarter')
elif month == 7 or month == 8 or month == 9:
    if month == 7:
        month_title = 'July'
    elif month == 8:
        month_title = 'August'
    else:
        month_title = 'September'
    print(month_title + ' falls in the Third quarter')
elif month == 10 or month == 11 or month == 12:
    if month == 10:
        month_title = 'October'
    elif month == 11:
        month_title = 'November'
    else: 
        month_title = 'December'
    print(month_title + ' falls in the Fourth quarter')
else:
    print('Sorry, you did not enter an integer between 1 and 12')