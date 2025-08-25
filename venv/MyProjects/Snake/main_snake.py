import time
from turtle import  Screen, Turtle
from snake import Snake
from food import Food

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("MEGA SNAKE!")
screen.tracer(0)

snake_body = []
snake = Snake()
food = Food()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)

    snake.snake_move()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.right,"Right")
    screen.onkey(snake.left,"Left")
    screen.listen()






screen.exitonclick()
