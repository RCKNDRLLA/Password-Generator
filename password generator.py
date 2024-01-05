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
    canvas.bind("<Enter>", on_enter)
    canvas.bind("<Leave>", on_leave)

def on_enter(event):
    canvas.config(bg='white')
    canvas.create_rectangle(10, 10, 20, 20, outline='black', fill='white')
def on_leave(event):
    canvas.config(bg=tk.cget("bg"))
    canvas.create_rectangle(10, 10, 20, 20, outline='black', fill=tk.cget('bg'))


def copy_to_clipboard(password):
    pyperclip.copy(password)
    print('Скопировано')
    # Очищаем Canvas
    canvas.delete("all")
    # Создаем галочку при нажатии на значок
    canvas.create_line(0, 5, 10, 15, fill='black', width=2)
    canvas.create_line(10, 15, 25, 0, fill='black', width=2)
    canvas.unbind("<Enter>", on_enter)





# create a window
tk = Tk()
tk.title("Password generator")
tk.geometry("500x120")
text_var = StringVar()

# create a label
password_label = Label(tk, textvariable=text_var, font='corbel 13')
password_label.grid(row=0, column=1, pady=(25, 0), padx=(150,10))


# Создаем Canvas для кнопки копирования
canvas = Canvas(tk, width=25, height=25)
canvas.grid(row=0, column=2, pady=(25,0), padx=(10, 10))

# Создаем значок копирования (два прямоугольника)
canvas.create_rectangle(5, 5, 15, 15, outline='black')  # Задний прямоугольник
canvas.create_rectangle(10, 10, 20, 20, outline='black', fill=tk.cget("bg"))  # Передний прямоугольник


# define a password changing function
def change_password():
    new_password = generate_password()
    text_var.set(new_password)
    print(new_password)

    # Привязываем событие клика к функции копирования
    canvas.bind("<Button-1>", lambda event: copy_to_clipboard(new_password))


button = Button(tk, text="Generate", width=20, font='corbel 13', pady=0, command=change_password)
button.grid(row=1, column=1, columnspan=2, pady=10, padx=150)

tk.mainloop()
