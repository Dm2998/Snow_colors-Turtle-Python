import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.color("blue") # colours 



def snowflake(side_length, levels):
    if levels == 0:
        t.forward(side_length)
        return
    side_length /= 3.0
    snowflake(side_length, levels-1)
    t.left(60)
    snowflake(side_length, levels-1)
    t.right(120)
    snowflake(side_length, levels-1)
    t.left(60)
    snowflake(side_length, levels-1)

t.penup()
t.goto(-150, 90)
t.pendown()
t.color("blue")


for i in range(3):
    snowflake(100.0, 3)
    t.right(120)
t.penup()
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
    snowflake(100.0, 6)
    t.right(120)
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
t.color(random.choice(colors))
t.color("blue")
t.penup()
t.goto(0, -150)
t.pendown()
t.begin_fill()
t.circle(10) 
t.end_fill()

turtle.done()
