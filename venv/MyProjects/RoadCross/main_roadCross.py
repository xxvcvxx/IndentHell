import time
from turtle import Screen
from player import Player
from car_manager import Car_manager

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player = Player()
car = Car_manager()

screen.listen()
screen.onkey(player.up, "Up")
#screen.onkey(player.down, "Down")
#screen.onkey(player.right, "Right")
#screen.onkey(player.left, "Left")

game_is_on = True
cars = [Car_manager() for _ in range(6)]
while game_is_on:
    screen.update()
    time.sleep(0.05)
    for car in cars:
        car.move()
