from turtle import Turtle, Screen
tim=Turtle()
screen=Screen()

def move_forwards():
    tim.forward(10)

def heading_right():
    tim.right(20)

def move_backwards():
    tim.backward(10)

def heading_left():
    tim.left(20)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(move_backwards,"s")
screen.onkey(heading_left,"a")
screen.onkey(heading_right,"d")
screen.onkey(clear,"c")

screen.exitonclick()