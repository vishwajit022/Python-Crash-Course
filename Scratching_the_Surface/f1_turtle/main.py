import turtle
tim=turtle.Turtle()
tim.shape("turtle")
tim.color("red","yellow")

for l in range(4):
    tim.forward(100)
    tim.right(90)


screen=turtle.Screen()
screen.exitonclick()

#or we could just use
#from turtle import Turtle 
#inorder to directly import the specific module
#from ____ import __SpecificStuff__

#or we could just
#import turtle as t
#tim=t.Turtle()

import heroes as h
print(h.gen())