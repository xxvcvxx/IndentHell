from turtle import Screen, Turtle

screen = Screen()
screen.bgpic("blank_states_img.gif")

pen = Turtle()
pen.penup()
pen.hideturtle()
answer = screen.textinput("StatesGame", "Enter a state name")
pen.write("blabla")


screen.exitonclick()