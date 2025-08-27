from turtle import Turtle

starting_positions = {
    "R": [(350, 0), (350, 20), (350, 40)],
    "L": [(-350, 0), (-350, 20), (-350, 40)]
}
move_distance = 20
up = 90
down = 270

class Paddle:
    def __init__(self,side):
        self.paddle_segments = []
        self.create_paddle(side)

    def create_paddle(self,side):
        for positions in starting_positions[side]:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(positions)
            self.paddle_segments.append(new_segment)
