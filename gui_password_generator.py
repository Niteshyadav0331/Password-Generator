from tkinter import *
import pyperclip
import random

root = Tk()
root.geometry("400x400")
root.title("Password Generator")

passstr = StringVar()
passlen = IntVar()

passlen.set(0)

def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
             'T', 'U', 'V', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             '0', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+',
             ]

    password = ""

    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    passstr.set(password)


def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)


Label(root, text = "Password Generator Application", font = "calibri 20 bold").pack()

Label(root, text = "Enter password length").pack(pady = 3)

Entry(root, textvariable = passlen).pack(pady = 3)

Button(root, text = "Generate Password", command = generate).pack(pady = 7)

Entry(root, textvariable = passstr).pack(pady = 3)

Button(root, text = "Copy to clipboard", command = copytoclipboard).pack()

root.mainloop()