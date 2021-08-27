# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow','white']
t = turtle.Pen()
t.speed(500)
turtle.bgcolor('black')
for x in range(350):
    t.pencolor(colors[x%7])
    t.width(x/100 + 2)
    t.forward(x)
    t.left(53)

t.ht()
turtle.done()