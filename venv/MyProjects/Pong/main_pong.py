import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG PONG")
screen.tracer(0)

game_is_on = True

left_paddle = Paddle('L')
right_paddle = Paddle('R')
ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
    ball.respawn()
    screen.update()

    if ball.distance(left_paddle) < 50:
        ball.bounce_with_paddle()
        print("boom")
    if ball.distance(right_paddle) < 50:
        ball.bounce_with_paddle()
        print("boom")

screen.exitonclick()
