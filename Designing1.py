import turtle

t=turtle.Turtle()
t.pencolor("red")

s=turtle.Screen()
s.bgcolor("black")



t.speed(0)

def write():
    t.penup()
    t.goto(-300,-400)
    t.pendown()
    t.pencolor('white')
    t.width(3)
    t.write("Corona Virus",font=("Arial",75,'bold'))

def draw():
    t.penup()
    t.goto(0,200)
    t.pendown()
    a=0
    b=0
    while True:
        t.forward(a)
        t.right(b)
        a+=3
        b+=1
        if b==210:
            break
    
    write()
    


draw()
t.ht()

turtle.done()