import turtle

t = turtle.Turtle()

sc = turtle.Screen().bgcolor("black")

t.speed(0)
t.width(2)

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

def heart():
    t.color('red','red')
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()


heart()
t.penup()
t.goto(-260,-20)
t.pencolor('red')
t.write("I  You",align = "left",font=('courier',150,'bold italic'))
t.ht()
turtle.done()