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
cars = [Car_manager() for _ in range(15)]
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for car in cars:
        car.move()
        if player.distance(car) <10:
            game_is_on= False
        car.respawn()

