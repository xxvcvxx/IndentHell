from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
is_counting = False
def start_timer():
    global is_counting
    if is_counting == False:
        is_counting =True
        count_down(5*60)
def reset_timer():
    global  is_counting
    canvas.itemconfig(timmer_text,text=55)
    is_counting=False
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global is_counting
    count_min = math.floor(count/60)
    count_sec = count % 60

    canvas.itemconfig(timmer_text,text=f"{count_min}:{count_sec}")
    if count >0 and is_counting==True:
        window.after(1000,count_down,count-1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50,pady=50,bg=YELLOW)

canvas = Canvas(bg = YELLOW, highlightthickness = 0)
image =PhotoImage(file="tomato.png")
canvas.create_image(200,112,image=image)
timmer_text= canvas.create_text(200,140, text="5",fill = "white", font=(FONT_NAME,24,"bold"))
timer_label=Label(text="TIMER",fg = GREEN,bg=YELLOW, font=(FONT_NAME,24,"bold"))
checkmark_label = Label(text="✓",fg = GREEN,bg=YELLOW, font=(FONT_NAME,30,"bold"))
start_button=Button(text="Start",command=start_timer,fg = "white",bg=RED, font=(FONT_NAME,18,"bold"),activebackground="darkred")
reset_button=Button(text="Reset",command=reset_timer,fg = "white",bg=RED, font=(FONT_NAME,18,"bold"),activebackground="darkred")


start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
checkmark_label.grid(row=3,column=1)
canvas.grid(row=1, column=1)
timer_label.grid(row=0, column=1)




window.mainloop()