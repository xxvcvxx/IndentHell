from turtle import  Screen, Turtle


starting_positions = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0)]
class Snake:
    def __init__(self):
        self.snake_body= []
        self.create_snake()

    def create_snake(self):
        for positions in starting_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(positions)
            self.snake_body.append(new_segment)
    def snake_move(self):
        for seg in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[seg - 1].xcor()
            new_y = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(new_x,new_y)
        self.snake_body[0].forward(20)
