import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(20)  # Set the drawing speed (0 is fastest)

# Function to generate a random color
def random_color():
    return (random.random(), random.random(), random.random())

# Number of steps for the random walk
num_steps = 10

# Perform the random walk with random colors
for _ in range(num_steps):
    # Set a random color for the Turtle's pen
    t.pencolor(random_color())

    # Randomly select the direction (0-359 degrees)
    angle = random.randint(0, 359)

    # Move the Turtle forward by a random distance
    distance = random.randint(10, 50)
    t.setheading(angle)
    t.forward(distance)

turtle.done()
