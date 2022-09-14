# Programmed by Tamara Lynch: Week 3 In Class Assignment 12 September 2022.
# Create a Python program that uses Turtle to draw the diagram 
#   exactly like it is in the pic. (Concentric red squares with
#   a blue dot in the middle and a blue turtle in the lower left corner)

# Initialize the turtle module, in away that makes coding less redundant
    # since the entire program is written in this one module.
from turtle import*  

# Draw the central dot
dot(10,'blue')
penup()

# Name variables that will be used repeatedly for square's sides
side = 100

# Set the pen color for the squares
pencolor('red')

# Draw the inner square

goto(50,-50)
pendown()
hideturtle()
for i in range(4):
    left(90)
    forward(side)
penup()

# Draw the outer square
side = 300  # This resets the variable for a larger square
goto(150,-150)
pendown()
hideturtle()
shape('square')
for i in range(4):
    left(90)
    forward(side)
penup()


# Place a large blue turtle in the lower left corner
goto(-250,-250)
setheading(90)
showturtle()
shape('turtle')
pencolor('blue')
pensize(15)

done() # Keep the drawing in the window
