import turtle
import random

t = turtle.Turtle()

sc = turtle.Screen()
sc.bgcolor("black")

t.speed(10)

b = random.randint(0,250)

color=['white','red','yellow','pink','cyan']

for i in range(300):
    t.pencolor(color[i%5])
    t.forward(i*3)
    t.right(b)

