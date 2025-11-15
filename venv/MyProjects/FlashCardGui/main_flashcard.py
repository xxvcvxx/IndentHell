from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("FlashCards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(bg=BACKGROUND_COLOR, highlightthickness=0, width=800, height=600)
image = PhotoImage(file="images/card_front.png")
canvas.create_image(400,300,image=image)
canvas.grid(row=1, column=1)

window.mainloop()