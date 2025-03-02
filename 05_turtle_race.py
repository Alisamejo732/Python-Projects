import turtle
import time
import random

# Constat height and width values
WIDTH, HEIGHT = 500, 500
MIN_RACERS = 1
MAX_RACERS = 10

# List of colors
COLORS = ['red', 'brown', 'black', 'pink', 'cyan', 'blue', 'purple', 'green', 'yellow', 'orange']

def get_number_of_racers():
    """
    Input: racers
            Checks if the input value of racers is valid of not
    Return: Returns the value of racers
    """
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
            if MIN_RACERS < racers <= MAX_RACERS:
                break
            else:
                print("Enter number in range (2 - 10)")
        else:
            print("Input is not numeric... Try Again")
    return racers


def create_turtle(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, c in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(c)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) *spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def race_turtles(colors):
    turtles = create_turtle(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= (HEIGHT // 2 -10):
                return colors[turtles.index(racer)]

def init_turtle():
    # Initializing the turtle screen
    screen = turtle.Screen()
    # Setting up the screen height and widht
    screen.setup(WIDTH, HEIGHT)
    # Setting up the screen title (optional)
    screen.title("Turtle Racing!")

# Getting number of racers
no_of_racers = get_number_of_racers()

# Initializing turtle sccreen
init_turtle()

# Shuffling the colors list
random.shuffle(COLORS)
colors = COLORS[:no_of_racers]

# checking for the winner
winner = race_turtles(colors)
print(f"{winner.title()} won the race.")