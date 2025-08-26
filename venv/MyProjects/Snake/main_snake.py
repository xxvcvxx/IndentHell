import time
from turtle import  Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("MEGA SNAKE!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.listen()

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)

    snake.snake_move()
    if snake.head.distance(food) < 15:
        print("omnom")
        food.respawn()
        snake.add_segment()
        scoreboard.increase_score()





screen.exitonclick()
