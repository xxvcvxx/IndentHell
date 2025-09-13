from turtle import Turtle

up = 90
down = 270
left = 180
right = 0

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.goto(0,-280)

    def up (self):
        self.setheading(up)
        self.forward(20)

    def down (self):
        self.setheading(down)
        self.forward(20)

    def right (self):
        self.setheading(right)
        self.forward(20)

    def left (self):
        self.setheading(left)
        self.forward(20)


