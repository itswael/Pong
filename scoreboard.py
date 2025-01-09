from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, player_1, player_2, max_score):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.update_score()
        self.player_1 = player_1
        self.player_2 = player_2
        self.max_score = max_score

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player_1 +": "+self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 200)
        self.write(self.player_1 +": "+self.r_score, align="center", font=("Courier", 40, "normal"))

    def game_over(self, winner):
        self.clear()
        self.goto(0, 0)
        self.write(f"{winner} Won", align="center", font=("Courier", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def check_winner(self):
        if self.l_score is self.max_score:
            self.game_over(self.player_1)
            return True
        if self.r_score is self.max_score:
            self.game_over(self.player_2)
            return True
        return False