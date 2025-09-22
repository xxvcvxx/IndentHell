from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.hightscore = 0
        self.get_high_score()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.update()

    def increase_score(self):
        self.points += 1
        self.update()

    def new_high_score(self):
        if int(self.points) > int(self.hightscore):
            with open("highScore.txt","w",encoding="utf-8") as plik:
                plik.write(str(self.points))
            self.hightscore = self.points

    def get_high_score(self):
        with open("highScore.txt", "r", encoding="utf-8") as plik:
            self.hightscore = plik.read().strip()

    def update(self):
        self.clear()
        self.new_high_score()
        self.goto(-100, 280)
        self.write("Score: " + str(self.points), align="center", font=("Courier", 15, "bold"))
        self.goto(100, 280)
        self.write("High Score: " + str(self.hightscore), align="center", font=("Courier", 15, "bold"))

    def end_game_summary(self):
            self.clear()
            self.goto(0,40)
            self.write("GAME OVER", align="center", font=("Courier", 30, "bold"))
            self.goto(0,-20)
            self.write("Score: " + str(self.points), align="center", font=("Courier", 15, "bold"))
            self.goto(0,-50)
            self.write("High Score: " + str(self.hightscore), align="center", font=("Courier", 15, "bold"))