import turtle  
# Creating turtle  
t = turtle.Turtle()  
  
turtle.bgcolor("black")  
turtle.pensize(2)  
turtle.speed(0)  

colors = ["red", "blue", "magenta", "green", "yellow", "white"]

for i in range(36):  
    turtle.color(colors[i%6])  
    turtle.circle(100)  
    turtle.left(10)  
  
  
t.hideturtle() 
turtle.done()