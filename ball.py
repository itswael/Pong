from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        #self.shapesize(stretch_wid=5, stretch_len=1)
        #self.turtlesize(20, 100)
        self.x_move = 10
        self.y_move = 10
        self.pace = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1
        self.pace *= 0.9

    def reset_game(self):
        self.goto(0, 0)
        self.pace = 0.1
        self.bounce()