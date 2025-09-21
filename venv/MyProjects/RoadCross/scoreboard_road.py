from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,type):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.deaths = 0
        self.color("black")
        if type == "level":
            self.goto(200,280)
            self.update_level()
        if type == "deaths":
            self.goto(-200,280)
            self.update_deaths()


    def update_level(self):
        self.clear()
        self.write("Level: "+str(self.level),align="center", font=("Courier", 15, "bold"))
    def update_deaths(self):
        self.clear()
        self.write("Deaths: "+str(self.deaths),align="center", font=("Courier", 15, "bold"))

    def increase_level(self):
        self.level += 1

    def increase_deaths(self):
        self.deaths += 1

    def restart_level(self):
        self.level=1


