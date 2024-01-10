import random
from tkinter import *
import pyperclip

symbols = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+-=?@^_'
length = 8

# create a window
tk = Tk()
tk.resizable(False, False)
tk.title("Password generator")
tk.geometry("500x200")
text_var = StringVar()

# create a label
password_label = Label(tk, textvariable=text_var, width=20, font='corbel 13')
password_label.grid(row=0, column=1, columnspan=2, pady=(25, 20))

# Создаем Canvas для значка копирования
canvas = Canvas(tk, width=22, height=22)
canvas.grid(row=0, column=2, pady=(25, 10), padx=(10, 10))

# Создаем значок копирования (два прямоугольника)
canvas.create_rectangle(5, 5, 15, 15, outline='black')  # Задний прямоугольник
canvas.create_rectangle(10, 10, 20, 20, outline='black', fill=tk.cget("bg"))  # Передний прямоугольник


# создаем функцию выделения значка копирования
def on_enter():
    canvas.config(bg='lightblue')
    canvas.create_rectangle(10, 10, 20, 20, outline='black', fill='lightblue')


def on_leave():
    canvas.config(bg=tk.cget("bg"))
    canvas.create_rectangle(10, 10, 20, 20, outline='black', fill=tk.cget('bg'))


# define a password generation function
def generate_password():
    password = random.sample(symbols, length)
    return ''.join(password)


# создаем функцию очистки значка копирования
def clear_checkmark():
    canvas.delete("all")
    canvas.create_rectangle(5, 5, 15, 15, outline='black')  # Задний прямоугольник
    canvas.create_rectangle(10, 10, 20, 20, outline='black', fill=tk.cget("bg"))  # Передний прямоугольник


canvas.bind("<Enter>", on_enter)
canvas.bind("<Leave>", on_leave)


# определяем функцию копирования в буфер обмена
def copy_to_clipboard(password):
    pyperclip.copy(password)

    # Очищаем Canvas
    canvas.delete("all")
    canvas.unbind("<Enter>")
    canvas.unbind("<Leave>")

    # Создаем галочку при нажатии на значок
    canvas.create_line(0, 5, 10, 15, fill='black', width=2)
    canvas.create_line(10, 15, 25, 0, fill='black', width=2)
    canvas.config(bg=tk.cget("bg"))

    tk.after(2000, clear_checkmark)
    tk.after(2000, lambda: canvas.bind("<Enter>", on_enter))
    tk.after(2000, lambda: canvas.bind("<Leave>", on_leave))


# define a password changing function
def change_password():
    new_password = generate_password()
    text_var.set(new_password)
    clear_checkmark()

    # Привязываем событие клика к функции копирования
    canvas.bind("<Button-1>", lambda event: copy_to_clipboard(new_password))


# создаем функции уменьшения и увеличения длинны пароля при нажатии кнопок
def reducing_length():
    global length
    length -= 1
    text_var.set(generate_password())
    change_quantity()


def increasing_length():
    global length
    length += 1
    text_var.set(generate_password())
    change_quantity()


button = Button(tk, text="generate", width=20, font='corbel 13', pady=0, command=change_password)
button.grid(row=1, column=1, columnspan=2, pady=0, padx=150)

button1 = Button(tk, text='-', width=5, font='Corbel 13', pady=0, command=reducing_length)
button1.grid(row=1, column=1, columnspan=1, pady=0, padx=90, sticky='w')

button2 = Button(tk, text='+', width=5, font='Corbel 13', pady=0, command=increasing_length)
button2.grid(row=1, column=2, columnspan=1, pady=0, padx=90, sticky='e')


quantity = IntVar(value=8)
quantity_label = Label(tk, text="количество символов =", textvariable=quantity, font='corbel 15')
quantity_label.grid(row=2, column=1, columnspan=2, pady=0, padx=0)


# функция изменения длинны пароля
def change_quantity():
    quantity.set(length)


def checkbox_status():
    global symbols
    if var1.get() and var2.get():
        symbols = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+-=?@^_'
    elif not var1.get() and var2.get():
        symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+-=?@^_'
    elif var1.get() and not var2.get():
        symbols = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    else:
        symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


# Создаем переменные для отслеживания состояний чек-боксов
var1 = IntVar(value=1)
var2 = IntVar(value=1)

# Создаем Check buttons
checkbox1 = Checkbutton(tk, text='use digits', variable=var1, command=checkbox_status)
checkbox1.grid(row=3, column=1, columnspan=2, pady=0, padx=150)
checkbox2 = Checkbutton(tk, text='use symbols', variable=var2, command=checkbox_status)
checkbox2.grid(row=4, column=1, columnspan=2, pady=0, padx=150)

tk.mainloop()
