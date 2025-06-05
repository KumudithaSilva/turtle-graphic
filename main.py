import random
import turtle as t
from turtle import Turtle, Screen
from polygons import turtle_direction

t.colormode(255)
timmy = Turtle()
timmy.shape("classic")
timmy.home()

screen = Screen()

screen_width = screen.window_width() // 3
screen_height = screen.window_height() // 3


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
    screen.tracer(0)
    timmy.speed(0)
    timmy.pensize(9)
    timmy.forward(25)

    while count < 10000:
        random_path = random.randint(0, 3)
        timmy.color(random_color())
        timmy.setheading(turtle_direction[random_path])
        timmy.forward(25)

        x, y = timmy.pos()
        if not -screen_width < x < screen_width and -screen_height < y < screen_height:
            timmy.setheading((timmy.heading() + 180) % 360)
            timmy.forward(25)
        else:
            count += 1
        screen.update()


def draw_spirograph():
    count = 0
    timmy.speed(0)

    while count < 360:
        timmy.color(random_color())
        timmy.setheading(count)
        timmy.circle(radius=100)
        count += 5


screen.exitonclick()
