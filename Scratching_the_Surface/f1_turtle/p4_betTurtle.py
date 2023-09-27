import turtle
from turtle import Turtle, Screen
import random

isRaceOn = False

# Set up the screen
screen = Screen()
screen.setup(700, 500)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter a Color?")
colors = ["red", "yellow", "black", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []

# Create turtles and set their initial positions
for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-330, y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Check if the user made a bet
if user_bet:
    isRaceOn = True

while isRaceOn:
    for turtle in all_turtles:
        # Generate a random distance for each turtle to move forward
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        # Check if a turtle has crossed the finish line (x-coordinate > 330)
        if turtle.xcor() > 330:
            winning_color = turtle.pencolor()

            # Check if the user's bet matches the winning turtle's color
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

            # End the race
            isRaceOn = False

# Close the screen when clicked
screen.exitonclick()
