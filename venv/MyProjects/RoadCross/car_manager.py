import random
from turtle import Turtle


class Car_manager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=1, stretch_len=2)
        r_choice=random.choice([300, -300])
        self.goto(r_choice, 0)

    def move(self):
        if self.xcor() == 300:
            self.setheading(-180)
        self.forward(20)
