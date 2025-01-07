import time
from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong")

paddle = Paddle()
screen.update()
screen.listen()
screen.onkey(paddle.go_up,"Up")
screen.onkey(paddle.go_down,"Down")

screen.exitonclick()