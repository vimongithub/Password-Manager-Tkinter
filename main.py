from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
import pyperclip
#-------------------------------- Password Generator -----------------------------------------------------------
def pass_gen():
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special_char = ["!", "@", "#", "%", "^", "&", "~", "(", ")", "*", "+"]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    pick_latters = [choice(letters) for _ in range(randint(8, 10))]
    pick_symbol = [choice(special_char) for _ in range(randint(2, 4))]
    pick_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_generate = pick_numbers + pick_symbol + pick_latters
    shuffle(password_generate)
    password = "".join(password_generate)
    pass_entry.insert(0, password)
    pyperclip.copy(password)



#---------------------------------------------------------------------------------------------------------------
#Save data into File:
def data_file():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }

    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please filee the remaining fields.")
    else:
        try:
            with open(file="data.json", mode='r') as file:
                # reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open(file="data.json", mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # updating data
            data.update(new_data)
            #save data
            with open(file="data.json", mode='w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)

#---------------------------------------------------------------------------------------------------------------
def search():
    website = website_entry.get()
    try:
        with open(file="data.json") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file Found")
    else:
        for key in data:
            if key == website:
                messagebox.showinfo(title="result",message=f"email : {data[key]['email']}\n "
                                                           f"Password: {data[key]['password']}")
            else:
                messagebox.showinfo(title="Error", message="No match Found")




window = Tk()
window.title("Password Manager")
window.config(pady=40, padx= 40)

canvas = Canvas(height=200, width=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(row=1, column=1)

#labels :

website_label = Label(text="Website:")
website_label.grid(row=2, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=0)
password_label=Label(text="Password:")
password_label.grid(row=4, column=0)

#entries

website_entry = Entry(width = 30)
website_entry.grid(row=2, column=1)
website_entry.focus()

email_entry = Entry(width=30)
email_entry.grid(row=3, column=1)
email_entry.insert(0, string="abc@gmail.com")
pass_entry = Entry(width = 30)
pass_entry.grid(row=4, column=1)

#button
search = Button(text="Search", width=15, command=search)
search.grid(row=2, column=2)

pass_generator = Button(text="Password Generator", command=pass_gen)
pass_generator.grid(row=4, column=2)

add = Button(text="Add", width=20, command=data_file)
add.grid(row=5, column=1)

window.mainloop()