import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard_pong import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG PONG")
screen.tracer(0)

game_is_on = True

left_paddle = Paddle('L')
right_paddle = Paddle('R')
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    if abs(ball.xcor()) >= 330 and ball.distance(right_paddle) < 50:
        ball.bounce_with_paddle()
    if abs(ball.xcor()) >= 330 and ball.distance(left_paddle) < 50:
        ball.bounce_with_paddle()

    if ball.xcor() >= 440:
        scoreboard.increase_score("L")
        ball.respawn()
    elif ball.xcor() <= -440:
        scoreboard.increase_score("R")
        ball.respawn()

    screen.update()

screen.exitonclick()
