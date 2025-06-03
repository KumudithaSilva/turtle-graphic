import random
import turtle as t
from turtle import Turtle, Screen
from polygons import turtle_direction

t.colormode(255)
timmy = Turtle()
timmy.shape("classic")
timmy.home()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_shape():
    for shape in range(3, 11):
        central_angle = 360 / shape
        timmy.color(random_color())
        for _ in range(shape):
            timmy.forward(100)
            timmy.right(central_angle)


def random_walk():
    count = 0
    timmy.speed(0)
    timmy.pensize(9)
    timmy.forward(25)

    while count < 1000:
        random_path = random.randint(0, 3)
        timmy.color(random_color())
        timmy.setheading(turtle_direction[random_path])
        timmy.forward(25)

        count += 1

random_walk()

screen = Screen()
screen.exitonclick()
