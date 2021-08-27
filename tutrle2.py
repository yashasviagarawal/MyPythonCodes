import turtle
t=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("black")
t.speed(0)
t.color("white")
for i in range(450):
    t.fd(6+i)
    t.right(91)
    i+=2
turtle.done()