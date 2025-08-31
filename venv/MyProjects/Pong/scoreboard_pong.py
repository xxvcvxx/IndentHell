from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points_l = 0
        self.points_r = 0
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update()

    def increase_score(self, side):
        if side == 'L':
            self.points_l += 1
        elif side == "R":
            self.points_r += 1
        self.update()

    def update(self):
        self.clear()
        self.write(str(self.points_l) + " : " + str(self.points_r), align="center", font=("Courier", 25, "bold"))


