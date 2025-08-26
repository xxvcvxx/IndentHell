from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update()

    def increase_score(self):
        self.points += 1
        self.update()

    def update(self):
        self.clear()
        self.write("Score: " + str(self.points), align="center", font=("Courier", 15, "bold"))

    def gameover(self):
        self.clear()
        self.goto(0,40)
        self.write("GAME OVER", align="center", font=("Courier", 30, "bold"))
        self.goto(0,-20)
        self.write("Score: " + str(self.points), align="center", font=("Courier", 15, "bold"))
