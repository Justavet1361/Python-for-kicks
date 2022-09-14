# Tamara Lynch: Week 2 In Class Assignment 29 August 2022
# Create a program that prompts the user for 3 bowling scores. 
# The program should then display the 3 scores and the average.

# To clear the screen after the inputs and the outputs, import windows os
#       then use the 'cls' argument to clear the screen
# import time to get a "calculating" pause
import os
import time
#Introduce the game
print('')
print('')
print('*************************************************************')
print('Welcome to the bowling score averager')
print('*************************************************************')
print('')
print('')
# Have the user input three bowling scores and change them from strings to integers
game1 = int(input('Please enter your first bowling game, "Game 1" score: '))
os.system('cls')
game2 = int(input('Please enter your second bowling game, "Game 2" score: '))
os.system('cls')
game3 = int(input('Please enter your third bowling game, "Game 3" score: '))
os.system('cls')
time.sleep(2)

# Calculate the average of the three game scores.  
# The magic number "3" is the total number of game scores collected.
averageScore = (game1 + game2 + game3)/3

# Do outputting here...
print('---------------------------------------------------------------------')
print("Your score for your first bowling game was reported as:  " + str(game1))
print('---------------------------------------------------------------------')
print("Your score for your second bowling game was reported as:  " + str(game2))
print('---------------------------------------------------------------------')
print("Your score for your third bowling game was reported as:  " + str(game3))
print('---------------------------------------------------------------------')
print('')
print('')
print("Your average bowling score over three games is: " + str(averageScore))
print('***********************************************************************')
print('')
print('Congratulations!')
print('')
print('')