import turtle

t = turtle.Turtle()

sc = turtle.Screen()

sc.bgcolor("black")

t.width(2)
t.speed(0)


color=('white','purple','cyan')

for i in range(300):
    t.pencolor(color[i%3])
    t.forward(i*4)
    t.right(121)

t.ht()
t.done()