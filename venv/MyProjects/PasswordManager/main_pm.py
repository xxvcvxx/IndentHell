from tkinter import *

window =Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=400, height=400)
image = PhotoImage(file="logo2.png")
canvas.create_image(200,200,image = image)
canvas.pack()
window.mainloop()