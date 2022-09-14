# Programmed by Tamara Lynch: Week 3 In Class Assignment 12 September 2022. v1.0
# Create a Python program that uses Turtle to draw the diagram 
#   exactly like it is in the pic. (A vertical rectangle with three circles
#       red on top, yellow in the middle, green at the bottom, 
#       i.e. 'traffic light', each circle is outlined in black)

# Initialize the turtle module, in away that makes coding less redundant
    # since the entire program is written in this one module.
from turtle import*  

pensize(4)
hideturtle()
penup()

# Draw the outer rectangle
goto(-60,-140)
pendown()
forward(120)
left(90)
forward(360)
left(90)
forward(120)
left(90)
forward(360)
penup()

# Draw the red circle
home(0,0)
goto(0,100)
pendown()
fillcolor('red')
begin_fill()
circle(40)
end_fill()
penup()

# Draw the yellow circle (at the center of the drawing)
home()
pendown()
fillcolor('yellow')
begin_fill()
circle(40)
end_fill()
penup()

# Draw the green circle
goto(0,-100)
pendown()
fillcolor('green')
begin_fill()
circle(40)
end_fill()


done()

