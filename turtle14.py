import turtle

t=turtle.Turtle()

sc = turtle.Screen()
sc.bgcolor('black')

t.pencolor('cyan')
t.speed(0)
t.width(10)

def circle():
    for i in range(7):
        t.circle(150-(i*8))
        t.right(60)

for j in range(8):
    circle()

t.ht()
turtle.done()
