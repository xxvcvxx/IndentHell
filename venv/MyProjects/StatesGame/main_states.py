from turtle import Screen, Turtle
import pandas as pd

IMAGE_PATH = "blank_states_img.gif"
DATA_PATH = "50_states.csv"
OUTPUT_PATH = "new.csv"

screen = Screen()
screen.bgpic(IMAGE_PATH)

pen = Turtle()
pen.penup()
pen.hideturtle()

data = pd.read_csv(DATA_PATH)
missing_states_list = data.state.tolist()

game_is_on = True
while game_is_on:
    answer = screen.textinput("States Game", "Enter a state name").title()

    if answer in data.state.tolist():
        row = data[data.state == answer]
        x, y = int(row.x), int(row.y)
        pen.goto(x, y)
        pen.write(answer)
        missing_states_list.remove(answer)

    elif answer == "Exit":
        game_is_on = False

new_csv = pd.DataFrame(missing_states_list, columns=["State"])
new_csv.index = new_csv.index + 1
new_csv.index.name = "No."
new_csv.to_csv(OUTPUT_PATH)
