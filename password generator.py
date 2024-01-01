import random
from tkinter import *
import pyperclip

symbols = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+-=?@^_'

print('Укажите количество паролей для генерации')
quantity = int(input())
print('Укажите длину одного пароля')
lenth = int(input())


# define a password generation function
def generate_password():
    password = random.sample(symbols, lenth)
    return ''.join(password)


def copy_to_clipboard(password):
    pyperclip.copy(password)
    print('Скопировано')


# create a window
tk = Tk()
tk.title("Password generator")
tk.geometry("500x120")
text_var = StringVar()

# create a label
password_label = Label(tk, textvariable=text_var, font='corbel 13')
password_label.pack(pady=(25, 0))


# define a password changing function
def change_password():
    new_password = generate_password()
    text_var.set(new_password)
    print(text_var)
    # create a copy button
    copy_button = Button(tk, text="Copy to Clipboard", command=lambda: copy_to_clipboard(new_password))
    copy_button.pack(pady=(5, 10))


button = Button(tk, text="Generate", width=20, font='corbel 13', pady=0, command=change_password)
button.pack(side=BOTTOM, pady=10)

tk.mainloop()
