import tkinter.messagebox
from tkinter import *
import pyperclip
import json

window = Tk()
window.config(padx=20, pady=20)
window.title("Password Generator")

for x in range(4):
    window.columnconfigure(x, weight=1)
    window.rowconfigure(x, weight=1)

# canvas

canvas = Canvas(highlightthickness=0, width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=0, columnspan=3)

# labels

website_txt = Label(text="Website : ")
website_txt.grid(row=1, column=0)

email_username_txt = Label(text="Email/UserName : ")
email_username_txt.grid(row=2, column=0)

pass_txt = Label(text="Password : ")
pass_txt.grid(row=3, column=0)

# Entries

website_input = Entry()
website_input.grid(row=1, column=1, columnspan=1, sticky='w')
website_input.focus()

email_username_input = Entry(width=30)
email_username_input.insert(END, "cmd.princedaniel@gmail.com")
email_username_input.grid(row=2, column=1, columnspan=2, sticky='w' + 'e')

pass_input = Entry()
pass_input.grid(row=3, column=1, sticky='w')


# button functions

def save():
    website = website_input.get()
    email_username = email_username_input.get()
    password = pass_input.get()

    warning_txt = ""
    if len(website) == 0:
        warning_txt += "Website cannot be empty ! \n"
    if len(email_username) == 0:
        warning_txt += "Email/UserName cannot be empty ! \n"
    if len(password) == 0:
        warning_txt += "Password cannot be empty ! \n"

    if not len(warning_txt) == 0:
        tkinter.messagebox.showwarning("Warning", warning_txt)
    else:
        is_ok = tkinter.messagebox.askokcancel(
            title=website,
            message=f"These are the details entered : \n"
                    f"Email/UserName : {email_username} \n"
                    f"Password : {password}\n\n"
                    "Is it ok to save ? ")
        new_data = {
            website: {
                "email_username": email_username,
                "password": password
            }
        }

        if is_ok:
            try:
                file = open("data.json", "r")
                data = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = new_data
            else:
                data.update(new_data)

            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)

            website_input.delete(0, END)
            email_username_input.delete(0, END)
            pass_input.delete(0, END)


def generate_pass():
    # Password Generator Project
    pass_input.delete(0, END)
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pyperclip.copy(password)
    pass_input.insert(0, password)

    tkinter.messagebox.showinfo(
        title="password generated",
        message="your randomly generated password \n"
                "has been copied to your clipboard."
    )


def print_all_passwords():
    with open("data.json") as file:
        json_data = json.load(file)
    print(json_data)


def find_credentials():
    website_to_find = website_input.get()
    if len(website_to_find) < 3:
        tkinter.messagebox.showwarning(
            title="Field is Empty !",
            message="website name should be greater than 2 characters"
        )
    else:
        try:
            file = open("data.json")  # file_not_found exception
            data = json.load(file)  # json_decode_error exception
            email = data[website_to_find]["email_username"]  # key_error
            password = data[website_to_find]["password"]  # key_error

            tkinter.messagebox.showinfo(
                title="Saved Credentials Found",
                message=f"Email : {email}\nPassword : {password}"
            )
        except FileNotFoundError:
            tkinter.messagebox.showwarning(
                title="no passwords file found",
                message="You don't have any saved passwords !!!"
            )
        except json.decoder.JSONDecodeError:
            tkinter.messagebox.showwarning(
                title="file format not json",
                message="a \"data.json\" file is corrupt, please remove it and try again"
            )
        except KeyError:
            tkinter.messagebox.showwarning(
                title="no credentials found",
                message="You have not stored any credentials for this website"
            )


# Buttons

pass_gen_btn = Button(text="Generate Password", command=generate_pass)
pass_gen_btn.grid(row=3, column=2, sticky='we')

search_btn = Button(text="Search", command=find_credentials)
search_btn.grid(row=1, column=2, sticky='we')

# load_btn = Button(text="Load All Passwords", command=print_all_passwords)
# load_btn.grid(row=3, column=2, sticky='w' + 'e')

save_btn = Button(text="Save", width=25, command=save)
save_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
