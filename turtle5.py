# importing turtle module
import turtle
  
# number of sides
n = 100

colors = ['red','blue','green','white','yellow','purple']
  
# creating instance of turtle
pen = turtle.Turtle()
turtle.bgcolor('black')
  
pen.speed(10)

# loop to draw a side
for i in range(n):
    if(i%5==0):
        pen.pencolor(colors[i%6])
    # drawing side of 
    # length i*10
    pen.forward(i * 10)
    pen.width(i/100 + 1)
  
    # changing direction of pen 
    # by 144 degree in clockwise
    pen.right(144)
  
# closing the instance
pen.ht()
turtle.done()