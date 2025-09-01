from turtle import Turtle

border_x = 440
border_y = 290
move_distance = 20
starting_angle = -30


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("White")
        self.right(starting_angle)

    def move(self):
        # self.goto(self.xcor()+5,self.ycor()+5)
        self.forward(5)
        if self.ycor() >= border_y or self.ycor() <= -border_y:
            self.setheading(-self.heading())

    def respawn(self):
        if self.xcor() >= border_x or self.xcor() <= -border_x:
            self.goto(0, 0)

    def bounce_with_paddle(self):
        self.setheading(180 - self.heading())
        self.forward(move_distance)



