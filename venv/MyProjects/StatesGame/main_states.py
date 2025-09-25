from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.bgpic("blank_states_img.gif")

pen = Turtle()
pen.penup()
pen.hideturtle()
data = pandas.read_csv("50_states.csv")

game_is_on=True
while game_is_on:
    answer = screen.textinput("StatesGame", "Enter a state name").capitalize()
    if answer in data.state.tolist():
        row = data[data.state == answer]
        x=int(row.x)
        y=int(row.y)
        pen.goto(x,y)
        pen.write(answer)




screen.exitonclick()