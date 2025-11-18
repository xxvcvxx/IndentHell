from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/polish_words.csv")
to_learn = data.to_dict(orient="records")




def next_card():
    canvas.itemconfig(image_card, image=image_front)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="Polish")
    canvas.itemconfig(card_word, text=current_card["Polish"])
    window.after(3000, lambda :flip_card(current_card))

def flip_card(current_card):
    canvas.itemconfig(image_card, image=image_back)
    canvas.itemconfig(card_word, text=current_card["English"])

window = Tk()
window.title("FlashCards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(bg=BACKGROUND_COLOR, highlightthickness=0, width=800, height=600)
image_front = PhotoImage(file="images/card_front.png")
image_back= PhotoImage(file="images/card_back.png")
image_card = canvas_front = canvas.create_image(400,300,image=image_front)
canvas.grid(row=1, column=0,columnspan=2)
card_title = canvas.create_text(400, 200, text="WELCOME", font=("Arial", 40, "italic"), fill="gray")
card_word = canvas.create_text(400, 300, text="HEJ", font=("Arial", 60), fill="black")

btn_right_image = PhotoImage(file="images/right.png")
btn_right= Button(image=btn_right_image,borderwidth=0, highlightthickness=0,command=next_card)
btn_right.grid(row=2,column=1)

btn_wrong_image = PhotoImage(file="images/wrong.png")
btn_wrong = Button(image=btn_wrong_image,borderwidth=0, highlightthickness=0,command=next_card)
btn_wrong.grid(row=2, column=0,)


window.mainloop()
