import turtle
from turtle import Turtle, Screen
from polygons import polygons

data = polygons

timmy = Turtle()
timmy.shape("classic")
timmy.home()
timmy.speed(1)

def draw_shape(polygons_data):
    for i in range(len(polygons_data)):
         sides = data[i]['sides']
         central_angle = data[i]['central_angle']
         color = data[i]['color']

         timmy.color(color)
         for _ in range(sides):
             timmy.right(central_angle)
             timmy.forward(100)

draw_shape(data)





screen = Screen()
screen.exitonclick()
