import turtle                         # import turtle module
import random                         # import turtle module

t = turtle.Turtle()                  # create a turtle object
t.speed(0)
t.color("blue") # colours 



def snowflake(side_length, levels):       # function to draw snowflake
    if levels == 0:                         # draw a straight line
        t.forward(side_length)
        return
    side_length /= 3.0                      # divide the side length by 3
    snowflake(side_length, levels-1)
    t.left(60)
    snowflake(side_length, levels-1)              # draw 3 smaller snowflakes
    t.right(120)
    snowflake(side_length, levels-1)
    t.left(60)
    snowflake(side_length, levels-1)

t.penup()                    # move the turtle to the starting position   
t.goto(-150, 90)             # goto function to move the turtle to a specific position
t.pendown()                  # draw the snowflake
t.color("blue")


for i in range(3):          # draw 3 snowflakes
    snowflake(100.0, 3)
    t.right(120)
t.penup()                    # move the turtle to the starting position
t.goto(0, 0)
t.pendown()
t.color("red")

for i in range(3):
    snowflake(100.0, 4)
    t.right(120)
t.penup()
t.goto(150, 90)
t.pendown()
t.color("green")

for i in range(3):
    snowflake(100.0, 5)
    t.right(120)
t.penup()
t.goto(-75, -90)
t.pendown()
t.color("yellow")

for i in range(3):
    snowflake(100.0, 6)       # draw 6 snowflakes
    t.right(120)            # right function to turn the turtle to the right
t.penup()
t.goto(75, -90)
t.pendown()
t.color("orange")

for i in range(3):
    snowflake(100.0, 7)
    t.right(120)
t.penup()
t.goto(0, -150)
t.pendown()
t.color("purple")

colors=['#92b6f0','#d95d78','#5cdbb5','#5ccde0','#e0d758','#ed9277']
t.color(random.choice(colors))      # random color
t.color("blue")
t.penup()
t.goto(0, -150)          # goto function to move the turtle to a specific position
t.pendown()
t.pendown()
t.begin_fill()
t.circle(10) 
t.end_fill()

turtle.done()
