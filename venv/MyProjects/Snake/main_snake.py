import time
from turtle import  Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("MEGA SNAKE!")
screen.tracer(0)

snake_body = []

snake = Snake()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.snake_move()








screen.exitonclick()
