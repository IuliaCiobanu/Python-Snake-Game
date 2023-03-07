from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-40, 260)
        self.score = 0
        self.write(f"Score = {self.score}", move=True, font=("Courier", 16, "bold", "normal"))

    def end_the_game(self):
        self.goto(-60, 0)
        self.write("GAME OVER", move=True, font=("Courier", 18, "bold", "normal"))

    def increse_score(self):
        self.clear()
        self.score +=1
        self.setposition(-40, 260)
        self.write(f"Score = {self.score}", move=True, font=("Courier ", 16, "bold", "normal"))

