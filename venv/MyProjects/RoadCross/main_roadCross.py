import time
from turtle import Screen
from player import Player
from car_manager import Car_manager

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.up, "Up")
#screen.onkey(player.down, "Down")
#screen.onkey(player.right, "Right")
#screen.onkey(player.left, "Left")

game_is_on = True
total_cars = 2
game_speed =0.1

def game_over():
 pass

cars = [Car_manager() for _ in range(int(total_cars))]
while game_is_on:
    screen.update()
    time.sleep(game_speed)
    for car in cars:
        car.move()
        if player.distance(car) <20:
            game_is_on= False
        car.respawn()
    if player.ycor()>=300:
        player.respawn()
        game_speed *= 0.6

