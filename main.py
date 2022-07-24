from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox
FONT = ('Livvic', 12)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

    nr_letters = randint(8, 10)
    nr_numbers = randint(2, 4)
    nr_symbols = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters+password_numbers+password_symbols
    shuffle(password_list)
    password = ''.join(password_list)

    password_entry.insert(END, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(password) == 0 or len(website) == 0:
        messagebox.showwarning(
            title='Oops',
            message='Please don\'t leave any field empty!'
        )
    else:
        ok = messagebox.askokcancel(
            title=website,
            message=f'The details entered are: \n Email: {email} \n Password: {password} \n \n Is it ok to save?'
        )

        if ok:
            with open('data.txt', 'a') as file:
                file.write(
                    f'{website} | {email} | {password} \n'
                )
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('PyPAssword Manager')

window.config(
    padx=50,
    pady=50
)

# CANVAS
canvas = Canvas(
    width=200,
    height=200,
    highlightthickness=0
)

img = PhotoImage(
    file='logo.png'
)

canvas.create_image(
    100,
    100,
    image=img
)

canvas.grid(
    row=0,
    column=1
)

# WEBSITE DETAILS
website_text = Label(
    text="Website: ",
    font=FONT
)

website_text.grid(
    row=1,
    column=0
)

website_entry = Entry(
    width=35,
    font=FONT,
    bd=0
)

website_entry.grid(
    row=1,
    column=1,
    columnspan=2
)
website_entry.focus()

# EMAIL DETAILS
email_name = Label(
    text='Email/Username: ',
    font=FONT
)

email_name.grid(
    row=2,
    column=0
)

email_entry = Entry(
    width=35,
    font=FONT,
    bd=0
)

email_entry.insert(END, 'irohjoshuaobiz@gmail.com')

email_entry.grid(
    row=2,
    column=1,
    columnspan=2
)

# PASSWORD DETAILS
password_label = Label(
    text='Password: ',
    font=FONT
)

password_label.grid(
    row=3,
    column=0
)

password_entry = Entry(
    font=FONT,
    bd=0
)

password_entry.grid(
    row=3,
    column=1
)

# GENERATE PASSWORD
genrate_btn = Button(
    text='Generate Password',
    font=('Livvic', 10),
    bd=0,
    bg='white',
    command=generate_password
)

genrate_btn.grid(
    row=3,
    column=2
)

# ADD PASSWORD
add_btn = Button(
    text='Add',
    width=36,
    font=FONT,
    bd=0,
    bg='white',
    command=save
)

add_btn.grid(
    row=4,
    column=1,
    columnspan=2
)


window.mainloop()
