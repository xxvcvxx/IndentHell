import time
from turtle import  Screen, Turtle

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("MEGA SNAKE!")
screen.tracer(0)


snake_head = Turtle()
snake_head.shape("square")
snake_head.color("white")
snake_head.penup()
snake_head.goto(20,0)
starting_position = (0,0)
snake_body = [snake_head]


for i in range (0,1):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(starting_position)
    snake_body.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg in range(len(snake_body)-1, 0, -1):
        new_x = snake_body[seg - 1].xcor()
        new_y = snake_body[seg - 1].ycor()
        snake_body[seg].goto(new_x,new_y)
    snake_body[0].forward(20)






screen.exitonclick()
