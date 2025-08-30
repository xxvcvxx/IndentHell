from turtle import Turtle

border = 250
move_distance = 20



class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.create_paddle(side)

    def create_paddle(self, side):
        self.penup()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid=5, stretch_len=1)
        if side == "L":
            self.goto(-350, 0)
        else:
            self.goto(350, 0)

    def go_up(self):
        if self.ycor() + move_distance <= border:
            self.goto(self.xcor(), self.ycor() + move_distance)

    def go_down(self):
        if self.ycor() - move_distance >= -border:
            self.goto(self.xcor(), self.ycor() - move_distance)

#   def create_paddle(self,side):
#       for positions in starting_positions[side]:
#           new_segment = Turtle("square")
#           new_segment.color("white")
#           new_segment.penup()
#           new_segment.goto(positions)
#           self.paddle_segments.append(new_segment)

#   def up(self):
#       if self.paddle_segments[-1].ycor() + move_distance <= border:
#           for seg in self.paddle_segments:
#               new_y= seg.ycor() + move_distance
#               seg.goto(seg.xcor(),new_y)


#    def down(self):
#        if self.paddle_segments[0].ycor() - move_distance >= -border:
#            for seg in self.paddle_segments:
#                new_y= seg.ycor() - move_distance
#                seg.goto(seg.xcor(),new_y)
#
