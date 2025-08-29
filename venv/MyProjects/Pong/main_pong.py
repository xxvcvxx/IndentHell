import time
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG PONG")
screen.tracer(0)

game_is_on = True


left_paddle = Paddle('L')
right_paddle = Paddle('R')

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    screen.update()



screen.exitonclick()