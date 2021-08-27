#importing of module
import turtle
from turtle import *

#initializing a variable for turtle in Turtle for accessing that pen
t = turtle.Turtle()

#setting screen in which turtle will move..
sc = turtle.Screen()
sc.bgcolor('black')

#setting pencolor, speed of movement and width of turtle pen..
t.pencolor('cyan')
t.speed(0)
t.width(10)

# function for making different circles and of different radius
def circle():
    for i in range(7):
        t.circle(150-(i*8))
        t.right(60)

#function for creating circles 
for j in range(8):
    circle()

t.ht()#telling turtle that you may hide now
turtle.done()#telling turtle you can stop your work is done
