import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MEGA SNAKE!")
screen.tracer(0)

border = 300
game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


def game_over():
    global game_is_on
    snake.hide_snake()
    food.hideturtle()
    screen.update()
    scoreboard.gameover()
    game_is_on = False


while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.snake_move()

    # Eating food
    if snake.head.distance(food) < 15:
        food.respawn()
        snake.extend()
        scoreboard.increase_score()

    # Collision with wall
    if abs(snake.head.xcor()) >= border or abs(snake.head.ycor()) >= border:
        game_over()
        game_is_on = False

    # Collision with own body
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_over()


screen.exitonclick()
