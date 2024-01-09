import random
from tkinter import *
import pyperclip

symbols = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+-=?@^_'

print('Укажите количество паролей для генерации')
quantity = int(input())
print('Укажите длину одного пароля')
lenth = int(input())


def on_enter(event):
    canvas.config(bg='blue')
    canvas.create_rectangle(10, 10, 20, 20, outline='black', fill='blue')


def on_leave(event):
    canvas.config(bg=tk.cget("bg"))
    canvas.create_rectangle(10, 10, 20, 20, outline='black', fill=tk.cget('bg'))


# define a password generation function
def generate_password():
    password = random.sample(symbols, lenth)
    return ''.join(password)


def clear_checkmark():
    canvas.delete("all")
    canvas.create_rectangle(5, 5, 15, 15, outline='black')  # Задний прямоугольник
    canvas.create_rectangle(10, 10, 20, 20, outline='black', fill=tk.cget("bg"))  # Передний прямоугольник


# create a window
tk = Tk()
tk.title("Password generator")
tk.geometry("500x120")
text_var = StringVar()

# create a label
password_label = Label(tk, textvariable=text_var, font='corbel 13')
password_label.grid(row=0, column=1, pady=(25, 0), padx=(150, 10))

# Создаем Canvas для кнопки копирования
canvas = Canvas(tk, width=22, height=22)
canvas.grid(row=0, column=2, pady=(25, 0), padx=(10, 10))

# Создаем значок копирования (два прямоугольника)
canvas.create_rectangle(4, 5, 15, 15, outline='black')  # Задний прямоугольник
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
    print(new_password)

    # Привязываем событие клика к функции копирования
    canvas.bind("<Button-1>", lambda event: copy_to_clipboard(new_password))


button = Button(tk, text="Generate", width=20, font='corbel 13', pady=0, command=change_password)
button.grid(row=1, column=1, columnspan=2, pady=10, padx=150)


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


# Создаем переменные для отслеживания состояний чекбоксов
var1 = IntVar(value=1)
var2 = IntVar(value=1)

# Создаем Checkbuttons
checkbox1 = Checkbutton(tk, text="Использовать цифры", variable=var1, command=checkbox_status)
checkbox1.grid(row=3, column=1, columnspan=2, pady=10, padx=150)
checkbox2 = Checkbutton(tk, text='Использовать символы', variable=var2, command=checkbox_status)
checkbox2.grid(row=4, column=1, columnspan=2, pady=10, padx=150)

tk.mainloop()
