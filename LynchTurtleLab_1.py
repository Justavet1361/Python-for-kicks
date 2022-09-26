# Programmed by Tamara Lynch: Week 3  and 4 Turtle Lab 1.  
#   14 September 2022.
# This turtle lab demonstrates the creation of a circle, 
#   square, and a shape of the programmer's choice 

# Initialize the turtle as a green turtle shape.
from turtle import*

setup(1200, 900)
shape('turtle')
pencolor('green')
fillcolor('green')
speed(1)
penup()

# Draw the required circle, at x = 200, y = 100, 100 pixels diameter,
    # contrasting pen and fill color, pensize = 10

goto(200, 100)
pen(pencolor = 'red', fillcolor = 'purple', pensize = 10, speed = 2)
pendown()
begin_fill()
circle(100)
end_fill()
penup()

fillcolor('green') # change turtle back to green

# Draw the required square at x = -200, y = -200
#   contrasting pen color and fill color with pensize = 5
#   side length of 200 pixels

goto(-200, -200)
pen(pencolor ='green', fillcolor = 'yellow', pensize = 5, speed = 5)
pendown()
side = 200
begin_fill()
for i in range(4):
    left(90)
    forward(side)
end_fill()
penup()

fillcolor('green') # change the turtle back to green

# Draw a star as the optional shape, with different pen color,
#   pen size, and contrasting fill color.

goto(100,-50)
pen(pencolor='coral', fillcolor = 'cornflower blue', pensize = 7, speed = 3)
pendown()
begin_fill()
for i in range(5):
    forward(200)
    right(144)
end_fill()
penup()

fillcolor('green')

# Relocate the turtle to (0,0)
home()

done()