import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard_pong import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_HIT_X = 330
OUT_OF_BOUNDS_X = 440
INITIAL_SPEED = 0.05
SPEED_MULTIPLIER = 0.7

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("PONG PONG")
screen.tracer(0)

ball_speed = INITIAL_SPEED
game_running = True

left_paddle = Paddle('L')
right_paddle = Paddle('R')
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


def handle_point_scored(side):
    scoreboard.increase_score(side)
    ball.respawn()
    return INITIAL_SPEED


def handle_paddle_hit(current_speed):
    ball.bounce_with_paddle()
    return current_speed * SPEED_MULTIPLIER


def check_paddle_collision(paddle, current_speed):
    if abs(ball.xcor()) >= PADDLE_HIT_X and ball.distance(paddle) < 50:
        return handle_paddle_hit(current_speed)
    return current_speed


while game_running:
    screen.update()
    time.sleep(ball_speed)
    ball.move()

    ball_speed = check_paddle_collision(right_paddle, ball_speed)
    ball_speed = check_paddle_collision(left_paddle, ball_speed)

    if ball.xcor() >= OUT_OF_BOUNDS_X:
        ball_speed = handle_point_scored("L")
    elif ball.xcor() <= -OUT_OF_BOUNDS_X:
        ball_speed = handle_point_scored("R")

screen.exitonclick()
