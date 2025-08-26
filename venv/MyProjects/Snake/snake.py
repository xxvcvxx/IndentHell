from turtle import  Screen, Turtle


starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0
class Snake:
    def __init__(self):
        self.snake_body= []
        self.create_snake()
        self.head = self.snake_body[0]

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def create_snake(self):
        for positions in starting_positions:
            self.add_segment(positions)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def snake_move(self):
        for seg in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[seg - 1].xcor()
            new_y = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(new_x,new_y)
        self.snake_body[0].forward(move_distance)
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def hide_snake(self):
        for i in range(len(self.snake_body)):
            self.snake_body[i].hideturtle()


