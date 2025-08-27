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
left_paddle = Paddle('R')
screen.update()



screen.exitonclick()