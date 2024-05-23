from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic"):
        super().__init__(shape)
        self.score = 0
        self.timer = 0.2
        self.penup()
        self.ht()
        self.goto(-230,250)
        self.write(f"Level: {self.score}",align="center",font=("Impact",25,"normal"))

    def update(self):
        self.score += 1
        self.timer *= 0.9
        self.clear()
        self.write(f"Level: {self.score}",align="center",font=("Impact",25,"normal"))
