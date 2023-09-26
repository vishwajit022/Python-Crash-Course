import turtle
tim=turtle.Turtle()
tim.shape("turtle")
tim.color("red","yellow")

for l in range(4):
    tim.forward(100)
    tim.right(90)


screen=turtle.Screen()
screen.exitonclick()

