from tkinter import *
from tkinter import messagebox
import random
import json

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data={website:{
        "email": email,
        "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title='Error', message="Please fill all fields!")
    else:
        answer = messagebox.askokcancel(title=website, message="Do you want to save these login details?")
        if answer:
            try:
                with open('file.json', 'r') as f:
                    data=json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                data = {}
            with open('file.json', 'w') as f:
                data.update(new_data)
                json.dump(data,f,indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title= "Success",message="Password has been saved.")


def password_generate():
    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    special_chars = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '{', '|', '}', '~']

    if len(password_entry.get()) != 0:
        password_entry.delete(0,END)

    password_letters = [random.choice(lowercase_letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(special_chars) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

def find_password():
    website = website_entry.get()
    try:
        with open('file.json', 'r') as f:
            data=json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror(title='Error', message="File not found or is corrupted.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Website: {website}\nEmail= {email} \nPassword={password}")


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo2.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

email_label = Label(text="Email/UserName")
email_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "bla@bla.pl")

password_label = Label(text="Password")
password_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

gen_password_button = Button(text="Generate Password", command=password_generate)
gen_password_button.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add", width=40, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10, sticky="we")

search_button = Button(text='Search', bg= '#ADD8E6',fg ='black',width=15,command=find_password)
search_button.grid(row=1, column=2, sticky="w")

window.mainloop()
