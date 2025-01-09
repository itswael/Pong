import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong")

r_paddle = Paddle((350,0))
l_paddle = Paddle((-360,0))
ball = Ball()
scoreboard = Scoreboard()

screen.update()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(r_paddle) < 50 and ball.xcor() >320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.hit()

    if ball.xcor() > 350:
        scoreboard.l_point()
        ball.reset_game()

    if ball.xcor() < -360:
        ball.reset_game()
        scoreboard.r_point()

    game_is_on = scoreboard.check_winner()

screen.exitonclick()