from turtle import Turtle, Screen

screen=Screen()
screen.setup(700,500)
user_bet=screen.textinput(title="Make your bet",prompt="Which Turtle will win the race? Enter a Color?")
color=["red","yellow","black","green","blue","purple"]

for turtle_index in range (0,6):
    tim=Turtle("turtle")
    tim.penup()
    tim.color()
    tim.goto(-330,0)

screen.exitonclick()