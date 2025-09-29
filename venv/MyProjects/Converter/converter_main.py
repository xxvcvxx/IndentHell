from tkinter import *

window = Tk()
window.title("blabla")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

FONT_STYLE = ("Arial", 12, "bold")
PADDING = 10
KM = "Km"
MILES = "Miles"
answer = "0"
to_miles = True

km_lebel = Label(text="Km", font=FONT_STYLE)
miles_lebel = Label(text="Miles", font=FONT_STYLE)
text_lebel = Label(text="Is equal to", font=FONT_STYLE)
answer_lebel = Label(text="0", font=FONT_STYLE)


km_lebel.grid(row=1, column=2, padx=PADDING, pady=PADDING)
miles_lebel.grid(row=0, column=2, padx=PADDING, pady=PADDING)
text_lebel.grid(row=1, column=0, padx=PADDING, pady=PADDING)
answer_lebel.grid(row=1, column=1, padx=PADDING, pady=PADDING)

def button_clicked():
    if to_miles == True:
        value = float(input.get())
        answer_lebel["text"]= value * 0.632371
    elif to_miles == False:
        value = float(input.get())
        answer_lebel["text"]= value * 1.60934

def reverse_button_clicked():
    global to_miles
    to_miles = not to_miles

    if to_miles:
        km_lebel["text"] = KM
        miles_lebel["text"] = MILES
        reverse_button["text"] = "Km → Mile"
    else:
        km_lebel["text"] = MILES
        miles_lebel["text"] = KM
        reverse_button["text"] = "Mile → Km"

calculate_button = Button(text="clik", command=button_clicked, width=30)
calculate_button.grid(row=2, column=1, padx=PADDING, pady=PADDING)

reverse_button = Button(text="Km → Mile", command=reverse_button_clicked, width=10)
reverse_button.grid(row=2, column=0, padx=PADDING, pady=PADDING)

input = Entry(width=30)
input.grid(row=0, column=1)

window.mainloop()
