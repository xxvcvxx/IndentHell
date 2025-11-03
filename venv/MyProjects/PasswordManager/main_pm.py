from tkinter import *


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    with open('file.txt','a') as f:
        f.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0,END)
        password_entry.delete(0,END)


window =Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo2.png")
canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1,column=0)

website_entry = Entry(width=50)
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=2,sticky="w", padx=5, pady=5)

email_label = Label(text="Email/UserName")
email_label.grid(row=2,column=0,sticky="w", padx=5, pady=5)

email_entry = Entry(width=50)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"bla@bla.pl")

password_label = Label(text="Password")
password_label.grid(row=3,column=0,sticky="w", padx=5, pady=5)

password_entry = Entry(width=32)
password_entry.grid(row=3,column=1)

gen_password_button = Button(text="Generate Password")
gen_password_button.grid(row=3,column=2,sticky="w")

add_button = Button(text="Add",width=40,command= save)
add_button.grid(row=4, column=1, columnspan=2, pady=10, sticky="we")
















window.mainloop()