import turtle

pen = turtle.Turtle()
sc = turtle.Screen()

sc.bgcolor("black")
pen.color('red')

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():

    pen.up()
    pen.goto(-100,-250)
    pen.down()
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(140)
    curve()
    pen.forward(112)
    pen.end_fill()

def text():
    pen.up()
    pen.goto(-150,200)
    pen.down()
    pen.write("A  ", align = "left", font = ("courier",150,"bold italic"))
    pen.up()
    pen.goto(-300,130)
    pen.down()
    pen.write("Aparna ", align = "left", font = ("courier",80,"bold italic"))
    pen.up()
    pen.goto(-300,30)
    pen.down()
    pen.write("My Beastu ", align = "left", font = ("courier",80,"bold italic"))
    pen.up()
    pen.goto(-300,-70)
    pen.down()
    pen.write("I Love You..   ", align = "left", font = ("courier",80,"bold italic"))

text()
heart()
pen.ht()
turtle.done()