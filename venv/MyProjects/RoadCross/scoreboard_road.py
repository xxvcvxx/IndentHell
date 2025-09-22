from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,type):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.type = type
        self.color("black")
        if type == "level":
            self.value = 1
            self.goto(200,280)
            self.update()
        if type == "deaths":
            self.value = 0
            self.goto(-200,280)
            self.update()

    def update(self):
        self.clear()
        self.write(f"{self.type.capitalize()}: "+str(self.value),align="center", font=("Courier", 15, "bold"))

    def increase(self):
        self.value +=1

    def restart(self):
        if self.type == "level":
            self.value =1



