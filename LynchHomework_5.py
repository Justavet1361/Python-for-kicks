# Designed by Tamara Lynch: Week 4 In Class Assignment #1 22 September 2022.

# Create a Python program that prompts the user to enter an integer. 
#   The program should display “Positive” if the number is greater than 0, 
#   “Negative” if the number is less than 0, and “Zero” if the number is equal to 0. 
#   The program should then display “Even” if the number is even, and “Odd” if the number is odd.

# User prompt
number = int(input('Please enter any positive or negative integer (whole number): '))

# Determine if positive or negative and disply the result
if number < 0:
    print(str(number) + ' is Negative')
elif number == 0:
    print(str(number) + ' is Zero')
elif number > 0:
    print(str(number) + ' is Positive')
else:
    print('Please try again and ensure you enter an iteger.')

# Display if Odd or Even
if number % 2 == 0:
    print('And ' + str(number) + ' is even.')
else:
    print('And' + str(number) + ' is odd.')