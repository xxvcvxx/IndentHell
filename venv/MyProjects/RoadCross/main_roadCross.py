import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard_road import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

def game_over():
    global game_is_on
    game_is_on = False
def death():
    global game_speed
    death_board.increase()
    death_board.update()
    player.respawn()
    level_board.restart()
    level_board.update()
    game_speed = 0.1

def level_up():
    global game_speed
    level_board.increase()
    level_board.update()
    player.respawn()
    game_speed *= GAME_SPEED_MULTIPLIER

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(game_over, "q")
# screen.onkey(player.down, "Down")
# screen.onkey(player.right, "Right")
# screen.onkey(player.left, "Left")

game_is_on = True
TOTAL_CARS = 6
game_speed = 0.1
GAME_SPEED_MULTIPLIER = 0.6
COLLISION_DISTANCE = 20
UPPER_EDGE = 300

cars = [CarManager() for _ in range(int(TOTAL_CARS))]
level_board = Scoreboard("level")
death_board = Scoreboard("deaths")

while game_is_on:
    screen.update()
    time.sleep(game_speed)

    for car in cars:
        car.move()
        if player.distance(car) < COLLISION_DISTANCE:
            death()
        car.respawn()

    if player.ycor() >= UPPER_EDGE:
        level_up()
