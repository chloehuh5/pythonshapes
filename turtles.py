# pythonshapes
from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0



### Write your code below:
t.begin_fill()
t.fillcolor("HotPink")
var = input('How many sides?')
var = int(var)
for sides in range(var):
    t.forward(25)
    t.left(360/var)
    


t.end_fill()




# Close window on click.
exitonclick()
