import turtle

t = turtle.Turtle()

sc = turtle.Screen()

sc.bgcolor("Black")

t.speed(0)

color=['cyan','red','blue','purple',
'white','orange','green','yellow']

for i in range(60):
    t.pencolor(color[i%8])
    t.width(2)
    t.forward(i)
    t.circle(90,steps=5)
    t.forward(i)
    t.right(45)

t.ht()
turtle.done()

