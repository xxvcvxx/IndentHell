import random
from turtle import Turtle, colormode

colormode(255)
basic_colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (0, 255, 255),
    (255, 0, 255),
]

class Car_manager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(basic_colors))
        self.shapesize(stretch_wid=1, stretch_len=2)
        random_x = random.choice(range(260,-261,-20))
        random_y = random.choice(range(240,-241,-20))
        self.goto(random_x, random_y)
        self.setheading(180)

    def move(self):
        self.forward(10)

    def respawn(self):
        if self.xcor() == -300:
            random_y = random.choice(range(240,-241,-20))
            self.goto(300,random_y)

