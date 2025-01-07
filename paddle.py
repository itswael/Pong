from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        #self.turtlesize(20, 100)
        self.goto(350, 0)

    def go_up(self):
        if self.ycor() < 230:
            new_y = self.ycor() + 20
            self.goto(self.xcor(),new_y)

    def go_down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)