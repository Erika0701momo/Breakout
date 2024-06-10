from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-270, 250)
        self.write(f"Score: {self.score}", align="left", font=("Courier", 25, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 25, "normal"))

    def get_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_clear(self):
        self.goto(0, 0)
        self.write("CLEAR!", align="center", font=("Courier", 25, "normal"))