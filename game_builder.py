from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

class GameBuilder:
    def __init__(self, player_1, player_2, max_score):
        self.screen = Screen()
        self.r_paddle = Paddle((350,0))
        self.l_paddle = Paddle((-360,0))
        self.ball = Ball()
        self.scoreboard = Scoreboard(player_1, player_2, max_score)

    def build(self):
        self.set_screen()

    def set_screen(self):
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.set_listener()

    def set_listener(self):
        self.screen.listen()
        self.screen.onkey(self.r_paddle.go_up, "Up")
        self.screen.onkey(self.r_paddle.go_down, "Down")
        self.screen.onkey(self.l_paddle.go_up, "w")
        self.screen.onkey(self.l_paddle.go_down, "s")

    def play(self):
        game_is_on = True

        while game_is_on:
            time.sleep(self.ball.pace)
            self.screen.update()
            self.ball.move()
            if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                self.ball.bounce()

            if (self.ball.distance(self.r_paddle) < 50 and self.ball.xcor() > 320) or (
                    self.ball.distance(self.l_paddle) < 50 and self.ball.xcor() < -320):
                self.ball.hit()

            if self.ball.xcor() > 350:
                self.scoreboard.l_point()
                self.ball.reset_game()

            if self.ball.xcor() < -360:
                self.ball.reset_game()
                self.scoreboard.r_point()

            game_is_on = self.scoreboard.check_winner()

    def exitonclick(self):
        self.screen.exitonclick()